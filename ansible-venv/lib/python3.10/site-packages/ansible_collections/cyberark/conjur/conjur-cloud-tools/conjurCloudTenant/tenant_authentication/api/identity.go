package api

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type IdentityTenant struct {
	ConjurIdentityURL string
	Username          string
	Password          string
}

func NewIdentityTenant(conjurIdentityURL, username, password string) *IdentityTenant {
	return &IdentityTenant{
		ConjurIdentityURL: conjurIdentityURL,
		Username:          username,
		Password:          password,
	}
}

// GetToken retrieves the authentication token for the IdentityTenant.
// It starts the authentication process, sends a POST request to the ConjurIdentityURL,
// and returns the authentication token if successful.
// If there is an error during the authentication process or while sending the POST request,
// an error is returned.
func (i *IdentityTenant) GetToken(sessionID, mechanismID string) (string, error) {
	payload := map[string]interface{}{
		"Action":      "Answer",
		"SessionId":   sessionID,
		"MechanismId": mechanismID,
		"Answer":      i.Password,
	}
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		return "", err
	}

	url := i.ConjurIdentityURL + "/Security/AdvanceAuthentication"
	resp, err := http.Post(url, "application/json", bytes.NewBuffer(payloadBytes))
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusUnauthorized {
		return "", fmt.Errorf("failed to authenticate. Invalid Identity credentials")
	}
	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf("failed to send POST request. Status code: %d", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	var jsonData map[string]interface{}
	err = json.Unmarshal(body, &jsonData)
	if err != nil {
		return "", err
	}

	token, ok := jsonData["Result"].(map[string]interface{})["Token"].(string)
	if !ok {
		return "", fmt.Errorf("failed to retrieve authentication token")
	}

	return token, nil
}

// startAuthentication initiates the authentication process for the IdentityTenant.
// It sends a POST request to the ConjurIdentityURL with the user's username as payload.
// The response contains a session ID and a list of challenges.
// It returns the session ID, mechanism ID, and any error encountered during the process.
func (i *IdentityTenant) StartAuthentication() (string, string, error) {
	payload := map[string]interface{}{
		"Version": "1.0",
		"User":    i.Username,
	}
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		return "", "", err
	}

	url := i.ConjurIdentityURL + "/Security/StartAuthentication"
	resp, err := http.Post(url, "application/json", bytes.NewBuffer(payloadBytes))
	if err != nil {
		return "", "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return "", "", fmt.Errorf("failed to send POST request. Status code: %d", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", "", err
	}

	var jsonData map[string]interface{}
	err = json.Unmarshal(body, &jsonData)
	if err != nil {
		return "", "", err
	}

	sessionID, ok := jsonData["Result"].(map[string]interface{})["SessionId"].(string)
	if !ok {
		return "", "", fmt.Errorf("failed to retrieve session ID")
	}

	challenges, ok := jsonData["Result"].(map[string]interface{})["Challenges"].([]interface{})
	if !ok || len(challenges) == 0 {
		return "", "", fmt.Errorf("failed to retrieve challenges")
	}

	mechanisms, ok := challenges[0].(map[string]interface{})["Mechanisms"].([]interface{})
	if !ok || len(mechanisms) == 0 {
		return "", "", fmt.Errorf("failed to retrieve mechanisms")
	}

	mechanismID, ok := mechanisms[0].(map[string]interface{})["MechanismId"].(string)
	if !ok {
		return "", "", fmt.Errorf("failed to retrieve mechanism ID")
	}

	return sessionID, mechanismID, nil
}

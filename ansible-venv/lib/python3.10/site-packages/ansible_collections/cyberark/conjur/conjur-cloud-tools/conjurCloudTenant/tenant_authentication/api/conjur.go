package api

import (
	"bytes"
	"fmt"
	"io"
	"log"
	"net/http"
)

type ConjurCloud struct {
	conjurCloudURL string
	identityToken  string
	client         *http.Client
}

func NewConjurCloud(conjurCloudURL, identityToken string) *ConjurCloud {
	return &ConjurCloud{
		conjurCloudURL: conjurCloudURL,
		identityToken:  identityToken,
		client:         &http.Client{},
	}
}

// GetToken sends a POST request to the Conjur authentication endpoint to obtain a token.
// It returns the token as a string if the request is successful, otherwise it returns an error.
func (c *ConjurCloud) GetToken() (string, error) {
	url := fmt.Sprintf("%s/api/authn-oidc/cyberark/conjur/authenticate", c.conjurCloudURL)
	payload := []byte("id_token=" + c.identityToken)
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(payload))
	if err != nil {
		log.Printf("failed to create request: %v", err)
		return "", fmt.Errorf("failed to create request: %v", err)
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept-Encoding", "base64")

	resp, err := c.client.Do(req)
	if err != nil {
		log.Printf("failed to send request: %v", err)
		return "", fmt.Errorf("failed to send request: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusUnauthorized {
		log.Println("failed to authenticate. Invalid identity token")
		return "", fmt.Errorf("failed to authenticate. Invalid identity token")
	}
	if resp.StatusCode != http.StatusOK {
		log.Printf("failed to send POST request. Status code: %d", resp.StatusCode)
		return "", fmt.Errorf("failed to send POST request. Status code: %d", resp.StatusCode)
	}

	data, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Printf("failed to read response body: %v", err)
		return "", fmt.Errorf("failed to read response body: %v", err)
	}

	return string(data), nil
}

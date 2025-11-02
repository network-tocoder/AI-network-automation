package api

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
)

type ConjurEdge struct {
	conjurCloudURL string
	conjurToken    string
	edgeName       string
	client         *http.Client
}

func NewConjurEdge(conjurCloudURL, conjurToken, edgeName string) *ConjurEdge {
	return &ConjurEdge{
		conjurCloudURL,
		conjurToken,
		edgeName,
		&http.Client{},
	}
}

// CreateEdge creates a new edge server in Conjur Cloud.
// It sends a POST request to the Conjur API with the edge name as the payload.
// The method returns an error if the request fails or if the edge already exists.
func (ce *ConjurEdge) CreateEdge() error {
	url := fmt.Sprintf("%s/api/edge/conjur", ce.conjurCloudURL)

	payload := struct {
		EdgeName string `json:"edge_name"`
	}{
		EdgeName: ce.edgeName,
	}

	payloadBytes, err := json.Marshal(payload)

	if err != nil {
		log.Printf("failed to marshal payload: %v", err)
		return fmt.Errorf("failed to marshal payload: %v", err)
	}

	req, err := http.NewRequest("POST", url, bytes.NewBuffer(payloadBytes))
	if err != nil {
		log.Printf("failed to create request: %v", err)
		return fmt.Errorf("failed to create request: %v", err)
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept-Encoding", "base64")
	req.Header.Set("Authorization", fmt.Sprintf("Token token=\"%s\"", ce.conjurToken))

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Printf("failed to send request: %v", err)
		return fmt.Errorf("failed to send request: %v", err)
	}

	defer resp.Body.Close()

	switch resp.StatusCode {
	case http.StatusUnauthorized:
		log.Println("failed to authenticate. Invalid conjur token")
		return fmt.Errorf("failed to authenticate. Invalid conjur token")
	case http.StatusCreated:
		log.Println("Edge created successfully")
	case http.StatusConflict:
		log.Println("Edge already exists")
		return fmt.Errorf("edge already exists")
	default:
		log.Printf("failed to send POST request. Status code: %d", resp.StatusCode)
		return fmt.Errorf("failed to send POST request. Status code: %d", resp.StatusCode)
	}

	return nil
}

// GetToken retrieves a token from the Conjur Edge service.
// It sends a GET request to the Conjur Edge API endpoint to obtain the token.
// The method returns the token as a string if the request is successful.
// If there is an error during the request or the response status code is not expected,
// an error is returned along with an error message.
func (ce *ConjurEdge) GetToken() (string, error) {
	url := fmt.Sprintf("%s/api/edge/edge-creds/conjur/%s", ce.conjurCloudURL, ce.edgeName)
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		log.Printf("failed to create request: %v", err)
		return "", fmt.Errorf("failed to create request: %v", err)
	}

	req.Header.Set("Accept-Encoding", "base64")
	req.Header.Set("Authorization", fmt.Sprintf("Token token=\"%s\"", ce.conjurToken))
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Printf("failed to send request: %v", err)
		return "", fmt.Errorf("failed to send request: %v", err)
	}

	defer resp.Body.Close()

	switch resp.StatusCode {
	case http.StatusUnauthorized:
		log.Println("failed to authenticate. Invalid conjur token")
		return "", fmt.Errorf("failed to authenticate. Invalid conjur token")
	case http.StatusOK:
		log.Println("Token retrieved successfully")
	default:
		log.Printf("failed to send GET request. Status code: %d", resp.StatusCode)
		return "", fmt.Errorf("failed to send GET request. Status code: %d", resp.StatusCode)
	}

	data, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Printf("failed to read response body: %v", err)
		return "", fmt.Errorf("failed to read response body: %v", err)
	}

	return string(data), nil
}

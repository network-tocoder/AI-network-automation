package api

import (
	"fmt"
	"io"
	"log"
	"net/http"
)

type Synchronizer struct {
	conjurCloudURL string
	conjurToken    string
	client         *http.Client
}

func NewSynchronizer(conjurCloudURL, conjurToken string) *Synchronizer {
	return &Synchronizer{
		conjurCloudURL: conjurCloudURL,
		conjurToken:    conjurToken,
		client:         &http.Client{},
	}
}

// CreateSynchronizer sends a POST request to the Conjur Cloud API to create a synchronizer.
// It returns an error if the request fails or if the response status code is not as expected.
func (s *Synchronizer) CreateSynchronizer() error {

	url := fmt.Sprintf("%s/api/synchronizer", s.conjurCloudURL)
	req, err := http.NewRequest("POST", url, nil)
	if err != nil {
		log.Printf("failed to create request: %v", err)
		return fmt.Errorf("failed to create request: %v", err)
	}

	req.Header.Set("Authorization", fmt.Sprintf("Token token=\"%s\"", s.conjurToken))
	req.Header.Set("Accept", "application/x.secretsmgr.v2+json")
	req.Header.Set("Accept-Encoding", "base64")

	resp, err := s.client.Do(req)
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
		log.Println("Created synchronizer")
	case http.StatusConflict:
		log.Println("Synchronizer already exists")
	default:
		log.Printf("failed to send POST request. Status code: %d", resp.StatusCode)
		return fmt.Errorf("failed to send POST request. Status code: %d", resp.StatusCode)
	}

	return nil
}

// GetToken retrieves a token from the Conjur Cloud API for authentication.
// It sends a GET request to the specified URL and returns the response body as a string.
// If the request fails or the response status code is not 200 OK, an error is returned.
// The Conjur token and URL are set in the Synchronizer struct.
func (s *Synchronizer) GetToken() (string, error) {

	url := fmt.Sprintf("%s/api/synchronizer/installer-creds", s.conjurCloudURL)
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		log.Printf("failed to create request: %v", err)
		return "", fmt.Errorf("failed to create request: %v", err)
	}

	req.Header.Set("Authorization", fmt.Sprintf("Token token=\"%s\"", s.conjurToken))
	req.Header.Set("Accept", "application/x.secretsmgr.v2+json")
	req.Header.Set("Accept-Encoding", "base64")

	resp, err := s.client.Do(req)
	if err != nil {
		log.Printf("failed to send request: %v", err)
		return "", fmt.Errorf("failed to send request: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusUnauthorized {
		log.Println("failed to authenticate. Invalid conjur token")
		return "", fmt.Errorf("failed to authenticate. Invalid conjur token")
	}
	if resp.StatusCode != http.StatusOK {
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

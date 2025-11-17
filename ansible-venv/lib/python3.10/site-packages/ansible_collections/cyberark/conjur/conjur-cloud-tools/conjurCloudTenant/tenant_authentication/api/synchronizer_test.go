package api_test

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.cyberng.com/Conjur-Enterprise/conjur-cloud-tools/conjur-cloud-tools/tenantAuth/api"
)

func TestCreateSynchronizer(t *testing.T) {
	// Create a test server to mock the HTTP requests
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Verify the request method and URL
		if r.Method != "POST" {
			t.Errorf("Unexpected request method. Expected: POST, Got: %s", r.Method)
		}
		expectedURL := "/api/synchronizer"
		if r.URL.Path != expectedURL {
			t.Errorf("Unexpected request URL. Expected: %s, Got: %s", expectedURL, r.URL.Path)
		}

		// Verify the request headers
		expectedAuthHeader := fmt.Sprintf("Token token=\"%s\"", "test-token")
		if r.Header.Get("Authorization") != expectedAuthHeader {
			t.Errorf("Unexpected Authorization header. Expected: %s, Got: %s", expectedAuthHeader, r.Header.Get("Authorization"))
		}
		expectedAcceptHeader := "application/x.secretsmgr.v2+json"
		if r.Header.Get("Accept") != expectedAcceptHeader {
			t.Errorf("Unexpected Accept header. Expected: %s, Got: %s", expectedAcceptHeader, r.Header.Get("Accept"))
		}
		expectedEncodingHeader := "base64"
		if r.Header.Get("Accept-Encoding") != expectedEncodingHeader {
			t.Errorf("Unexpected Accept-Encoding header. Expected: %s, Got: %s", expectedEncodingHeader, r.Header.Get("Accept-Encoding"))
		}

		// Return a mock response
		w.WriteHeader(http.StatusCreated)
	}))
	defer server.Close()

	// Create a new instance of Synchronizer
	synchronizer := api.NewSynchronizer(server.URL, "test-token")

	// Call the CreateSynchronizer method
	err := synchronizer.CreateSynchronizer()
	if err != nil {
		t.Errorf("Failed to create synchronizer: %v", err)
	}
}
func TestGetSynchronizerToken(t *testing.T) {
	// Create a test server to mock the HTTP requests
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Verify the request method and URL
		if r.Method != "GET" {
			t.Errorf("Unexpected request method. Expected: GET, Got: %s", r.Method)
		}
		expectedURL := "/api/synchronizer/installer-creds"
		if r.URL.Path != expectedURL {
			t.Errorf("Unexpected request URL. Expected: %s, Got: %s", expectedURL, r.URL.Path)
		}

		// Verify the request headers
		expectedAuthHeader := fmt.Sprintf("Token token=\"%s\"", "test-token")
		if r.Header.Get("Authorization") != expectedAuthHeader {
			t.Errorf("Unexpected Authorization header. Expected: %s, Got: %s", expectedAuthHeader, r.Header.Get("Authorization"))
		}
		expectedAcceptHeader := "application/x.secretsmgr.v2+json"
		if r.Header.Get("Accept") != expectedAcceptHeader {
			t.Errorf("Unexpected Accept header. Expected: %s, Got: %s", expectedAcceptHeader, r.Header.Get("Accept"))
		}
		expectedEncodingHeader := "base64"
		if r.Header.Get("Accept-Encoding") != expectedEncodingHeader {
			t.Errorf("Unexpected Accept-Encoding header. Expected: %s, Got: %s", expectedEncodingHeader, r.Header.Get("Accept-Encoding"))
		}

		// Return a mock response
		w.WriteHeader(http.StatusOK)
		_, _ = w.Write([]byte("test-token-response"))
	}))
	defer server.Close()

	// Create a new instance of Synchronizer
	synchronizer := api.NewSynchronizer(server.URL, "test-token")

	// Call the GetToken method
	token, err := synchronizer.GetToken()
	if err != nil {
		t.Errorf("Failed to get token: %v", err)
	}

	// Verify the returned token
	expectedToken := "test-token-response"
	if token != expectedToken {
		t.Errorf("Unexpected token. Expected: %s, Got: %s", expectedToken, token)
	}
}

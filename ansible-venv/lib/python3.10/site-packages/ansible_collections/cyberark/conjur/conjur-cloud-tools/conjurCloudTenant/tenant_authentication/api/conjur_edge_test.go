package api_test

import (
	"fmt"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.cyberng.com/Conjur-Enterprise/conjur-cloud-tools/conjur-cloud-tools/tenantAuth/api"
)

func TestCreateEdge(t *testing.T) {
	// Create a test server to mock the HTTP requests
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Verify the request method and URL
		if r.Method != "POST" {
			t.Errorf("Unexpected request method. Expected: POST, Got: %s", r.Method)
		}
		expectedURL := "/api/edge/conjur"
		if r.URL.Path != expectedURL {
			t.Errorf("Unexpected request URL. Expected: %s, Got: %s", expectedURL, r.URL.Path)
		}

		// Verify the request headers
		expectedAuthHeader := fmt.Sprintf("Token token=\"%s\"", "test-token")
		if r.Header.Get("Authorization") != expectedAuthHeader {
			t.Errorf("Unexpected Authorization header. Expected: %s, Got: %s", expectedAuthHeader, r.Header.Get("Authorization"))
		}
		expectedContentTypeHeader := "application/json"
		if r.Header.Get("Content-Type") != expectedContentTypeHeader {
			t.Errorf("Unexpected Content-Type header. Expected: %s, Got: %s", expectedContentTypeHeader, r.Header.Get("Content-Type"))
		}
		expectedEncodingHeader := "base64"
		if r.Header.Get("Accept-Encoding") != expectedEncodingHeader {
			t.Errorf("Unexpected Accept-Encoding header. Expected: %s, Got: %s", expectedEncodingHeader, r.Header.Get("Accept-Encoding"))
		}

		// Verify the request payload
		expectedPayload := `{"edge_name":"test-edge"}`
		body, _ := io.ReadAll(r.Body)
		if string(body) != expectedPayload {
			t.Errorf("Unexpected request payload. Expected: %s, Got: %s", expectedPayload, string(body))
		}

		// Return a mock response
		w.WriteHeader(http.StatusCreated)
	}))
	defer server.Close()

	// Create a new instance of ConjurEdge
	conjurEdge := api.NewConjurEdge(server.URL, "test-token", "test-edge")

	// Call the CreateEdge method
	err := conjurEdge.CreateEdge()
	if err != nil {
		t.Errorf("Failed to create edge: %v", err)
	}
}
func TestGetEdgeToken(t *testing.T) {
	// Create a test server to mock the HTTP requests
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Verify the request method and URL
		if r.Method != "GET" {
			t.Errorf("Unexpected request method. Expected: GET, Got: %s", r.Method)
		}
		expectedURL := "/api/edge/edge-creds/conjur/test-edge"
		if r.URL.Path != expectedURL {
			t.Errorf("Unexpected request URL. Expected: %s, Got: %s", expectedURL, r.URL.Path)
		}

		// Verify the request headers
		expectedAuthHeader := fmt.Sprintf("Token token=\"%s\"", "test-token")
		if r.Header.Get("Authorization") != expectedAuthHeader {
			t.Errorf("Unexpected Authorization header. Expected: %s, Got: %s", expectedAuthHeader, r.Header.Get("Authorization"))
		}
		expectedEncodingHeader := "base64"
		if r.Header.Get("Accept-Encoding") != expectedEncodingHeader {
			t.Errorf("Unexpected Accept-Encoding header. Expected: %s, Got: %s", expectedEncodingHeader, r.Header.Get("Accept-Encoding"))
		}

		// Return a mock response
		w.WriteHeader(http.StatusOK)
		fmt.Fprint(w, "mock-token")
	}))
	defer server.Close()

	// Create a new instance of ConjurEdge
	conjurEdge := api.NewConjurEdge(server.URL, "test-token", "test-edge")

	// Call the GetToken method
	token, err := conjurEdge.GetToken()
	if err != nil {
		t.Errorf("Failed to get token: %v", err)
	}

	// Verify the returned token
	expectedToken := "mock-token"
	if token != expectedToken {
		t.Errorf("Unexpected token. Expected: %s, Got: %s", expectedToken, token)
	}
}

package api_test

import (
	"bytes"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.cyberng.com/Conjur-Enterprise/conjur-cloud-tools/conjur-cloud-tools/tenantAuth/api"
)

func TestGetConjurToken(t *testing.T) {
	// Create a test server to mock the HTTP requests
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Verify the request method and URL
		if r.Method != "POST" {
			t.Errorf("Unexpected request method. Expected: POST, Got: %s", r.Method)
		}

		// Check the URL
		if r.URL.Path != "/api/authn-oidc/cyberark/conjur/authenticate" {
			t.Errorf("Unexpected URL. Expected: /api/authn-oidc/cyberark/conjur/authenticate, Got: %s", r.URL.Path)
		}

		// Check the headers
		contentType := r.Header.Get("Content-Type")
		acceptEncoding := r.Header.Get("Accept-Encoding")
		if contentType != "application/json" {
			t.Errorf("Unexpected Content-Type header. Expected: application/json, Got: %s", contentType)
		}
		if acceptEncoding != "base64" {
			t.Errorf("Unexpected Accept-Encoding header. Expected: base64, Got: %s", acceptEncoding)
		}

		// Verify the request payload
		expectedPayload := []byte("id_token=test-identity-token")
		body, _ := io.ReadAll(r.Body)

		if !bytes.Equal(body, expectedPayload) {
			t.Errorf("Unexpected request payload. Expected: %s, Got: %s", expectedPayload, string(body))
		}

		// Return a mock response
		response := "mock-token"
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(response))
	}))
	defer server.Close()

	// Create a new instance of ConjurCloud
	conjur := api.NewConjurCloud(server.URL, "test-identity-token")

	// Call the GetToken method
	token, err := conjur.GetToken()
	if err != nil {
		t.Errorf("Failed to get token: %v", err)
	}

	// Verify the returned token
	expectedToken := "mock-token"
	if token != expectedToken {
		t.Errorf("Unexpected token. Expected: %s, Got: %s", expectedToken, token)
	}
}

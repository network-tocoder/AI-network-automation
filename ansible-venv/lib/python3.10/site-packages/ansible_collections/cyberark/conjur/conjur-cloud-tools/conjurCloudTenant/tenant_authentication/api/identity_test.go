package api_test

import (
	"io"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.cyberng.com/Conjur-Enterprise/conjur-cloud-tools/conjur-cloud-tools/tenantAuth/api"
)

func TestStartAuthentication(t *testing.T) {
	// Create a test server to mock the HTTP requests
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Check the URL
		if r.URL.Path != "/Security/StartAuthentication" {
			t.Errorf("Unexpected URL. Expected: /Security/StartAuthentication, Got: %s", r.URL.Path)
		}

		// Check the request method
		if r.Method != http.MethodPost {
			t.Errorf("Unexpected request method. Expected: %s, Got: %s", http.MethodPost, r.Method)
		}

		// Check the payload
		expectedPayload := `{"User":"test-user","Version":"1.0"}`
		body, err := io.ReadAll(r.Body)
		if err != nil {
			t.Errorf("Failed to read request body: %v", err)
		}
		if string(body) != expectedPayload {
			t.Errorf("Unexpected payload. Expected: %s, Got: %s", expectedPayload, string(body))
		}

		// Return a mock response
		response := `{
			"Result": {
				"SessionId": "mock-session-id",
				"Challenges": [
					{
						"Mechanisms": [
							{
								"MechanismId": "mock-mechanism-id"
							}
						]
					}
				]
			}
		}`
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(response))
	}))
	defer server.Close()

	// Create a new instance of IdentityTenant
	identity := api.NewIdentityTenant(server.URL, "test-user", "test-password")

	// Call the StartAuthentication method
	sessionID, mechanismID, err := identity.StartAuthentication()
	if err != nil {
		t.Errorf("Failed to start authentication: %v", err)
	}

	// Verify the returned session ID and mechanism ID
	expectedSessionID := "mock-session-id"
	if sessionID != expectedSessionID {
		t.Errorf("Unexpected session ID. Expected: %s, Got: %s", expectedSessionID, sessionID)
	}

	expectedMechanismID := "mock-mechanism-id"
	if mechanismID != expectedMechanismID {
		t.Errorf("Unexpected mechanism ID. Expected: %s, Got: %s", expectedMechanismID, mechanismID)
	}
}

func TestGetIdentityToken(t *testing.T) {
	// Create a test server to mock the HTTP requests
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// Check the request method
		if r.Method != http.MethodPost {
			t.Errorf("Unexpected request method. Expected: %s, Got: %s", http.MethodPost, r.Method)
		}

		// Check the payload
		expectedPayload := `{"Action":"Answer","Answer":"test-password","MechanismId":"mock-mechanism-id","SessionId":"mock-session-id"}`
		body, err := io.ReadAll(r.Body)
		if err != nil {
			t.Errorf("Failed to read request body: %v", err)
		}
		if string(body) != expectedPayload {
			t.Errorf("Unexpected payload. Expected: %s, Got: %s", expectedPayload, string(body))
		}

		// Check the URL
		if r.URL.Path != "/Security/AdvanceAuthentication" {
			t.Errorf("Unexpected URL. Expected: /Security/AdvanceAuthentication, Got: %s", r.URL.Path)
		}

		// Return a mock response
		response := `{
			"Result": {
				"Token": "mock-token"
			}
		}`
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(response))
	}))
	defer server.Close()

	// Create a new instance of IdentityTenant
	identity := api.NewIdentityTenant(server.URL, "test-user", "test-password")

	// Call the GetToken method
	sessionID := "mock-session-id"
	mechanismID := "mock-mechanism-id"
	token, err := identity.GetToken(sessionID, mechanismID)
	if err != nil {
		t.Errorf("Failed to get token: %v", err)
	}

	// Verify the returned token
	expectedToken := "mock-token"
	if token != expectedToken {
		t.Errorf("Unexpected token. Expected: %s, Got: %s", expectedToken, token)
	}
}

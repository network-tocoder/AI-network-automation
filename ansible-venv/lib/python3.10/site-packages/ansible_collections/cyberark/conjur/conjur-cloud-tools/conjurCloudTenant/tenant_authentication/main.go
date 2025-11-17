package main

import (
	"flag"
	"fmt"
	"log"
	"os"

	"github.cyberng.com/Conjur-Enterprise/conjur-cloud-tools/conjur-cloud-tools/tenantAuth/api"
)

func main() {
	// accept caller input arguments
	identityURL := flag.String("identity-url", "", "Conjur identity URL")
	username := flag.String("username", "", "Conjur username")
	password := flag.String("password", "", "Conjur password")

	conjurURL := flag.String("conjur-url", "", "Conjur cloud URL")
	identityToken := flag.String("identity-token", "", "Identity token")
	conjurToken := flag.String("conjur-token", "", "Conjur token")

	edgeName := flag.String("conjur-edge", "", "Conjur edge name")

	flag.Parse()

	// validate required arguments
	if *identityURL == "" && *conjurURL == "" {
		log.Fatal("Missing required arguments: identity-url or conjur-url")
	}

	if *identityURL != "" && *username == "" {
		log.Fatal("Missing required arguments: username")
	}

	if *conjurToken != "" && *conjurURL == "" {
		log.Fatal("Missing required argument: conjur-url")
	}

	if *conjurURL != "" && *identityToken == "" && *conjurToken == "" {
		log.Fatal("Missing required argument: identity-token")
	}

	// If identityURL is provided, get identity token
	if *identityURL != "" {
		tenantPassword := determine_password(*password)
		// get identity token
		identityToken, err := get_identity_token(*identityURL, *username, tenantPassword)
		if err != nil {
			log.Fatal("Failed to get identity token:", err)
		}
		fmt.Print(identityToken)
		return
	}

	// If conjurURL and identityToken are provided, get conjur token
	if *conjurURL != "" && *identityToken != "" {
		// get conjur token
		conjurToken, err := get_conjur_token(*conjurURL, *identityToken)
		if err != nil {
			log.Fatal("Failed to get conjur token:", err)
		}
		fmt.Print(conjurToken)
		return
	}

	// If conjurToken is provided, get synchronizer token or create conjur edge
	if *conjurToken != "" {
		switch *edgeName {
		case "":
			// get synchronizer token
			synchToken, err := get_synchronizer_token(*conjurURL, *conjurToken)
			if err != nil {
				log.Fatal("Failed to get synchronizer creds:", err)
			}
			fmt.Print(synchToken)
			return
		default:
			// create conjur edge and get token
			conjurEdge, err := create_conjur_edge(*conjurURL, *conjurToken, *edgeName)
			if err != nil {
				log.Fatal("Failed to create conjur edge: ", err)
			}
			fmt.Print(conjurEdge)
			return
		}
	}
}

// get_identity_token retrieves an identity token from the given identity URL using the provided username and password.
// It returns the identity token as a string and any error encountered during the retrieval process.
func get_identity_token(identityURL, username, password string) (string, error) {
	identity_tenant := api.NewIdentityTenant(identityURL, username, password)
	sessionID, mechanismID, err := identity_tenant.StartAuthentication()
	if err != nil {
		return "", err
	}

	identity_token, err := identity_tenant.GetToken(sessionID, mechanismID)
	if err != nil {
		return "", err
	}
	return identity_token, nil
}

// get_conjur_token retrieves a Conjur token from the Conjur Cloud using the provided Conjur URL and identity token.
// It returns the Conjur token and any error encountered during the retrieval process.
func get_conjur_token(conjurURL, identityToken string) (string, error) {
	conjurCloud := api.NewConjurCloud(conjurURL, identityToken)
	conjur_token, err := conjurCloud.GetToken()
	if err != nil {
		return "", err
	}
	return conjur_token, nil
}

// get_synchronizer_token retrieves a synchronizer token from Conjur Cloud.
// It takes the Conjur Cloud URL and Conjur token as input parameters.
// It returns the synchronizer token as a string and any error encountered.
func get_synchronizer_token(conjurCloudURL, conjurToken string) (string, error) {
	synchronizer := api.NewSynchronizer(conjurCloudURL, conjurToken)
	err := synchronizer.CreateSynchronizer()
	if err != nil {
		return "", err
	}
	synch_creds, err := synchronizer.GetToken()
	if err != nil {
		return "", err
	}
	return synch_creds, nil
}

// create_conjur_edge creates a Conjur edge using the provided Conjur Cloud URL, Conjur token, and edge name.
// It returns the Conjur edge token and an error if any.
func create_conjur_edge(conjurCloudURL, conjurToken, edgeName string) (string, error) {
	conjur_edge := api.NewConjurEdge(conjurCloudURL, conjurToken, edgeName)
	err := conjur_edge.CreateEdge()
	if err != nil {
		if err.Error() == "edge already exists" {
			return get_conjur_edge_token(conjurCloudURL, conjurToken, edgeName)
		}
		return "", err
	}

	return get_conjur_edge_token(conjurCloudURL, conjurToken, edgeName)
}

// get_conjur_edge_token retrieves a Conjur Edge token from the Conjur Cloud using the provided Conjur Cloud URL, Conjur token, and edge name.
// It returns the Conjur Edge token and any error encountered during the retrieval process.
func get_conjur_edge_token(conjurCloudURL, conjurToken, edgeName string) (string, error) {
	conjur_edge := api.NewConjurEdge(conjurCloudURL, conjurToken, edgeName)
	conjur_edge_token, err := conjur_edge.GetToken()
	if err != nil {
		return "", err
	}
	return conjur_edge_token, nil
}

// determine_password determines the password for the tenant.
// If the tenantPassword is nil, it retrieves the password from the environment variable CONJUR_CLOUD_ADMIN_PASS.
// If the environment variable is empty, it logs a fatal error.
// Returns the password as a pointer to a string.
func determine_password(tenantPassword string) string {
	if tenantPassword == "" {
		tenantPassword = os.Getenv("CONJUR_CLOUD_ADMIN_PASS")
		if tenantPassword == "" {
			log.Fatal("Missing required argument: password")
		}
		return tenantPassword
	}
	return tenantPassword
}

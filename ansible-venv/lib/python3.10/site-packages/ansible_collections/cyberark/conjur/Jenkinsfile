#!/usr/bin/env groovy
@Library("product-pipelines-shared-library") _

// Automated release, promotion and dependencies
properties([
  // Include the automated release parameters for the build
  release.addParams(),
  // Dependencies of the project that should trigger builds
  dependencies([])
])

// Performs release promotion.  No other stages will be run
if (params.MODE == "PROMOTE") {
  release.promote(params.VERSION_TO_PROMOTE) { infrapool, sourceVersion, targetVersion, assetDirectory ->

    infrapool.agentSh """
      cp "${assetDirectory}/cyberark-conjur-${sourceVersion}.tar.gz" ./cyberark-conjur-${targetVersion}.tar.gz

      export TAG="v${targetVersion}"
      summon ./ci/publish_to_galaxy

      cp ./cyberark-conjur-${targetVersion}.tar.gz "${assetDirectory}/."
    """

  }
  release.copyEnterpriseRelease(params.VERSION_TO_PROMOTE)
  return
}

pipeline {
  agent { label 'conjur-enterprise-common-agent' }

  options {
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '30'))
  }

  triggers {
    cron(getDailyCronString())
  }

  environment {
    MODE = release.canonicalizeMode()
    ANSIBLE_VERSION = 'stable-2.17' 
    PYTHON_VERSION = '3.12' 
  }


  stages {
    stage('Scan for internal URLs') {
      steps {
        script {
          detectInternalUrls()
        }
      }
    }

    stage('Get InfraPool ExecutorV2 Agent') {
      steps {
        script {
          // Request InfraPool
          INFRAPOOL_EXECUTORV2_AGENTS = getInfraPoolAgent(type: "ExecutorV2", quantity: 1, duration: 1)
          INFRAPOOL_EXECUTORV2_AGENT_0 = INFRAPOOL_EXECUTORV2_AGENTS[0]
          infrapool = infraPoolConnect(INFRAPOOL_EXECUTORV2_AGENT_0, {})
        }
      }
    }

    // Generates a VERSION file based on the current build number and latest version in CHANGELOG.md
    stage('Validate Changelog and set version') {
      steps {
        script {
          updateVersion(infrapool, "CHANGELOG.md", "${BUILD_NUMBER}")
        }
      }
    }
    stage ('Run conjur_variable unit tests') {
      steps {
        script {
          infrapool.agentSh './dev/test_unit.sh -r'
          infrapool.agentStash name: 'unit-test-report', includes: 'tests/output/reports/coverage=units/*'
          unstash 'unit-test-report'
        }
        publishHTML (target : [allowMissing: false,
        alwaysLinkToLastBuild: false,
        keepAll: true,
        reportDir: 'tests/output/reports/coverage=units/',
        reportFiles: 'index.html',
        reportName: 'Ansible Coverage Report',
        reportTitles: 'Conjur Ansible Collection report'])
      }
    }

    stage('Run conjur_variable sanity tests') {
      stages {
        stage('conjur_variable sanity tests for Ansible core 2.15') {
          steps {
            script {
              infrapool.agentSh './dev/test_sanity.sh -a stable-2.15 -p 3.10'
            }
          }
        }
        stage('conjur_variable sanity tests for Ansible core 2.16') {
          steps {
            script {
              infrapool.agentSh './dev/test_sanity.sh -a stable-2.16 -p 3.12'
            }
          }
        }
        stage('conjur_variable sanity tests for Ansible core (2.17) - default') {
          steps {
            script {
              infrapool.agentSh './dev/test_sanity.sh -r'
              infrapool.agentStash name: 'sanity-test-report', includes: 'tests/output/reports/coverage=sanity/*'
              unstash 'sanity-test-report'
            }
            publishHTML (target : [allowMissing: false,
            alwaysLinkToLastBuild: false,
            keepAll: true,
            reportDir: 'tests/output/reports/coverage=sanity/',
            reportFiles: 'index.html',
            reportName: 'Ansible Sanity Coverage Report',
            reportTitles: 'Conjur Ansible Collection sanity report'])
          }
        }
      }
    }
    
    stage('Run integration tests with Conjur Open Source') {
      stages {
        stage('Ansible v10 (core 2.17) - latest') {
          stages {
            stage('Deploy Conjur') {
              steps {
                script {
                  infrapool.agentSh './dev/start.sh -v 10 -p 3.12'
                }
              }
            }
            stage('Run tests') {
              parallel {
                stage('Testing conjur_variable lookup plugin') {
                  steps {
                    script {
                      infrapool.agentSh './ci/test.sh -d -t conjur_variable'
                    }
                  }
                  post {
                    always {
                      script {
                        infrapool.agentStash name: 'conjur_variable', includes: 'tests/conjur_variable/junit/*'
                        unstash 'conjur_variable'
                        junit 'tests/conjur_variable/junit/*'
                      }
                    }
                  }
                }

                stage('Testing conjur_host_identity role') {
                  steps {
                    script {
                      infrapool.agentSh './ci/test.sh -d -t conjur_host_identity'
                    }
                  }
                  post {
                    always {
                      script {
                        infrapool.agentStash name: 'conjur_host_identity', includes: 'roles/conjur_host_identity/tests/junit/*'
                        unstash 'conjur_host_identity'
                        junit 'roles/conjur_host_identity/tests/junit/*'
                      }
                    }
                  }
                }
              }
            }
          }
        }

        stage('Ansible v9 (core 2.16)') {
          stages {
            stage('Deploy Conjur') {
              steps {
                script {
                  infrapool.agentSh './dev/start.sh -v 9 -p 3.12'
                }
              }
            }
            stage('Run tests') {
              parallel {
                stage('Testing conjur_variable lookup plugin') {
                  steps {
                    script {
                      infrapool.agentSh './ci/test.sh -d -t conjur_variable'
                    }
                  }
                  post {
                    always {
                      script {
                        infrapool.agentStash name: 'conjur_variable', includes: 'tests/conjur_variable/junit/*'
                        unstash 'conjur_variable'
                        junit 'tests/conjur_variable/junit/*'
                      }
                    }
                  }
                }

                stage('Testing conjur_host_identity role') {
                  steps {
                    script {
                      infrapool.agentSh './ci/test.sh -d -t conjur_host_identity'
                    }
                  }
                  post {
                    always {
                      script {
                        infrapool.agentStash name: 'conjur_host_identity', includes: 'roles/conjur_host_identity/tests/junit/*'
                        unstash 'conjur_host_identity'
                        junit 'roles/conjur_host_identity/tests/junit/*'
                      }
                    }
                  }
                }
              }
            }
          }
        }

        stage('Ansible v8 (core 2.15)') {
          stages {
            stage('Deploy Conjur') {
              steps {
                script {
                  infrapool.agentSh './dev/start.sh -v 8 -p 3.11'
                }
              }
            }
            stage('Run tests') {
              parallel {
                stage('Testing conjur_variable lookup plugin') {
                  steps {
                    script {
                      infrapool.agentSh './ci/test.sh -d -t conjur_variable'
                    }
                  }
                  post {
                    always {
                      script {
                        infrapool.agentStash name: 'conjur_variable', includes: 'tests/conjur_variable/junit/*'
                        unstash 'conjur_variable'
                        junit 'tests/conjur_variable/junit/*'
                      }
                    }
                  }
                }

                stage('Testing conjur_host_identity role') {
                  steps {
                    script {
                      infrapool.agentSh './ci/test.sh -d -t conjur_host_identity'
                    }
                  }
                  post {
                    always {
                      script {
                        infrapool.agentStash name: 'conjur_host_identity', includes: 'roles/conjur_host_identity/tests/junit/*'
                        unstash 'conjur_host_identity'
                        junit 'roles/conjur_host_identity/tests/junit/*'
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

    stage('Run integration tests with Conjur Enterprise') {
      stages {
        stage('Deploy Conjur Enterprise') {
          steps {
            script {
              infrapool.agentSh './dev/start.sh -e -v 10 -p 3.12'
            }
          }
        }
        stage('Run tests') {
          parallel {
            stage("Testing conjur_variable lookup plugin") {
              steps {
                script {
                  infrapool.agentSh './ci/test.sh -d -t conjur_variable'
                }
              }
              post {
                always {
                  script {
                    infrapool.agentStash name: 'conjur_variable', includes: 'tests/conjur_variable/junit/*'
                    unstash 'conjur_variable'
                    junit 'tests/conjur_variable/junit/*'
                  }
                }
              }
            }
            stage("Testing conjur_host_identity role") {
              steps {
                script {
                  infrapool.agentSh './ci/test.sh -d -t conjur_host_identity'
                }
              }
              post {
                always {
                  script {
                    infrapool.agentStash name: 'conjur_host_identity', includes: 'roles/conjur_host_identity/tests/junit/*'
                    unstash 'conjur_host_identity'
                    junit 'roles/conjur_host_identity/tests/junit/*'
                  }
                }
              }
            }
          }
        }
      }
    }
    
    stage('Run Conjur Cloud tests') {
      stages {
        stage('Create a Tenant') {
          steps {
            script {
              TENANT = getConjurCloudTenant()
            }
          }
        }
        stage('Authenticate') {
          steps {
            script {
              def id_token = getConjurCloudTenant.tokens(
                infrapool: infrapool,
                identity_url: "${TENANT.identity_information.idaptive_tenant_fqdn}",
                username: "${TENANT.login_name}"
              )

              def conj_token = getConjurCloudTenant.tokens(
                infrapool: infrapool,
                conjur_url: "${TENANT.conjur_cloud_url}",
                identity_token: "${id_token}"
                )

              env.conj_token = conj_token
            }
          }
        }
        stage('Run tests against Tenant') {
          environment {
            INFRAPOOL_CONJUR_APPLIANCE_URL="${TENANT.conjur_cloud_url}"
            INFRAPOOL_CONJUR_AUTHN_LOGIN="${TENANT.login_name}"
            INFRAPOOL_CONJUR_AUTHN_TOKEN="${env.conj_token}"
            INFRAPOOL_TEST_CLOUD=true
          }
          steps {
            script {
              infrapool.agentSh "./dev/start.sh -c -v 10 -p 3.12"
            }
          }
        }
        stage('Ansible v10 (core 2.17) - latest') {
          stages {
            stage('Run tests') {
              parallel {
                stage('Testing conjur_variable lookup plugin') {
                  steps {
                    script {
                      infrapool.agentSh './ci/test.sh -d -t conjur_variable'
                    }
                  }
                  post {
                    always {
                      script {
                        infrapool.agentStash name: 'conjur_variable', includes: 'tests/conjur_variable/junit/*'
                        unstash 'conjur_variable'
                        junit 'tests/conjur_variable/junit/*'
                      }
                    }
                  }
                }
                stage('Testing conjur_host_identity role') {
                  steps {
                    script {
                      infrapool.agentSh './ci/test.sh -d -t conjur_host_identity'
                    }
                  }
                  post {
                    always {
                      script {
                        infrapool.agentStash name: 'conjur_host_identity', includes: 'roles/conjur_host_identity/tests/junit/*'
                        unstash 'conjur_host_identity'
                        junit 'roles/conjur_host_identity/tests/junit/*'
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    stage('Build artifacts') {
      steps {
        script {
          infrapool.agentSh './ci/build_release'
        }
      }
    }
    stage('Release') {
      when {
        expression {
          MODE == "RELEASE"
        } 
      }
      steps {
        script {
          release(infrapool) { billOfMaterialsDirectory, assetDirectory, toolsDirectory ->
            // Publish release artifacts to all the appropriate locations
            // Copy any artifacts to assetDirectory to attach them to the Github release
            infrapool.agentSh "cp cyberark-conjur-*.tar.gz  ${assetDirectory}"
          }
        }
      }
    }
  }
  post {
    always {
      script {
            deleteConjurCloudTenant("${TENANT.id}")
      }
      releaseInfraPoolAgent(".infrapool/release_agents")
    }
  }
}

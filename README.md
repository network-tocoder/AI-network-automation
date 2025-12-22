# 🚀 Network Automation Series

![Network Coder Banner](assets/banner.jpg)

**Network | AI | Tool Integration | Virtual LAB | Automation**

[![YouTube](https://img.shields.io/badge/YouTube-NetworkCoder-red?style=for-the-badge&logo=youtube)](https://youtube.com/@NetworkCoder)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/network-tocoder)

---

## 🎓 What You'll Learn

This series takes you from zero to hero in network automation. Build a complete virtual lab, automate firewalls, deploy NetBox for infrastructure management, and integrate everything with modern DevOps tools.

---

## 📺 Video Index

| # | Video | Topic | YouTube |
|---|-------|-------|---------|
| 1 | [EVE-NG Installation](#video-1-eve-ng-installation--virtual-lab-setup) | EVE-NG, Virtual Lab Setup | [▶️ Watch](https://www.youtube.com/watch?v=ABNOS7GypxA) |
| 2 | [Build Automation Environment](#video-2-build-automation-environment-inside-eve-ng) | Linux, Ansible, VS Code | [▶️ Watch](https://www.youtube.com/watch?v=NPq7AjCguBY) |
| 3 | [Git Workflow](#video-3-git-workflow-for-network-engineers) | Git, GitHub, Version Control | [▶️ Watch](https://www.youtube.com/watch?v=vykDi7PFeW0) |
| 4 | [Deploy FortiGate](#video-4-deploy-fortigate-firewall-on-eve-ng) | FortiGate, EVE-NG | [▶️ Watch](https://www.youtube.com/watch?v=8W9OJAP773s) |
| 5 | [FortiGate + Ansible](#video-5-fortigate-automation-using-ansible) | Ansible, Vault, Playbooks | [▶️ Watch](https://www.youtube.com/watch?v=3VL-JRIJT8M) |
| 6 | [FortiGate + REST API](#video-6-fortigate-automation-using-rest-api) | REST API, Postman | [▶️ Watch](https://www.youtube.com/watch?v=Eqy4q9SsmtE) |
| 7 | [NetBox + Docker](#video-7-netbox-installation-using-docker) | NetBox, Docker Compose | [▶️ Watch](https://www.youtube.com/watch?v=OGQGly7NIFY) |
| 8 | [NetBox Dynamic Inventory](#video-8-netbox-dynamic-inventory---core-concepts) | ORB, DIODE, Architecture | [▶️ Watch](https://www.youtube.com/watch?v=JZ-jDCT8mQY) |
| 9 | [NetBox Auto-Discovery](#video-9-netbox-auto-discovery---complete-setup-guide) | DIODE, ORB Agent, OAuth | [▶️ Watch](https://www.youtube.com/watch?v=DODzEsMTmKQ) |
| 10 | [pyATS + NetBox](#video-10-pyats--netbox-integration) | pyATS, Network Testing | [▶️ Watch](https://www.youtube.com/watch?v=V_PmWxC2QDA) |

---

## 🛠️ Tech Stack

![EVE-NG](https://img.shields.io/badge/EVE--NG-00A98F?style=for-the-badge&logo=vmware&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NetBox](https://img.shields.io/badge/NetBox-0078D4?style=for-the-badge&logo=buffer&logoColor=white)
![FortiGate](https://img.shields.io/badge/FortiGate-EE3124?style=for-the-badge&logo=fortinet&logoColor=white)
![Cisco](https://img.shields.io/badge/Cisco-1BA0D7?style=for-the-badge&logo=cisco&logoColor=white)

---

## Video 1: EVE-NG Installation & Virtual Lab Setup

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=ABNOS7GypxA)

### 📋 Overview

Install EVE-NG on VMware Workstation and build your first virtual network topology.

### 🎯 What You'll Learn

- Install EVE-NG on VMware Workstation
- Build your first virtual network topology
- Configure network devices for automation

### 💻 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 4 Cores (VT-x/AMD-V enabled) | 8+ Cores |
| RAM | 8 GB | 16+ GB |
| Storage | 50 GB | 100+ GB SSD |
| Hypervisor | VMware/VirtualBox | VMware Workstation Pro |

### 💻 Commands

<details>
<summary>1. Initial Setup After Boot</summary>

```bash
# Default credentials
Username: root
Password: eve

# The setup wizard will guide you through:
# - Hostname configuration
# - Domain name
# - Network configuration (DHCP or Static IP)
# - Root password change
```

</details>

<details>
<summary>2. Update EVE-NG</summary>

```bash
# Update system packages
apt update && apt upgrade -y

# Fix any broken packages
apt --fix-broken install
```

</details>

<details>
<summary>3. Access Web Interface</summary>

```bash
# Find your EVE-NG IP address
ip addr show
hostname -I

# Access in browser: http://YOUR-EVE-NG-IP
# Default web credentials:
# Username: admin
# Password: eve
```

</details>

<details>
<summary>4. Upload Device Images</summary>

```bash
# Connect via SFTP/SCP
# Upload images to appropriate folders:

# Cisco IOS/IOL
/opt/unetlab/addons/iol/bin/

# Cisco VIRL/QEMU images
/opt/unetlab/addons/qemu/

# Fix permissions after upload
/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
```

</details>

<details>
<summary>5. Useful EVE-NG Commands</summary>

```bash
# Check EVE-NG service status
systemctl status eve-ng

# Restart EVE-NG services
systemctl restart eve-ng

# Fix permissions (run after adding images)
/opt/unetlab/wrappers/unl_wrapper -a fixpermissions

# Stop all running nodes
/opt/unetlab/wrappers/unl_wrapper -a stopall
```

</details>

### 🔗 Resources

- [EVE-NG Official Website](https://www.eve-ng.net/)
- [EVE-NG Documentation](https://www.eve-ng.net/index.php/documentation/)

---

## Video 2: Build Automation Environment Inside EVE-NG

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=NPq7AjCguBY)

### 📋 Overview

Deploy a Linux node inside EVE-NG, install Ansible, and integrate VS Code for a professional automation workflow.

### 🎯 What You'll Learn

- Deploy Linux node in EVE-NG
- Install Ansible for network automation
- Integrate VS Code for professional workflow

### 💻 Commands

<details>
<summary>1. Update Ubuntu & Install Prerequisites</summary>

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Check Python version
python3 --version

# Install OpenSSH Server
sudo apt install openssh-server -y
sudo systemctl enable ssh
sudo systemctl start ssh

# Install Python venv
sudo apt install python3-venv -y
```

</details>

<details>
<summary>2. Create Project & Virtual Environment</summary>

```bash
# Create Ansible project directory
mkdir ~/ansible-project
cd ~/ansible-project

# Create virtual environment
python3 -m venv ansible-venv

# Activate virtual environment
source ansible-venv/bin/activate
```

</details>

<details>
<summary>3. Install Ansible</summary>

```bash
# Upgrade pip
pip install --upgrade pip

# Install Ansible
pip install ansible

# Verify installation
ansible --version
```

</details>

<details>
<summary>4. Create Alias for Quick Access</summary>

```bash
# Add alias to .bashrc
echo "alias netdev='cd ~/ansible-project && source ansible-venv/bin/activate'" >> ~/.bashrc

# Reload bashrc
source ~/.bashrc

# Now just type 'netdev' to activate environment
```

</details>

<details>
<summary>5. VS Code Remote SSH Setup</summary>

```bash
# Get Linux node IP
ip addr show

# In VS Code:
# 1. Install "Remote - SSH" extension
# 2. Press F1 → "Remote-SSH: Connect to Host"
# 3. Enter: user@YOUR-LINUX-IP
# 4. Select Linux, enter password
```

</details>

### 🔗 Resources

- [Ansible Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/)
- [VS Code Remote SSH](https://code.visualstudio.com/docs/remote/ssh)

---

## Video 3: Git Workflow for Network Engineers

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=vykDi7PFeW0)

### 📋 Overview

Learn Git version control essentials and push your Ansible projects to GitHub.

### 🎯 What You'll Learn

- Complete Git workflow explained
- Push Ansible projects to GitHub
- Version control for network automation

### 💻 Commands

<details>
<summary>1. Install & Configure Git</summary>

```bash
# Install Git
sudo apt install git -y

# Configure Git identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list
```

</details>

<details>
<summary>2. Generate SSH Key for GitHub</summary>

```bash
# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Start SSH agent and add key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

# Display public key (copy this to GitHub)
cat ~/.ssh/id_rsa.pub

# Test GitHub connection
ssh -T git@github.com
```

</details>

<details>
<summary>3. Initialize Repository & First Commit</summary>

```bash
# Initialize repository
cd ~/ansible-project
git init

# Add files to staging
git add .

# First commit
git commit -m "Initial commit"
```

</details>

<details>
<summary>4. Push to GitHub</summary>

```bash
# Add remote origin (SSH method)
git remote add origin git@github.com:username/repo.git

# Push to main branch
git push -u origin main
```

</details>

<details>
<summary>5. Configure .gitignore</summary>

```bash
# Create .gitignore
cat > .gitignore << 'EOF'
# Virtual Environments
ansible-venv/
venv/
.venv/

# Python
__pycache__/
*.pyc

# IDE
.vscode/
.idea/

# OS
.DS_Store
EOF

# If venv was already tracked, remove it
git rm -r --cached ansible-venv/
git add .gitignore
git commit -m "Add gitignore and remove venv from tracking"
```

</details>

<details>
<summary>6. Common Git Commands</summary>

```bash
# Check status
git status

# View commit history
git log --oneline

# Create new branch
git checkout -b feature-branch

# Merge branch
git merge feature-branch

# Pull latest changes
git pull origin main

# Stash changes
git stash
git stash pop
```

</details>

### 🔗 Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub SSH Setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

---

## Video 4: Deploy FortiGate Firewall on EVE-NG

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=8W9OJAP773s)

### 📋 Overview

Install and configure FortiGate firewall in your EVE-NG virtual lab.

### 🎯 What You'll Learn

- FortiGate installation in virtual lab
- Network security device configuration
- Integration with automation stack

### 💻 Commands

<details>
<summary>1. Upload FortiGate Image to EVE-NG</summary>

```bash
# Upload FortiGate qcow2 image via SFTP to:
/opt/unetlab/addons/qemu/fortinet-FGT/

# Fix permissions
/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
```

</details>

<details>
<summary>2. FortiGate Initial Configuration</summary>

```bash
# Default credentials
Username: admin
Password: (blank - press Enter)

# Set new password
config system admin
    edit admin
        set password YourNewPassword
    next
end

# Configure management interface
config system interface
    edit port1
        set ip 192.168.1.111/24
        set allowaccess ping https ssh http
    next
end

# Set default gateway
config router static
    edit 1
        set gateway 192.168.1.1
        set device port1
    next
end
```

</details>

<details>
<summary>3. Create API Admin User</summary>

```bash
# Create API admin user
config system api-user
    edit "api-admin"
        set accprofile "super_admin"
        set vdom "root"
        config trusthost
            edit 1
                set ipv4-trusthost 192.168.1.0/24
            next
        end
    next
end

# Generate API token from GUI:
# System > Administrators > api-admin > Regenerate
```

</details>

### 🔗 Resources

- [FortiGate Documentation](https://docs.fortinet.com/product/fortigate)

---

## Video 5: FortiGate Automation Using Ansible

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=3VL-JRIJT8M)

### 📋 Overview

Automate FortiGate firewalls using Ansible with secure credential storage via Ansible Vault.

### 🎯 What You'll Learn

- Install Ansible Collections for FortiGate
- Ansible Vault Setup
- Demo Playbook 1 - System Information Check
- Demo Playbook 2 - Deploy Firewall Policy

### 📁 Project Structure

```
ansible-project/
├── ansible.cfg
├── inventory/
│   └── hosts
├── host_vars/
│   └── Forti-FW-1.yml (encrypted)
└── playbooks/
    ├── fortigate_system_info.yml
    └── fortigate_create_policy.yml
```

### 💻 Commands

<details>
<summary>1. Install FortiGate Collection</summary>

```bash
# Check Ansible version
ansible --version

# Install FortiGate collection
ansible-galaxy collection install fortinet.fortios

# Verify installation
ansible-galaxy collection list | grep fortinet
```

</details>

<details>
<summary>2. Ansible Vault Commands</summary>

```bash
# Create encrypted vault file
ansible-vault create host_vars/Forti-FW-1.yml

# View encrypted file (shows encrypted text)
cat host_vars/Forti-FW-1.yml

# View decrypted content
ansible-vault view host_vars/Forti-FW-1.yml

# Edit encrypted file
ansible-vault edit host_vars/Forti-FW-1.yml

# Change vault password
ansible-vault rekey host_vars/Forti-FW-1.yml
```

</details>

<details>
<summary>3. Inventory Verification</summary>

```bash
# List all inventory with vault decryption
ansible-inventory --list -i inventory/hosts --ask-vault-pass

# Check specific host variables
ansible-inventory --host Forti-FW-1 --ask-vault-pass

# View inventory in YAML format
ansible-inventory --list -i inventory/hosts --ask-vault-pass --yaml
```

</details>

<details>
<summary>4. Run Playbooks</summary>

```bash
# Run system info playbook
ansible-playbook playbooks/fortigate_system_info.yml --ask-vault-pass

# Run with verbose output
ansible-playbook playbooks/fortigate_system_info.yml --ask-vault-pass -vvv

# Create firewall policy
ansible-playbook playbooks/fortigate_create_policy.yml --ask-vault-pass

# Dry run (check mode)
ansible-playbook playbooks/fortigate_create_policy.yml --ask-vault-pass --check
```

</details>

<details>
<summary>5. Inventory File (inventory/hosts)</summary>

```ini
[fortigates]
Forti-FW-1 ansible_host=192.168.1.111

[fortigates:vars]
ansible_network_os=fortinet.fortios.fortios
ansible_connection=httpapi
ansible_httpapi_use_ssl=yes
ansible_httpapi_validate_certs=no
ansible_httpapi_port=443
```

</details>

### 🔗 Resources

- [Fortinet Ansible Collection](https://galaxy.ansible.com/fortinet/fortios)
- [FortiOS Ansible Docs](https://ansible-galaxy-fortios-docs.readthedocs.io/)

---

## Video 6: FortiGate Automation Using REST API

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=Eqy4q9SsmtE)

### 📋 Overview

Automate FortiGate using REST API with Postman and VS Code integration.

### 🎯 What You'll Learn

- REST API automation with Postman
- VS Code integration for API testing
- CRUD operations (GET, POST, PUT, DELETE)

### 📁 FortiGate API Structure

```
/api/v2/
├── cmdb/      → Configuration (Create, Read, Update, Delete)
├── monitor/   → Status & Monitoring (Read-only)
└── log/       → Logs & Events (Read-only)
```

### 🔧 Postman Environment Variables

| Variable | Value |
|----------|-------|
| `base_url` | `https://your-fortigate-ip` |
| `api_token` | `your-api-token` |
| `vdom` | `root` |

### 💻 API Endpoints & Commands

<details>
<summary>1. GET - System Monitoring</summary>

**Endpoint:**
```
https://{{base_url}}/api/v2/monitor/system/status?vdom={{vdom}}
```

**cURL:**
```bash
curl -k -X GET "https://192.168.1.111/api/v2/monitor/system/status?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

**Headers:**
```
Authorization: Bearer {{api_token}}
```

</details>

<details>
<summary>2. POST - Create Firewall Address</summary>

**Endpoint:**
```
https://{{base_url}}/api/v2/cmdb/firewall/address?vdom={{vdom}}
```

**cURL:**
```bash
curl -k -X POST "https://192.168.1.111/api/v2/cmdb/firewall/address?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "API_Demo_Server",
    "subnet": "10.0.5.100 255.255.255.255",
    "type": "ipmask",
    "comment": "Created via Postman API"
  }'
```

**Request Body (JSON):**
```json
{
  "name": "API_Demo_Server",
  "subnet": "10.0.5.100 255.255.255.255",
  "type": "ipmask",
  "comment": "Created via Postman API"
}
```

</details>

<details>
<summary>3. PUT - Update Interface</summary>

**Endpoint:**
```
https://{{base_url}}/api/v2/cmdb/system/interface/port2?vdom={{vdom}}
```

**cURL:**
```bash
curl -k -X PUT "https://192.168.1.111/api/v2/cmdb/system/interface/port2?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "alias": "LAN-Internal",
    "description": "Updated via Postman API"
  }'
```

**Request Body (JSON):**
```json
{
  "alias": "LAN-Internal",
  "description": "Updated via Postman API"
}
```

</details>

<details>
<summary>4. GET - Firewall Addresses & Policies</summary>

```bash
# Get all firewall addresses
curl -k -X GET "https://192.168.1.111/api/v2/cmdb/firewall/address?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"

# Get all firewall policies
curl -k -X GET "https://192.168.1.111/api/v2/cmdb/firewall/policy?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"

# Get system interfaces
curl -k -X GET "https://192.168.1.111/api/v2/cmdb/system/interface?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

</details>

<details>
<summary>5. POST - Create Firewall Policy</summary>

**Endpoint:**
```
https://{{base_url}}/api/v2/cmdb/firewall/policy?vdom={{vdom}}
```

**Request Body (JSON):**
```json
{
  "name": "Allow-Web-Traffic",
  "srcintf": [{"name": "port1"}],
  "dstintf": [{"name": "port2"}],
  "srcaddr": [{"name": "all"}],
  "dstaddr": [{"name": "API_Demo_Server"}],
  "service": [{"name": "HTTP"}, {"name": "HTTPS"}],
  "action": "accept",
  "status": "enable"
}
```

</details>

<details>
<summary>6. Common API Endpoints Reference</summary>

**System Monitoring (GET only):**
```
/api/v2/monitor/system/status
/api/v2/monitor/system/interface
/api/v2/monitor/system/resource/usage
/api/v2/monitor/firewall/session
```

**Configuration (GET, POST, PUT, DELETE):**
```
/api/v2/cmdb/system/interface
/api/v2/cmdb/system/global
/api/v2/cmdb/firewall/address
/api/v2/cmdb/firewall/addrgrp
/api/v2/cmdb/firewall/policy
/api/v2/cmdb/firewall/service/custom
/api/v2/cmdb/router/static
```

**Logs (GET only):**
```
/api/v2/log/memory/filter
/api/v2/log/disk/filter
```

</details>

### 🔗 Resources

- [FortiGate REST API Guide](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/940602/rest-api)
- [Postman Download](https://www.postman.com/downloads/)

---

## Video 7: NetBox Installation Using Docker

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=OGQGly7NIFY)

### 📋 Overview

Deploy NetBox with Docker Compose for IPAM and DCIM management.

### 🎯 What You'll Learn

- Deploy NetBox with Docker Compose
- Complete setup and configuration
- Prepare for auto-discovery integration

### 💻 Commands

<details>
<summary>1. Install Docker</summary>

```bash
# Install OpenSSH Server
sudo apt install openssh-server -y

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker + Docker Compose
sudo apt install -y docker.io docker-compose

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group
sudo usermod -aG docker $USER

# Verify installation
docker --version
docker-compose --version
```

</details>

<details>
<summary>2. Download & Configure NetBox</summary>

```bash
# Clone NetBox Docker repository
git clone -b release https://github.com/netbox-community/netbox-docker.git

# Enter directory
cd netbox-docker

# Create override file for port mapping
cp docker-compose.override.yml.example docker-compose.override.yml
```

</details>

<details>
<summary>3. Start NetBox</summary>

```bash
# Pull images
docker-compose pull

# List pulled images
docker images | grep netbox

# Start NetBox stack
docker-compose up -d

# Check status
docker-compose ps

# Verify port listening
ss -tuln | grep :8000

# Test web access
curl -I http://localhost:8000
```

</details>

<details>
<summary>4. Troubleshooting</summary>

```bash
# Restart NetBox container
sudo docker-compose restart netbox

# Stop everything
docker-compose down

# View logs
docker-compose logs
docker-compose logs netbox
docker-compose logs postgres

# Nuclear reset (removes all data!)
docker-compose down -v
docker-compose pull
docker-compose up -d
```

</details>

<details>
<summary>5. Create Superuser</summary>

```bash
docker-compose exec netbox /opt/netbox/netbox/manage.py createsuperuser
```

</details>

### 🔗 Resources

- [NetBox Documentation](https://docs.netbox.dev/)
- [NetBox Docker GitHub](https://github.com/netbox-community/netbox-docker)

---

## Video 8: NetBox Dynamic Inventory - Core Concepts

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=JZ-jDCT8mQY)

### 📋 Overview

Understand the architecture of auto-discovery stack with ORB, DIODE, and NetBox.

### 🎯 What You'll Learn

- Architecture overview of auto-discovery stack
- How ORB, DIODE, and NetBox work together
- Understanding the data flow

### 🏗️ Architecture

```
┌─────────────────┐      SNMP/SSH      ┌──────────────┐
│  Network        │ <──────────────────│  ORB Agent   │
│  Devices        │                     │  (Discovery) │
└─────────────────┘                     └──────┬───────┘
                                               │
                                               │ gRPC (8080)
                                               ↓
                                        ┌──────────────┐
                                        │ DIODE Server │
                                        │ (Ingestion)  │
                                        └──────┬───────┘
                                               │
                                               │ OAuth2
                                               ↓
                                        ┌──────────────┐
                                        │   NetBox     │
                                        │   (DCIM)     │
                                        └──────────────┘
```

### 🔐 OAuth2 Flow

```
ORB Agent → Hydra (OAuth) → DIODE Server → NetBox

Credentials:
- orb-agent uses: "diode-ingest" client
- DIODE Server uses: "diode-to-netbox" client
```

### 🔗 Resources

- [NetBox DIODE Plugin](https://github.com/netboxlabs/diode-netbox-plugin)
- [ORB Agent Documentation](https://github.com/netboxlabs/orb-agent)

---

## Video 9: NetBox Auto-Discovery - Complete Setup Guide

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=DODzEsMTmKQ)

### 📋 Overview

Complete setup guide for NetBox auto-discovery with DIODE and ORB Agent.

### 🎯 What You'll Learn

- Deploy DIODE Server with Docker
- Install and configure NetBox DIODE Plugin
- Setup ORB Agent with OAuth authentication
- Troubleshoot common issues
- Live auto-discovery demonstration

### 🏗️ Architecture

```
┌─────────────────┐      SSH/NAPALM      ┌──────────────┐
│  Network        │ <────────────────────│  ORB Agent   │
│  Devices        │                      │  (Discovery) │
└─────────────────┘                      └──────┬───────┘
                                                │
                                                │ gRPC (8080)
                                                ↓
┌─────────────────────────────────────────────────────────┐
│                    DIODE SERVER                         │
│  ┌─────────┐  ┌───────────┐  ┌────────────────┐       │
│  │ Hydra   │  │ Ingester  │  │  Reconciler    │       │
│  │ (OAuth) │  │ (Receive) │  │ (Push to NB)   │       │
│  └─────────┘  └───────────┘  └────────────────┘       │
└─────────────────────────────────────────────────────────┘
                                                │
                                                │ API + OAuth2
                                                ↓
                                        ┌──────────────┐
                                        │   NetBox     │
                                        │   (DCIM)     │
                                        └──────────────┘
```

### 💻 Commands

<details>
<summary>1. Create Directory Structure</summary>

```bash
# Create main directory with subdirectories
mkdir -p ~/netbox-discovery/diode
mkdir -p ~/netbox-discovery/orb-agent

# Verify structure
ls -la ~/netbox-discovery/
```

</details>

<details>
<summary>2. Deploy DIODE Server</summary>

```bash
# Navigate to DIODE directory
cd ~/netbox-discovery/diode

# Download quickstart script
curl -sSfLo quickstart.sh https://raw.githubusercontent.com/netboxlabs/diode/release/diode-server/docker/scripts/quickstart.sh

# Make executable
chmod +x quickstart.sh

# Run with your NetBox URL
./quickstart.sh http://192.168.1.120:8000

# Save the credentials displayed at the end!
# DIODE_CLIENT_ID:     diode-ingest
# DIODE_CLIENT_SECRET: <your-secret-here>

# View generated OAuth2 credentials
cat oauth2/client/client-credentials.json

# Start DIODE services
docker compose up -d

# Verify all services are running
docker compose ps
```

</details>

<details>
<summary>3. Install NetBox DIODE Plugin</summary>

```bash
# Navigate to NetBox Docker directory
cd ~/netbox-docker

# Verify NetBox is running
docker compose ps

# Enter NetBox container as root
docker compose exec -u root netbox bash

# Inside container: Install pip first
apt update && apt install -y python3-pip

# Install DIODE plugin
pip3 install --target=/opt/netbox/venv/lib/python3.12/site-packages \
  --break-system-packages \
  netboxlabs-diode-netbox-plugin

# Verify installation
ls -la /opt/netbox/venv/lib/python3.12/site-packages/ | grep -i diode

# Test plugin import
/opt/netbox/venv/bin/python3 -c "import netbox_diode_plugin; print('Plugin OK')"

# Exit container
exit
```

</details>

<details>
<summary>4. Commit Container as Custom Image</summary>

```bash
# Create custom Docker image with plugin installed
docker commit netbox-docker-netbox-1 netbox-with-diode:latest

# Verify image was created
docker images | grep netbox-with-diode

# Edit docker-compose.yml to use custom image
nano docker-compose.yml
```

**Update docker-compose.yml:**
```yaml
services:
  netbox:
    # Comment out original image:
    # image: docker.io/netboxcommunity/netbox:${VERSION-v4.1-3.0.2}
    
    # Add custom image:
    image: netbox-with-diode:latest
```

</details>

<details>
<summary>5. Configure DIODE Plugin</summary>

```bash
# Get netbox-to-diode credentials from DIODE server
cd ~/netbox-discovery/diode
cat oauth2/client/client-credentials.json | jq '.[] | select(.client_id == "netbox-to-diode")'

# Edit NetBox plugins configuration
cd ~/netbox-docker
nano configuration/plugins.py
```

**plugins.py content:**
```python
PLUGINS = [
    "netbox_diode_plugin",
]

PLUGINS_CONFIG = {
    "netbox_diode_plugin": {
        "diode_target_override": "grpc://192.168.1.120:8080/diode",
        "diode_client_id": "netbox-to-diode",
        "diode_client_secret": "YOUR_NETBOX_TO_DIODE_SECRET_HERE",
    }
}
```

</details>

<details>
<summary>6. Apply Plugin Configuration</summary>

```bash
# Run database migrations
docker compose exec netbox python3 /opt/netbox/netbox/manage.py migrate

# Restart NetBox services
docker compose restart netbox netbox-worker

# Verify plugin loaded
docker compose logs netbox | grep -i diode

# Check container health
docker compose ps
```

</details>

<details>
<summary>7. Fix Docker Network Connectivity (if needed)</summary>

If NetBox can't reach DIODE (shows error in Plugins → Diode → Settings):

```bash
# Edit DIODE docker-compose.yaml to join NetBox network
cd ~/netbox-discovery/diode
nano docker-compose.yaml
```

**Add network configuration:**
```yaml
networks:
  default:
    name: netbox-docker_default
    external: true
```

```bash
# Restart DIODE
docker compose down
docker compose up -d
```

</details>

<details>
<summary>8. Create ORB Agent Configuration</summary>

```bash
# Navigate to ORB Agent directory
cd ~/netbox-discovery/orb-agent

# Create config.yaml
nano config.yaml
```

**config.yaml content:**
```yaml
orb:
  config_manager:
    active: local
  
  backends:
    device_discovery:
    
    common:
      diode:
        target: grpc://localhost:8080/diode
        client_id: diode-ingest
        client_secret: YOUR_DIODE_INGEST_SECRET_HERE
        agent_name: orb-netbox-discovery
        tls:
          insecure: true
      
      agent_labels:
        environment: lab
        location: networkcoder
  
  policies:
    device_discovery:
      cisco_routers:
        config:
          schedule: "*/5 * * * *"
          defaults:
            site: Main-DC
            role: Router
        scope:
          - driver: ios
            hostname: 192.168.1.101
            username: admin
            password: Cisco123
            optional_args:
              enable_password: Cisco123
          
          - driver: ios
            hostname: 192.168.1.102
            username: admin
            password: Cisco123
            optional_args:
              enable_password: Cisco123
          
          - driver: ios
            hostname: 192.168.1.103
            username: admin
            password: Cisco123
            optional_args:
              enable_password: Cisco123

logs:
  level: info
  format: json
```

</details>

<details>
<summary>9. Create ORB Agent Docker Compose</summary>

```bash
# Create docker-compose.yml for ORB Agent
nano docker-compose.yml
```

**docker-compose.yml content:**
```yaml
services:
  orb-agent:
    image: netboxlabs/orb-agent:latest
    container_name: orb-agent
    restart: unless-stopped
    network_mode: host
    command: ["run", "--config", "/opt/orb/config.yaml"]
    volumes:
      - ./config.yaml:/opt/orb/config.yaml:ro
```

</details>

<details>
<summary>10. Start ORB Agent & Verify Discovery</summary>

```bash
# Start ORB Agent
cd ~/netbox-discovery/orb-agent
docker compose up -d

# Watch discovery logs
docker compose logs -f orb-agent

# Look for successful ingestion messages
docker compose logs -f orb-agent | grep -E "Successful|Getting information|Connected"
```

</details>

<details>
<summary>11. Monitor Data Flow</summary>

```bash
# Check DIODE Ingester (receives data from ORB)
cd ~/netbox-discovery/diode
docker compose logs -f diode-ingester | grep -i success

# Check DIODE Reconciler (pushes to NetBox)
docker compose logs -f diode-reconciler

# Check NetBox for new devices
# Browser: http://192.168.1.120:8000 → Devices → Devices
```

</details>

<details>
<summary>12. Troubleshooting Commands</summary>

```bash
# Check all container status
docker ps -a | grep -E "netbox|diode|orb"

# View ORB Agent logs
cd ~/netbox-discovery/orb-agent
docker compose logs --tail 50 orb-agent

# View DIODE logs
cd ~/netbox-discovery/diode
docker compose logs --tail 50

# Test DIODE connectivity
curl -s http://localhost:8080/health

# Restart all services in order
# 1. NetBox first
cd ~/netbox-docker && docker compose restart

# 2. DIODE second
cd ~/netbox-discovery/diode && docker compose restart

# 3. ORB Agent last
cd ~/netbox-discovery/orb-agent && docker compose restart
```

</details>

### 📁 Final Directory Structure

```
~/netbox-discovery/
├── diode/
│   ├── docker-compose.yaml
│   ├── quickstart.sh
│   ├── nginx/
│   └── oauth2/
│       └── client/
│           └── client-credentials.json
└── orb-agent/
    ├── config.yaml
    └── docker-compose.yml

~/netbox-docker/
├── docker-compose.yml (modified for custom image)
└── configuration/
    └── plugins.py (DIODE plugin config)
```

### 🔗 Resources

- [DIODE GitHub](https://github.com/netboxlabs/diode)
- [NetBox DIODE Plugin](https://github.com/netboxlabs/diode-netbox-plugin)
- [ORB Discovery](https://github.com/netboxlabs/orb-discovery)

---

## Video 10: pyATS + NetBox Integration

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=V_PmWxC2QDA)

### 📋 Overview

Network testing with pyATS and automated inventory sync with NetBox.

### 🎯 What You'll Learn

- Network testing with pyATS
- Automated inventory sync
- Integration workflow

### 💻 Commands

<details>
<summary>1. Install pyATS</summary>

```bash
# Activate virtual environment
source ~/ansible-project/ansible-venv/bin/activate

# Install pyATS
pip install pyats[full]

# Verify installation
pyats version check
```

</details>

<details>
<summary>2. Set Environment Variables</summary>

```bash
# Set NetBox credentials
export NETBOX_URL="http://192.168.1.120:8000"
export NETBOX_USER_TOKEN="your-netbox-api-token"
export DEF_PYATS_USER="admin"
export DEF_PYATS_PASS="Cisco123"

# Verify variables are set
env | grep -E "NETBOX|PYATS"

# Make persistent (add to .bashrc)
echo 'export NETBOX_URL="http://192.168.1.120:8000"' >> ~/.bashrc
echo 'export NETBOX_USER_TOKEN="your-token"' >> ~/.bashrc
echo 'export DEF_PYATS_USER="admin"' >> ~/.bashrc
echo 'export DEF_PYATS_PASS="Cisco123"' >> ~/.bashrc
source ~/.bashrc
```

</details>

<details>
<summary>3. Test NetBox API Connection</summary>

```bash
# Test API endpoint
curl -s -H "Authorization: Token ${NETBOX_USER_TOKEN}" \
    "${NETBOX_URL}/api/" | head -30

# List all devices
curl -s -H "Authorization: Token ${NETBOX_USER_TOKEN}" \
    "${NETBOX_URL}/api/dcim/devices/" | python3 -m json.tool | head -50
```

</details>

<details>
<summary>4. Generate Testbed from NetBox</summary>

```bash
# Generate testbed from NetBox (with site filter)
pyats create testbed netbox \
    --output testbed.yaml \
    --netbox-url=${NETBOX_URL} \
    --user-token=${NETBOX_USER_TOKEN} \
    --def_user='%ENV{DEF_PYATS_USER}' \
    --def_pass='%ENV{DEF_PYATS_PASS}' \
    --url_filter='site=main-dc'

# Validate testbed
pyats validate testbed testbed.yaml
```

</details>

<details>
<summary>5. Run pyATS Commands</summary>

```bash
# Parse show version on a device
genie parse "show version" --testbed-file testbed.yaml --device vIOS-R1

# Parse show ip interface brief
genie parse "show ip interface brief" --testbed-file testbed.yaml --device vIOS-R1

# Learn all features (BGP, OSPF, interfaces, etc.)
genie learn all --testbed-file testbed.yaml --device vIOS-R1
```

</details>

<details>
<summary>6. Manual Testbed File Example</summary>

```yaml
# testbed.yaml
---
testbed:
  name: EVE-NG-Network-Lab
  credentials:
    default:
      username: admin
      password: Cisco123
    enable:
      password: Cisco123

devices:
  R1:
    os: iosxe
    platform: csr1000v
    type: router
    connections:
      cli:
        protocol: ssh
        ip: 192.168.1.11
        port: 22

  R2:
    os: iosxe
    platform: csr1000v
    type: router
    connections:
      cli:
        protocol: ssh
        ip: 192.168.1.12
```

</details>

### 🔗 Resources

- [pyATS Documentation](https://developer.cisco.com/docs/pyats/)
- [pyATS GitHub](https://github.com/CiscoTestAutomation/pyats)

---

## 📚 Additional Resources

| Resource | Link |
|----------|------|
| EVE-NG | [eve-ng.net](https://www.eve-ng.net/) |
| NetBox | [netbox.dev](https://netbox.dev/) |
| Ansible Docs | [docs.ansible.com](https://docs.ansible.com/) |
| Docker Docs | [docs.docker.com](https://docs.docker.com/) |
| Fortinet Docs | [docs.fortinet.com](https://docs.fortinet.com/) |
| pyATS Docs | [developer.cisco.com/pyats](https://developer.cisco.com/docs/pyats/) |

---

## 🤝 Connect With Me

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@NetworkCoder)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/YourProfile)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ **If you find this helpful, please star the repo!** ⭐

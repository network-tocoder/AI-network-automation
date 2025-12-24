<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=45&pause=1000&color=00E5FF&center=true&vCenter=true&width=1500&lines=Network+Automation+Series;Building+Intent-Based+Networks;AI-Powered+Networking+with+MCP" alt="Network Automation Series" />
  </a>
</p>

<p align="center">
  <img src="assets/Series Thumpnail.jpg" alt="Network Coder Banner" width="800">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Network-007ACC?style=for-the-badge" alt="Network">
  <img src="https://img.shields.io/badge/AI-8A2BE2?style=for-the-badge" alt="AI">
  <img src="https://img.shields.io/badge/AI_Agents-141414?style=for-the-badge&logo=openai&logoColor=00F5FF" alt="AI Agents">
  <img src="https://img.shields.io/badge/MCP-FF8C00?style=for-the-badge" alt="MCP">
  <img src="https://img.shields.io/badge/Automation-D1242F?style=for-the-badge" alt="Automation">
  <img src="https://img.shields.io/badge/Virtual_LAB-228B22?style=for-the-badge" alt="Virtual Lab">
</p>

<p align="center">
  <a href="https://youtube.com/@NetworkCoder"><img src="https://img.shields.io/badge/Tutorials-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"></a>
  <a href="https://www.linkedin.com/in/hadeek"><img src="https://img.shields.io/badge/Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://github.com/network-tocoder"><img src="https://img.shields.io/badge/Projects-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
</p>

---

## 🎓 What You'll Learn

This series takes you from zero to hero in network automation. Build a complete virtual lab in EVE-NG, automate firewalls, deploy NetBox for infrastructure management, and integrate everything with modern DevOps tools and AI.

---

## 📺 Video Index

| # | Video | Topic | 🎬 Watch |
|---|-------|-------|----------|
| 1 | [EVE-NG Installation](#video-1-eve-ng-installation--first-virtual-lab) | EVE-NG, Virtual Lab Setup | [▶️ YouTube](https://www.youtube.com/watch?v=ABNOS7GypxA) |
| 2 | [Build Automation Environment](#video-2-build-automation-environment-inside-eve-ng) | Linux, Ansible, VS Code | [▶️ YouTube](https://www.youtube.com/watch?v=NPq7AjCguBY) |
| 3 | [Git Workflow](#video-3-git-workflow-for-network-engineers) | Git, GitHub, Version Control | [▶️ YouTube](https://www.youtube.com/watch?v=vykDi7PFeW0) |
| 4 | [Deploy FortiGate](#video-4-deploy-fortigate-firewall-on-eve-ng) | FortiGate, EVE-NG | [▶️ YouTube](https://www.youtube.com/watch?v=8W9OJAP773s) |
| 5 | [FortiGate Ansible](#video-5-fortigate-firewall-using-ansible) | Ansible, FortiGate, Vault | [▶️ YouTube](https://www.youtube.com/watch?v=3VL-JRIJT8M) |
| 6 | [FortiGate REST API](#video-6-fortigate-automation-using-rest-api) | REST API, Postman | [▶️ YouTube](https://www.youtube.com/watch?v=Eqy4q9SsmtE) |
| 7 | [NetBox Docker](#video-7-netbox-installation-using-docker) | NetBox, Docker | [▶️ YouTube](https://www.youtube.com/watch?v=OGQGly7NIFY) |
| 8 | [NetBox Dynamic Inventory](#video-8-netbox-dynamic-inventory---core-concepts-explained) | DIODE, ORB, Architecture | [▶️ YouTube](https://www.youtube.com/watch?v=JZ-jDCT8mQY) |
| 9 | [NetBox Auto-Discovery](#video-9-netbox-auto-discovery---complete-setup-guide) | DIODE, ORB Agent, OAuth | [▶️ YouTube](https://www.youtube.com/watch?v=DODzEsMTmKQ) |
| 10 | [pyATS + NetBox](#video-10-pyats--netbox-integration) | pyATS, Testing, NetBox | [▶️ YouTube](https://www.youtube.com/watch?v=V_PmWxC2QDA) |
| 11 | [NetBox + MCP Integration](#video-11-netbox--mcp-integration) | MCP, Claude Code, AI | [▶️ YouTube](https://www.youtube.com/watch?v=YOUR_VIDEO_ID) |

---

## 🛠️ Tech Stack

![EVE-NG](https://img.shields.io/badge/EVE--NG-00A98F?style=flat-square&logo=vmware&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=flat-square&logo=ansible&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![NetBox](https://img.shields.io/badge/NetBox-0078D4?style=flat-square&logo=buffer&logoColor=white)
![FortiGate](https://img.shields.io/badge/FortiGate-EE3124?style=flat-square&logo=fortinet&logoColor=white)
![Cisco](https://img.shields.io/badge/Cisco-1BA0D7?style=flat-square&logo=cisco&logoColor=white)

---

## Video 1: EVE-NG Installation & First Virtual Lab

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=ABNOS7GypxA)

### 📋 Overview

Install EVE-NG on VMware Workstation and build your first virtual network topology.

### 🎯 What You'll Learn

- Download and install EVE-NG Community Edition
- Configure VMware Workstation network settings
- Initial EVE-NG configuration
- Add network device images
- Create your first topology

### 💻 Commands

<details>
<summary>1. VMware Network Configuration</summary>

```bash
# Open Virtual Network Editor
# Edit > Virtual Network Editor > Change Settings

# Configure VMnet0 - Bridge to physical adapter
# This allows EVE-NG to use your home network IP range
```

</details>

<details>
<summary>2. EVE-NG VM Settings</summary>

```bash
# Recommended VM Settings:
# - Processors: 2 processors x 2 cores = 4 vCPUs
# - Memory: 8GB minimum (16GB recommended)
# - Hard Disk: 80GB
# - Network Adapter: Bridged (VMnet0)
# - Guest OS: Linux > Ubuntu 64-bit
```

</details>

<details>
<summary>3. EVE-NG Initial Setup</summary>

```bash
# Default credentials after installation
# Username: root
# Password: eve

# Update EVE-NG
apt update && apt upgrade -y

# Fix permissions (run after adding images)
/opt/unetlab/wrappers/unl_wrapper -a fixpermissions
```

</details>

<details>
<summary>4. Key EVE-NG Directories</summary>

```bash
# Lab files location
/opt/unetlab/labs/

# QEMU images (routers, firewalls)
/opt/unetlab/addons/qemu/

# IOL images (Cisco IOS)
/opt/unetlab/addons/iol/bin/

# Docker images
/opt/unetlab/addons/docker/

# Running lab configurations
/opt/unetlab/tmp/
```

</details>

<details>
<summary>5. Add Network Device Images</summary>

```bash
# Upload images via WinSCP/SCP to appropriate directory
# Example: Cisco IOL images
cd /opt/unetlab/addons/iol/bin/

# After uploading, fix permissions
/opt/unetlab/wrappers/unl_wrapper -a fixpermissions

# Verify images
ls -la /opt/unetlab/addons/qemu/
ls -la /opt/unetlab/addons/iol/bin/
```

</details>

### 🔗 Resources

- [EVE-NG Official Website](https://www.eve-ng.net/)
- [EVE-NG Documentation](https://www.eve-ng.net/index.php/documentation/)

---

## Video 2: Build Automation Environment Inside EVE-NG

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=NPq7AjCguBY)

### 📋 Overview

Deploy Linux node in EVE-NG, install Ansible, and integrate VS Code for professional development workflow.

### 🎯 What You'll Learn

- Add Linux node to EVE-NG topology
- Install Python and Ansible
- Configure VS Code Remote SSH
- Set up virtual environment best practices

### 💻 Commands

<details>
<summary>1. Download & Install Ubuntu Cloud Image</summary>

```bash
# On EVE-NG server - download Ubuntu cloud image
mkdir -p /tmp/ubuntu-download
cd /tmp/ubuntu-download

wget https://cloud-images.ubuntu.com/releases/22.04/release/ubuntu-22.04-server-cloudimg-amd64.img

# Rename to EVE-NG format
mv ubuntu-22.04-server-cloudimg-amd64.img virtioa.qcow2

# Move to EVE-NG directory
mkdir -p /opt/unetlab/addons/qemu/linux-ubuntu-22.04
mv virtioa.qcow2 /opt/unetlab/addons/qemu/linux-ubuntu-22.04/

# Fix permissions
/opt/unetlab/wrappers/unl_wrapper -a fixpermissions

# Verify installation
ls -la /opt/unetlab/addons/qemu/linux-ubuntu-22.04/
```

</details>

<details>
<summary>2. Linux Node Initial Setup</summary>

```bash
# Default credentials for EVE-NG Linux images
# Username: root
# Password: eve

# Update system
sudo apt update && sudo apt upgrade -y

# Install essential tools
sudo apt install -y python3 python3-pip python3-venv git curl wget nano vim
```

</details>

<details>
<summary>3. Create Python Virtual Environment</summary>

```bash
# Create virtual environment
python3 -m venv ~/ansible-venv

# Activate virtual environment
source ~/ansible-venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Create activation alias (add to ~/.bashrc)
echo 'alias netdev="source ~/ansible-venv/bin/activate"' >> ~/.bashrc
source ~/.bashrc

# Now you can use 'netdev' to activate
netdev
```

</details>

<details>
<summary>4. Install Ansible</summary>

```bash
# Activate virtual environment first
source ~/ansible-venv/bin/activate

# Install Ansible
pip install ansible

# Install additional useful packages
pip install paramiko netmiko napalm

# Verify installation
ansible --version
python3 --version
pip list
```

</details>

<details>
<summary>5. VS Code Remote SSH Setup</summary>

```bash
# On Linux node - Install OpenSSH Server
sudo apt install openssh-server -y

# Start and enable SSH service
sudo systemctl start ssh
sudo systemctl enable ssh

# Get IP address for VS Code connection
ip addr show
hostname -I

# In VS Code:
# 1. Install "Remote - SSH" extension
# 2. Press F1 > "Remote-SSH: Connect to Host"
# 3. Enter: root@<linux-node-ip>
# 4. Select Linux platform
# 5. Enter password when prompted
```

</details>

<details>
<summary>6. Configure SSH for Root Login (if needed)</summary>

```bash
# Edit SSH config
sudo nano /etc/ssh/sshd_config

# Find and modify these lines:
PermitRootLogin yes
PasswordAuthentication yes

# Restart SSH
sudo systemctl restart ssh
```

</details>

### 📁 Project Structure

```
~/ansible-project/
├── ansible.cfg
├── inventory/
│   └── hosts
├── group_vars/
│   └── all/
│       └── vault.yml
├── playbooks/
│   └── test.yml
└── roles/
```

### 🔗 Resources

- [Ansible Documentation](https://docs.ansible.com/)
- [VS Code Remote SSH](https://code.visualstudio.com/docs/remote/ssh)

---

## Video 3: Git Workflow for Network Engineers

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=vykDi7PFeW0)

### 📋 Overview

Complete Git workflow for version controlling network automation projects with GitHub integration.

### 🎯 What You'll Learn

- Install and configure Git
- Generate SSH keys for GitHub
- Git workflow: clone, branch, commit, push
- VS Code Git integration

### 💻 Commands

<details>
<summary>1. Install & Configure Git</summary>

```bash
# Install Git
sudo apt install git -y

# Configure Git identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Configure default branch name
git config --global init.defaultBranch main

# Enable credential caching
git config --global credential.helper cache

# Verify configuration
git config --list
```

</details>

<details>
<summary>2. Generate SSH Key for GitHub</summary>

```bash
# Generate ED25519 SSH key (recommended)
ssh-keygen -t ed25519 -C "your.email@example.com"

# Or RSA if ED25519 not supported
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# Display public key (copy this to GitHub)
cat ~/.ssh/id_ed25519.pub

# Add to GitHub:
# GitHub > Settings > SSH and GPG keys > New SSH key
# Paste the public key

# Test GitHub connection
ssh -T git@github.com
# Expected: "Hi username! You've successfully authenticated..."
```

</details>

<details>
<summary>3. Initialize Local Repository</summary>

```bash
# Navigate to your project
cd ~/ansible-project

# Initialize Git repository
git init

# Check status
git status

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Ansible project structure"
```

</details>

<details>
<summary>4. Connect to GitHub Repository</summary>

```bash
# Create repository on GitHub first, then:

# Add remote origin (SSH)
git remote add origin git@github.com:username/repo-name.git

# Verify remote
git remote -v

# Push to GitHub
git push -u origin main
```

</details>

<details>
<summary>5. Daily Git Workflow</summary>

```bash
# Pull latest changes before starting work
git pull origin main

# Create feature branch
git checkout -b feature/new-playbook

# Make your changes, then stage them
git add .

# Or stage specific files
git add playbooks/new-playbook.yml

# Commit with descriptive message
git commit -m "Add: FortiGate backup playbook"

# Push feature branch
git push origin feature/new-playbook

# After PR is merged, switch back to main
git checkout main
git pull origin main

# Delete local feature branch
git branch -d feature/new-playbook
```

</details>

<details>
<summary>6. Useful Git Commands</summary>

```bash
# View commit history
git log --oneline

# View changes before staging
git diff

# View staged changes
git diff --staged

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard local changes
git checkout -- filename

# Stash changes temporarily
git stash
git stash pop

# View all branches
git branch -a
```

</details>

<details>
<summary>7. .gitignore for Ansible Projects</summary>

```bash
# Create .gitignore
cat << 'EOF' > .gitignore
# Ansible
*.retry
*.pyc
__pycache__/

# Vault password files
.vault_pass
vault_password_file

# Environment files
.env
*.env

# IDE
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

# Logs
*.log

# Temporary files
*.tmp
*.swp
EOF
```

</details>

### 🔗 Resources

- [GitHub SSH Documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---

## Video 4: Deploy FortiGate Firewall on EVE-NG

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=8W9OJAP773s)

### 📋 Overview

FortiGate installation in virtual lab and network security device configuration.

### 🎯 What You'll Learn

- Add FortiGate image to EVE-NG
- Initial FortiGate configuration
- Enable management access
- Enable REST API

### 💻 Commands

<details>
<summary>1. Add FortiGate Image to EVE-NG</summary>

```bash
# On EVE-NG server
# Create directory for FortiGate
mkdir -p /opt/unetlab/addons/qemu/fortinet-FGT-v7-build0000/

# Upload FortiGate image via WinSCP/SCP
# Rename to virtioa.qcow2

# Fix permissions
/opt/unetlab/wrappers/unl_wrapper -a fixpermissions

# Verify
ls -la /opt/unetlab/addons/qemu/fortinet-FGT-v7-build0000/
```

</details>

<details>
<summary>2. FortiGate Initial CLI Setup</summary>

```bash
# Default credentials
# Username: admin
# Password: (blank - press Enter)

# Show system status
get system status

# Show interface status
get system interface physical
```

</details>

<details>
<summary>3. Configure Management Interface</summary>

```bash
# Configure port1 for management
config system interface
    edit port1
        set mode static
        set ip 192.168.1.99/24
        set allowaccess ping https ssh http fgfm
        set alias "Management"
    next
end

# Verify interface
show system interface port1
```

</details>

<details>
<summary>4. Configure Default Gateway</summary>

```bash
# Set default route
config router static
    edit 1
        set gateway 192.168.1.1
        set device port1
    next
end

# Verify routing
get router info routing-table all
```

</details>

<details>
<summary>5. Enable REST API Access</summary>

```bash
# Create API admin user
config system api-user
    edit "api_admin"
        set accprofile "super_admin"
        set vdom "root"
        config trusthost
            edit 1
                set ipv4-trusthost 192.168.1.0/24
            next
        end
    next
end

# Generate API token
execute api-user generate-key api_admin

# Save the token! It won't be shown again
```

</details>

<details>
<summary>6. Verify Configuration</summary>

```bash
# Test from Linux node
ping 192.168.1.99 -c 4

# Test HTTPS access
curl -k https://192.168.1.99

# Test API access
curl -k -X GET "https://192.168.1.99/api/v2/monitor/system/status" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

</details>

### 🔗 Resources

- [FortiGate Administration Guide](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide)

---

## Video 5: FortiGate Firewall Using Ansible

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=3VL-JRIJT8M)

### 📋 Overview

Install Ansible Collections for FortiGate, configure Ansible Vault, and run automation playbooks.

### 🎯 What You'll Learn

- Install FortiGate Ansible Collection
- Understand Ansible Galaxy and Collections
- Secure credentials with Ansible Vault
- Create and run FortiGate playbooks

### 💻 Commands

<details>
<summary>1. Install FortiGate Ansible Collection</summary>

```bash
# Activate virtual environment
source ~/ansible-venv/bin/activate

# Install FortiOS collection from Ansible Galaxy
ansible-galaxy collection install fortinet.fortios

# Verify installation
ansible-galaxy collection list | grep fortinet

# View collection documentation
ansible-doc -l | grep fortios
```

</details>

<details>
<summary>2. Project Directory Structure</summary>

```bash
# Create project structure
mkdir -p ~/ansible-project/{inventory,group_vars/fortigates,playbooks}
cd ~/ansible-project

# Create structure
tree ~/ansible-project/
# ansible-project/
# ├── ansible.cfg
# ├── inventory/
# │   └── hosts
# ├── group_vars/
# │   ├── all/
# │   │   └── vault.yml
# │   └── fortigates/
# │       └── vars.yml
# └── playbooks/
#     ├── fortigate_info.yml
#     └── fortigate_policy.yml
```

</details>

<details>
<summary>3. Create ansible.cfg</summary>

```bash
cat << 'EOF' > ~/ansible-project/ansible.cfg
[defaults]
inventory = inventory/hosts
host_key_checking = False
timeout = 30
retry_files_enabled = False
gathering = explicit
stdout_callback = yaml

[privilege_escalation]
become = True
become_method = enable
EOF
```

</details>

<details>
<summary>4. Create Inventory File</summary>

```bash
cat << 'EOF' > ~/ansible-project/inventory/hosts
[routers]
vIOS-R1 ansible_host=192.168.1.101
vIOS-R2 ansible_host=192.168.1.102
vIOS-R3 ansible_host=192.168.1.103

[routers:vars]
ansible_network_os=ios
ansible_connection=network_cli
ansible_user=ansible
ansible_password=ansible@123
ansible_become=yes
ansible_become_method=enable

[fortigates]
fw01 ansible_host=192.168.1.99

[fortigates:vars]
ansible_network_os=fortinet.fortios.fortios
ansible_connection=httpapi
ansible_httpapi_use_ssl=yes
ansible_httpapi_validate_certs=no
ansible_httpapi_port=443
EOF
```

</details>

<details>
<summary>5. Setup Ansible Vault for Credentials</summary>

```bash
# Create vault password file
echo "YourSecureVaultPassword" > ~/.vault_pass
chmod 600 ~/.vault_pass

# Create encrypted vault file
ansible-vault create group_vars/fortigates/vault.yml --vault-password-file ~/.vault_pass

# Add these contents:
# vault_fortios_api_token: "your-api-token-here"
# vault_fortios_user: "admin"
# vault_fortios_password: "your-password"

# Edit vault file later
ansible-vault edit group_vars/fortigates/vault.yml --vault-password-file ~/.vault_pass

# View vault file (decrypted)
ansible-vault view group_vars/fortigates/vault.yml --vault-password-file ~/.vault_pass
```

</details>

<details>
<summary>6. Create System Info Playbook</summary>

```yaml
# playbooks/fortigate_info.yml
---
- name: Get FortiGate System Information
  hosts: fortigates
  gather_facts: no
  vars_files:
    - ../group_vars/fortigates/vault.yml
  
  tasks:
    - name: Get system status
      fortinet.fortios.fortios_monitor_fact:
        access_token: "{{ vault_fortios_api_token }}"
        vdom: "root"
        selector: system_status
      register: system_status

    - name: Display system information
      debug:
        var: system_status.meta.results
```

</details>

<details>
<summary>7. Create Firewall Policy Playbook</summary>

```yaml
# playbooks/fortigate_policy.yml
---
- name: Create FortiGate Firewall Policy
  hosts: fortigates
  gather_facts: no
  vars_files:
    - ../group_vars/fortigates/vault.yml
  
  tasks:
    - name: Create address object
      fortinet.fortios.fortios_firewall_address:
        access_token: "{{ vault_fortios_api_token }}"
        vdom: "root"
        state: present
        firewall_address:
          name: "WebServer-Ansible"
          type: "ipmask"
          subnet: "10.0.10.100 255.255.255.255"
          comment: "Created by Ansible"

    - name: Create firewall policy
      fortinet.fortios.fortios_firewall_policy:
        access_token: "{{ vault_fortios_api_token }}"
        vdom: "root"
        state: present
        firewall_policy:
          policyid: 100
          name: "Ansible-Web-Policy"
          srcintf:
            - name: "port1"
          dstintf:
            - name: "port2"
          srcaddr:
            - name: "all"
          dstaddr:
            - name: "WebServer-Ansible"
          service:
            - name: "HTTP"
            - name: "HTTPS"
          action: "accept"
          status: "enable"
          logtraffic: "all"
          comments: "Created by Ansible automation"
```

</details>

<details>
<summary>8. Run Playbooks</summary>

```bash
# Run system info playbook
ansible-playbook playbooks/fortigate_info.yml --vault-password-file ~/.vault_pass

# Run policy playbook
ansible-playbook playbooks/fortigate_policy.yml --vault-password-file ~/.vault_pass

# Run with verbose output
ansible-playbook playbooks/fortigate_info.yml --vault-password-file ~/.vault_pass -vvv
```

</details>

### 🔗 Resources

- [Fortinet Ansible Collection](https://galaxy.ansible.com/fortinet/fortios)
- [FortiOS Ansible Modules Documentation](https://ansible-galaxy-fortios-docs.readthedocs.io/)

---

## Video 6: FortiGate Automation Using REST API

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=Eqy4q9SsmtE)

### 📋 Overview

REST API automation with Postman and VS Code integration for firewall configurations.

### 🎯 What You'll Learn

- Understand FortiGate REST API structure
- Use Postman for API testing
- CRUD operations with curl
- Create, update, and delete firewall objects

### 📁 FortiGate API Structure

```
/api/v2/
├── cmdb/      → Configuration (Create, Read, Update, Delete)
│   ├── firewall/address
│   ├── firewall/policy
│   ├── system/interface
│   └── router/static
├── monitor/   → Status & Monitoring (Read-only)
│   ├── system/status
│   ├── system/interface
│   └── router/ipv4
└── log/       → Logs & Events (Read-only)
```

### 🔧 Postman Environment Variables

| Variable | Value |
|----------|-------|
| `base_url` | `https://192.168.1.99` |
| `api_token` | `your-api-token` |
| `vdom` | `root` |

### 💻 Commands

<details>
<summary>1. Generate API Token on FortiGate</summary>

```bash
# FortiGate CLI: Create API admin user
config system api-user
    edit "api_user"
        set accprofile "super_admin"
        set vdom "root"
        config trusthost
            edit 1
                set ipv4-trusthost 192.168.1.0/24
            next
        end
    next
end

# Generate API token
execute api-user generate-key api_user

# IMPORTANT: Save this token immediately!
# Example: rdQH8FxsrN8y9G5dhHk4gf1qpjen0z
```

</details>

<details>
<summary>2. GET - System Status & Monitoring</summary>

```bash
# Get system status
curl -k -X GET "https://192.168.1.99/api/v2/monitor/system/status?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"

# Get system interfaces
curl -k -X GET "https://192.168.1.99/api/v2/cmdb/system/interface?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"

# Get firewall addresses
curl -k -X GET "https://192.168.1.99/api/v2/cmdb/firewall/address?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"

# Get firewall policies
curl -k -X GET "https://192.168.1.99/api/v2/cmdb/firewall/policy?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"

# Get specific address object
curl -k -X GET "https://192.168.1.99/api/v2/cmdb/firewall/address/WebServer-1?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

</details>

<details>
<summary>3. POST - Create Firewall Address Object</summary>

```bash
curl -k -X POST "https://192.168.1.99/api/v2/cmdb/firewall/address?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "WebServer-API",
    "type": "ipmask",
    "subnet": "10.0.10.100 255.255.255.255",
    "comment": "Created via REST API"
  }'

# Create subnet address
curl -k -X POST "https://192.168.1.99/api/v2/cmdb/firewall/address?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Internal-Network",
    "type": "ipmask",
    "subnet": "10.0.0.0 255.255.255.0",
    "comment": "Internal LAN subnet"
  }'
```

</details>

<details>
<summary>4. POST - Create Firewall Policy</summary>

```bash
curl -k -X POST "https://192.168.1.99/api/v2/cmdb/firewall/policy?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Allow-Web-Traffic-API",
    "srcintf": [{"name": "port1"}],
    "dstintf": [{"name": "port2"}],
    "srcaddr": [{"name": "all"}],
    "dstaddr": [{"name": "WebServer-API"}],
    "service": [{"name": "HTTP"}, {"name": "HTTPS"}],
    "action": "accept",
    "status": "enable",
    "logtraffic": "all",
    "comments": "Created via REST API"
  }'
```

</details>

<details>
<summary>5. PUT - Update Existing Object</summary>

```bash
# Update interface alias
curl -k -X PUT "https://192.168.1.99/api/v2/cmdb/system/interface/port2?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "alias": "LAN-Internal",
    "description": "Updated via API"
  }'

# Update address object
curl -k -X PUT "https://192.168.1.99/api/v2/cmdb/firewall/address/WebServer-API?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "comment": "Updated comment via API"
  }'
```

</details>

<details>
<summary>6. DELETE - Remove Objects</summary>

```bash
# Delete address object
curl -k -X DELETE "https://192.168.1.99/api/v2/cmdb/firewall/address/WebServer-API?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"

# Delete firewall policy by ID
curl -k -X DELETE "https://192.168.1.99/api/v2/cmdb/firewall/policy/100?vdom=root" \
  -H "Authorization: Bearer YOUR_API_TOKEN"
```

</details>

<details>
<summary>7. Common API Endpoints Reference</summary>

```bash
# System Information
/api/v2/monitor/system/status          # System status
/api/v2/monitor/system/interface       # Interface statistics
/api/v2/cmdb/system/global             # Global settings
/api/v2/cmdb/system/interface          # Interface configuration
/api/v2/cmdb/system/dns                # DNS settings

# Firewall
/api/v2/cmdb/firewall/address          # Address objects
/api/v2/cmdb/firewall/addrgrp          # Address groups
/api/v2/cmdb/firewall/policy           # Firewall policies
/api/v2/cmdb/firewall/service/custom   # Custom services

# VPN
/api/v2/cmdb/vpn.ssl.web/portal        # SSL VPN portals
/api/v2/cmdb/vpn.ipsec/phase1-interface # IPsec Phase 1

# Routing
/api/v2/cmdb/router/static             # Static routes
/api/v2/monitor/router/ipv4            # IPv4 routing table

# User & Authentication
/api/v2/cmdb/user/local                # Local users
/api/v2/cmdb/user/group                # User groups
```

</details>

### 🔗 Resources

- [FortiGate REST API Guide](https://docs.fortinet.com/document/fortigate/7.0.0/administration-guide/940602/rest-api)
- [Postman Download](https://www.postman.com/downloads/)

---

## Video 7: NetBox Installation Using Docker

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=OGQGly7NIFY)

### 📋 Overview

Deploy NetBox with Docker Compose for infrastructure documentation and source of truth.

### 🎯 What You'll Learn

- Install Docker and Docker Compose
- Deploy NetBox using docker-compose
- Create superuser account
- Configure auto-start with systemd

### 💻 Commands

<details>
<summary>1. System Update & Prerequisites</summary>

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install OpenSSH (if not installed)
sudo apt install -y openssh-server

# Install prerequisites
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release git
```

</details>

<details>
<summary>2. Install Docker & Docker Compose</summary>

```bash
# Install Docker and Docker Compose
sudo apt install -y docker.io docker-compose

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Verify Docker service
sudo systemctl status docker

# Check versions
docker --version
docker-compose --version
```

</details>

<details>
<summary>3. Configure User Permissions</summary>

```bash
# Add current user to docker group
sudo usermod -aG docker $USER

# Apply group changes (or logout/login)
newgrp docker

# Verify group membership
groups
getent group docker

# Test Docker without sudo
docker ps
```

</details>

<details>
<summary>4. Clone NetBox Docker Repository</summary>

```bash
# Clone NetBox Docker repository
git clone -b release https://github.com/netbox-community/netbox-docker.git
cd netbox-docker

# List files
ls -la

# Create override file for port mapping
cp docker-compose.override.yml.example docker-compose.override.yml

# Edit override file
nano docker-compose.override.yml
```

**docker-compose.override.yml:**
```yaml
services:
  netbox:
    ports:
      - "8000:8080"
```

</details>

<details>
<summary>5. Deploy NetBox</summary>

```bash
# Pull Docker images
docker-compose pull

# Start NetBox stack (background)
docker-compose up -d

# Check container status
docker-compose ps

# View logs
docker-compose logs -f netbox

# Verify port 8000 is listening
ss -tuln | grep :8000

# Test NetBox is responding
curl -I http://localhost:8000
```

</details>

<details>
<summary>6. Create Superuser Account</summary>

```bash
# Create admin user
docker-compose exec netbox /opt/netbox/netbox/manage.py createsuperuser

# Follow prompts:
# Username: admin
# Email: admin@netbox.local
# Password: (your secure password)
```

</details>

<details>
<summary>7. Docker Management Commands</summary>

```bash
# Stop all containers
docker-compose down

# Restart services
docker-compose restart

# Stop specific service
docker-compose stop netbox

# View running containers
docker ps

# View all containers (including stopped)
docker ps -a

# View resource usage
docker stats

# Clean up unused images
docker image prune -a
```

</details>

<details>
<summary>8. Create Systemd Auto-Start Service</summary>

```bash
# Create systemd service file
sudo nano /etc/systemd/system/netbox-docker.service
```

**Service file content:**
```ini
[Unit]
Description=NetBox Docker Compose Application
Requires=docker.service
After=docker.service network-online.target
Wants=network-online.target

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/home/user/netbox-docker
ExecStart=/usr/bin/docker-compose up -d
ExecStop=/usr/bin/docker-compose down
TimeoutStartSec=300
User=user
Group=docker

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable netbox-docker.service
sudo systemctl start netbox-docker.service

# Check service status
sudo systemctl status netbox-docker.service
```

</details>

<details>
<summary>9. Troubleshooting</summary>

```bash
# Check container logs
docker-compose logs -f netbox
docker-compose logs -f netbox-worker

# Restart unhealthy container
docker-compose restart netbox-worker

# Full reset (WARNING: deletes data)
docker-compose down -v
docker-compose up -d

# Check disk space
df -h

# Check memory
free -h
```

</details>

**Access NetBox:** `http://your-ip:8000`

### 🔗 Resources

- [NetBox Documentation](https://docs.netbox.dev/)
- [NetBox Docker GitHub](https://github.com/netbox-community/netbox-docker)

---

## Video 8: NetBox Dynamic Inventory - Core Concepts Explained

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=JZ-jDCT8mQY)

### 📋 Overview

Architecture overview of the auto-discovery stack: ORB, DIODE, and NetBox working together.

### 🎯 What You'll Learn

- Understand the discovery architecture
- Component roles and responsibilities
- Network ports and connectivity
- Data flow from devices to NetBox

### 🏗️ Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                     NETWORK DISCOVERY ARCHITECTURE                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────┐                                                     │
│  │  Network    │  SSH (22) / SNMP (161)                             │
│  │  Devices    │◄────────────────────┐                              │
│  │ (R1,R2,FW)  │                     │                              │
│  └─────────────┘                     │                              │
│                                      │                              │
│                              ┌───────┴───────┐                      │
│                              │   ORB Agent   │                      │
│                              │  (Discovery)  │                      │
│                              │   Container   │                      │
│                              └───────┬───────┘                      │
│                                      │                              │
│                                      │ gRPC (8080)                  │
│                                      ▼                              │
│                              ┌───────────────┐                      │
│                              │ DIODE Server  │                      │
│                              │  (Ingestion)  │                      │
│                              │   Container   │                      │
│                              └───────┬───────┘                      │
│                                      │                              │
│                                      │ HTTP API                     │
│                                      ▼                              │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                         NETBOX                                 │  │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐       │  │
│  │  │   DIODE     │    │   NetBox    │    │   NetBox    │       │  │
│  │  │   Plugin    │───▶│   Core      │───▶│  Database   │       │  │
│  │  │             │    │   (8000)    │    │ (PostgreSQL)│       │  │
│  │  └─────────────┘    └─────────────┘    └─────────────┘       │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 📦 Component Details

| Component | Function | Port | Protocol |
|-----------|----------|------|----------|
| **ORB Agent** | Discovers network devices | - | SSH/SNMP |
| **DIODE Server** | Ingests discovery data | 8080 | gRPC |
| **DIODE Plugin** | Processes data into NetBox | - | Internal |
| **NetBox** | Source of Truth | 8000 | HTTP |
| **OAuth (Hydra)** | Authentication | 4444, 4445 | HTTP |

### 🔄 Data Flow

1. **ORB Agent** connects to network devices via SSH/SNMP
2. **ORB Agent** sends discovered data to DIODE Server via gRPC
3. **DIODE Server** authenticates via OAuth and forwards to DIODE Plugin
4. **DIODE Plugin** processes and creates/updates objects in NetBox
5. **NetBox** becomes the single source of truth

---

## Video 9: NetBox Auto-Discovery - Complete Setup Guide

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=DODzEsMTmKQ)

### 📋 Overview

Complete setup guide for NetBox auto-discovery with DIODE and ORB Agent - clean installation from scratch.

### 🎯 What You'll Learn

- Install Docker Compose v2
- Deploy DIODE Server using quickstart script
- Install NetBox DIODE Plugin manually inside container
- Configure NetBox for DIODE Plugin
- Set up ORB Agent with OAuth credentials
- Run auto-discovery

### 💻 Commands

<details>
<summary>Prerequisites Check</summary>

```bash
# Verify Docker is installed
docker --version

# Verify Docker Compose v2
docker compose version

# Check network connectivity
ping -c 3 google.com
```

</details>

<details>
<summary>SECTION 1: Install Docker Compose v2</summary>

```bash
# Remove old version
sudo apt remove docker-compose -y

# Install Docker Compose v2
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Set permissions
sudo chmod +x /usr/local/bin/docker-compose

# Verify
docker compose version
```

</details>

<details>
<summary>SECTION 2: Create Directory Structure</summary>

```bash
cd ~
mkdir -p netbox-discovery/{diode,orb-agent}
cd netbox-discovery
```

</details>

<details>
<summary>SECTION 3: Install DIODE Server</summary>

```bash
cd ~/netbox-discovery/diode

# Download quickstart script
curl -o diode-quickstart.sh https://raw.githubusercontent.com/netboxlabs/diode/main/diode-quickstart.sh

# Make executable
chmod +x diode-quickstart.sh

# Run script (replace IP with your NetBox IP)
./diode-quickstart.sh --netbox-url http://192.168.1.120:8000

# Wait for completion...

# Verify files created
ls -la

# View OAuth credentials (SAVE THESE!)
cat oauth2/client/client-credentials.json

# Start DIODE
docker compose up -d

# Wait 30 seconds
sleep 30

# Check status
docker compose ps

# Verify all containers are running
```

</details>

<details>
<summary>SECTION 4: Install NetBox DIODE Plugin</summary>

```bash
cd ~/netbox-docker

# Ensure NetBox is running
docker compose ps

# Enter container as root
docker compose exec -u root netbox bash
```

**Inside container:**
```bash
apt update && apt install -y python3-pip

pip3 install --target=/opt/netbox/venv/lib/python3.12/site-packages \
  --break-system-packages \
  netboxlabs-diode-netbox-plugin

# Verify installation
ls -la /opt/netbox/venv/lib/python3.12/site-packages/ | grep -i diode

pip3 list | grep diode

/opt/netbox/venv/bin/python3 -c "import netbox_diode_plugin; print('Plugin OK')"

exit
```

**Back on host:**
```bash
# Commit container as image
docker commit netbox-docker-netbox-1 netbox-with-diode:latest

# Verify image
docker images | grep netbox-with-diode

# Stop NetBox
docker compose down
```

</details>

<details>
<summary>SECTION 5: Configure NetBox for DIODE Plugin</summary>

```bash
cd ~/netbox-docker

# Update docker-compose.yml
code docker-compose.yml
```

**Edit docker-compose.yml:**

Find:
```yaml
netbox: &netbox
  image: docker.io/netboxcommunity/netbox:${VERSION-v4.4-3.4.1}
```

Change to:
```yaml
netbox: &netbox
  image: netbox-with-diode:latest
  # image: docker.io/netboxcommunity/netbox:${VERSION-v4.4-3.4.1}
```

**Save and exit**

```bash
# Configure plugin
code configuration/plugins.py
```

**Get credentials from DIODE:**
```bash
# First, get the netbox-to-diode credentials
cat ~/netbox-discovery/diode/oauth2/client/client-credentials.json | grep -A 3 "netbox-to-diode"
```

**Add to plugins.py:**
```python
PLUGINS = [
    'netbox_diode_plugin',
]

PLUGINS_CONFIG = {
    'netbox_diode_plugin': {
        'diode_target_override': 'grpc://192.168.1.120:8080/diode',
        'diode_client_id': 'netbox-to-diode',
        'diode_client_secret': 'K75KBCHg8E6c6CbhwEumby8ct8cApoI8MpM0uMR4g=',
    }
}
```

**Save and exit**

```bash
# Start NetBox
docker compose up -d

# Wait for healthy
sleep 60

# Check status
docker compose ps

# Run migrations
docker compose exec netbox python3 /opt/netbox/netbox/manage.py migrate

# Restart
docker compose restart netbox netbox-worker

# Check logs
docker compose logs netbox | grep -i plugin
docker compose logs netbox | tail -30
```

</details>

<details>
<summary>SECTION 6: Verify NetBox Plugin</summary>

```bash
# Check plugin loaded
docker compose exec netbox pip list | grep diode

# Check logs
docker compose logs netbox | grep -i diode
```

**Verify in UI:**
- Open: http://192.168.1.120:8000
- Login
- Check for "Diode" in sidebar menu

</details>

<details>
<summary>SECTION 7: Create ORB Agent OAuth Client</summary>

**In NetBox UI:**
1. Navigate to: Diode → Client Credentials
2. Click "Create Client Credentials"
3. Copy the `client_id` and `client_secret`

**Save these for next step!**

</details>

<details>
<summary>SECTION 8: Configure ORB Agent</summary>

```bash
cd ~/netbox-discovery/orb-agent

# Create config file
code config.yaml
```

**Add configuration (replace credentials):**
```yaml
orb:
  config_manager:
    active: local

  backends:
    device_discovery:
    network_discovery:

    common:
      diode:
        target: grpc://localhost:8080/diode
        client_id: orb-discovery-a-2292af1c37b98c20
        client_secret: YOUR_CLIENT_SECRET_HERE
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
          schedule: "*/2 * * * *"
          defaults:
            site: Main-DC
            tenant: NetworkCoder-Lab
            role: Router
            status: active
        scope:
          - driver: ios
            hostname: 192.168.1.101
            username: ansible
            password: ansible@123

          - driver: ios
            hostname: 192.168.1.102
            username: ansible
            password: ansible@123

          - driver: ios
            hostname: 192.168.1.103
            username: ansible
            password: ansible@123

    network_discovery:
      lab_network_scan:
        config:
          schedule: "*/5 * * * *"
        scope:
          targets:
            - 192.168.1.0/24

logs:
  level: info
  format: json
```

**Save and exit**

```bash
# Create docker-compose file
code docker-compose.yml
```

**Add:**
```yaml
services:
  orb-agent:
    image: netboxlabs/orb-agent:latest
    container_name: orb-agent
    volumes:
      - ./config.yaml:/app/config.yaml
    restart: unless-stopped
```

**Save and exit**

```bash
# Start ORB Agent
docker compose up -d

# Wait 10 seconds
sleep 10

# Check logs
docker logs -f orb-agent
```

</details>

<details>
<summary>SECTION 9: Verification Commands</summary>

### Check All Services Status

```bash
# NetBox
cd ~/netbox-docker
docker compose ps

# DIODE
cd ~/netbox-discovery/diode
docker compose ps

# ORB Agent
cd ~/netbox-discovery/orb-agent
docker logs orb-agent --tail 50
```

### Check Data Flow

```bash
# ORB Agent logs (device discovery)
docker logs orb-agent | grep "Successful ingestion"

# DIODE Ingester logs
cd ~/netbox-discovery/diode
docker compose logs diode-ingester | grep -i success

# DIODE Reconciler logs
docker compose logs diode-reconciler | grep -i "applied"

# NetBox logs
cd ~/netbox-docker
docker compose logs netbox | grep -i diode
```

### Check Discovered Devices in NetBox

**Browser:**
- Open: http://192.168.1.120:8000
- Navigate to: Devices → Devices
- Verify routers appear

</details>

<details>
<summary>SECTION 10: Monitoring Commands</summary>

### Real-time Monitoring

```bash
# Watch ORB Agent discover devices
docker logs -f orb-agent

# Watch DIODE ingester receive data
cd ~/netbox-discovery/diode
docker compose logs -f diode-ingester

# Watch DIODE reconciler push to NetBox
docker compose logs -f diode-reconciler

# Watch NetBox receive data
cd ~/netbox-docker
docker compose logs -f netbox
```

### Check Authentication

```bash
# Check Hydra OAuth clients
cd ~/netbox-discovery/diode
docker compose exec hydra hydra list clients --endpoint http://localhost:4445

# Should show:
# - diode-ingest
# - diode-to-netbox
# - netbox-to-diode
# - orb-discovery-a-xxx
```

### Troubleshooting Commands

```bash
# Check if ORB can reach DIODE
docker logs orb-agent | grep -i error
docker logs orb-agent | grep -i "authentication"

# Check if DIODE can reach NetBox
cd ~/netbox-discovery/diode
docker compose logs diode-reconciler | grep -i error
docker compose logs diode-reconciler | grep -i timeout

# Check NetBox plugin errors
cd ~/netbox-docker
docker compose logs netbox | grep -i error
```

</details>

<details>
<summary>Quick Reference - All Service Locations</summary>

```bash
# NetBox
cd ~/netbox-docker

# DIODE Server
cd ~/netbox-discovery/diode

# ORB Agent
cd ~/netbox-discovery/orb-agent
```

</details>

<details>
<summary>Quick Start/Stop Commands</summary>

```bash
# Start all services
cd ~/netbox-docker && docker compose up -d
cd ~/netbox-discovery/diode && docker compose up -d
cd ~/netbox-discovery/orb-agent && docker compose up -d

# Stop all services
cd ~/netbox-docker && docker compose down
cd ~/netbox-discovery/diode && docker compose down
cd ~/netbox-discovery/orb-agent && docker compose down

# Restart all services
cd ~/netbox-docker && docker compose restart
cd ~/netbox-discovery/diode && docker compose restart
cd ~/netbox-discovery/orb-agent && docker compose restart
```

</details>

<details>
<summary>Configuration Files Reference</summary>

### DIODE OAuth Credentials
```bash
cat ~/netbox-discovery/diode/oauth2/client/client-credentials.json
```

### NetBox Plugin Config
```bash
cat ~/netbox-docker/configuration/plugins.py
```

### ORB Agent Config
```bash
cat ~/netbox-discovery/orb-agent/config.yaml
```

### DIODE .env (Reconciler credentials)
```bash
cat ~/netbox-discovery/diode/.env | grep DIODE_TO_NETBOX
```

</details>

<details>
<summary>Health Check Commands</summary>

```bash
# NetBox health
curl http://192.168.1.120:8000/api/ -I

# DIODE health
curl http://192.168.1.120:8080/diode -I

# Check all Docker containers
docker ps -a

# Check Docker resources
docker system df
```

</details>

<details>
<summary>Complete Installation Checklist</summary>

- [ ] Docker Compose v2 installed
- [ ] Directory structure created
- [ ] DIODE server running (7 containers)
- [ ] NetBox plugin installed
- [ ] NetBox using custom image
- [ ] Plugin configured with OAuth credentials
- [ ] NetBox showing DIODE menu
- [ ] ORB Agent OAuth client created in NetBox UI
- [ ] ORB Agent configured with credentials
- [ ] ORB Agent discovering devices
- [ ] DIODE receiving data
- [ ] DIODE pushing to NetBox
- [ ] Devices appearing in NetBox UI

</details>

<details>
<summary>Expected Container Counts</summary>

```bash
# NetBox: 6 containers
# - netbox
# - netbox-worker
# - postgres
# - redis
# - redis-cache
# - (housekeeping - may be absent)

# DIODE: 7 containers
# - diode-ingester
# - diode-reconciler
# - diode-auth
# - hydra
# - postgres
# - redis
# - ingress-nginx

# ORB Agent: 1 container
# - orb-agent

# Total: ~14 containers
docker ps | wc -l
```

</details>

<details>
<summary>Port Reference</summary>

```
8000 - NetBox UI
8080 - DIODE Server (gRPC)
4444 - Hydra public (OAuth tokens)
4445 - Hydra admin (OAuth introspection)
```

</details>

### 🔗 Resources

- [DIODE GitHub](https://github.com/netboxlabs/diode)
- [ORB Agent Documentation](https://github.com/netboxlabs/orb-agent)
- [NetBox DIODE Plugin](https://github.com/netboxlabs/diode-netbox-plugin)

---

## Video 10: pyATS + NetBox Integration

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=V_PmWxC2QDA)

### 📋 Overview

Network testing with pyATS and automated inventory sync with NetBox as source of truth.

### 🎯 What You'll Learn

- Install and configure pyATS
- Create testbed files manually and from NetBox
- Use pyATS for network testing
- Learn, Parse, and Diff workflows

### 💻 Commands

<details>
<summary>1. Install pyATS</summary>

```bash
# Activate virtual environment
source ~/ansible-venv/bin/activate

# Install pyATS full package
pip install "pyats[full]"

# Install pyATS contrib (includes NetBox plugin)
pip install pyats.contrib

# Verify installation
pyats version
genie --help
```

</details>

<details>
<summary>2. Set Environment Variables</summary>

```bash
# Add to ~/.bashrc
cat << 'EOF' >> ~/.bashrc

# NetBox API settings
export NETBOX_URL="http://192.168.1.120:8000"
export NETBOX_USER_TOKEN="your-netbox-api-token"

# Device credentials for pyATS
export DEF_PYATS_USER="ansible"
export DEF_PYATS_PASS="ansible@123"
EOF

# Reload bashrc
source ~/.bashrc

# Verify variables are set
echo "NETBOX_URL: $NETBOX_URL"
echo "NETBOX_USER_TOKEN: $NETBOX_USER_TOKEN"
echo "DEF_PYATS_USER: $DEF_PYATS_USER"
```

</details>

<details>
<summary>3. Create Testbed Manually</summary>

```yaml
# testbed.yaml
---
testbed:
  name: NetworkCoder-Lab

devices:
  vIOS-R1:
    os: ios
    type: router
    platform: iosv
    connections:
      defaults:
        class: unicon.Unicon
      cli:
        protocol: ssh
        ip: 192.168.1.101
        port: 22
    credentials:
      default:
        username: "%ENV{DEF_PYATS_USER}"
        password: "%ENV{DEF_PYATS_PASS}"
      enable:
        password: "%ENV{DEF_PYATS_PASS}"

  vIOS-R2:
    os: ios
    type: router
    platform: iosv
    connections:
      defaults:
        class: unicon.Unicon
      cli:
        protocol: ssh
        ip: 192.168.1.102
        port: 22
    credentials:
      default:
        username: "%ENV{DEF_PYATS_USER}"
        password: "%ENV{DEF_PYATS_PASS}"
      enable:
        password: "%ENV{DEF_PYATS_PASS}"

  vIOS-R3:
    os: ios
    type: router
    platform: iosv
    connections:
      defaults:
        class: unicon.Unicon
      cli:
        protocol: ssh
        ip: 192.168.1.103
        port: 22
    credentials:
      default:
        username: "%ENV{DEF_PYATS_USER}"
        password: "%ENV{DEF_PYATS_PASS}"
      enable:
        password: "%ENV{DEF_PYATS_PASS}"
```

</details>

<details>
<summary>4. Generate Testbed from NetBox</summary>

```bash
# Generate testbed from NetBox
pyats create testbed netbox \
    --output testbed-netbox.yaml \
    --netbox-url=${NETBOX_URL} \
    --user-token=${NETBOX_USER_TOKEN} \
    --def_user='%ENV{DEF_PYATS_USER}' \
    --def_pass='%ENV{DEF_PYATS_PASS}' \
    --url_filter='site=main-dc'

# Note: site filter uses slug (lowercase with hyphens)

# View generated testbed
cat testbed-netbox.yaml
```

</details>

<details>
<summary>5. pyATS Interactive Shell</summary>

```bash
# Start interactive shell
pyats shell --testbed testbed.yaml

# In the shell:
>>> testbed.devices
>>> device = testbed.devices['vIOS-R1']
>>> device.connect()
>>> device.execute('show version')
>>> device.execute('show ip interface brief')
>>> device.disconnect()
>>> exit()
```

</details>

<details>
<summary>6. Parse Command Output</summary>

```bash
# Parse show version
pyats parse "show version" --testbed testbed.yaml --device vIOS-R1

# Parse show ip interface brief
pyats parse "show ip interface brief" --testbed testbed.yaml --device vIOS-R1

# Parse show running-config
pyats parse "show running-config" --testbed testbed.yaml --device vIOS-R1

# Parse across all devices
pyats parse "show version" --testbed testbed.yaml
```

</details>

<details>
<summary>7. Learn Feature State</summary>

```bash
# Learn interface state
pyats learn interface --testbed testbed.yaml --device vIOS-R1 --output interface_state/

# Learn routing state
pyats learn routing --testbed testbed.yaml --device vIOS-R1 --output routing_state/

# Learn OSPF state
pyats learn ospf --testbed testbed.yaml --device vIOS-R1 --output ospf_state/

# Learn all features
pyats learn all --testbed testbed.yaml --output all_features/
```

</details>

<details>
<summary>8. Diff - Compare States</summary>

```bash
# First, learn the "before" state
pyats learn interface --testbed testbed.yaml --output before/

# Make some changes on devices...

# Learn the "after" state
pyats learn interface --testbed testbed.yaml --output after/

# Compare the two states
pyats diff before/ after/
```

</details>

<details>
<summary>9. Run pyATS Job</summary>

```bash
# Create a simple job file (job.py)
cat << 'EOF' > job.py
import os
from pyats.easypy import run

def main(runtime):
    run(testscript='test_script.py', runtime=runtime)
EOF

# Run the job
pyats run job job.py --testbed testbed.yaml
```

</details>

### 🔗 Resources

- [pyATS Documentation](https://developer.cisco.com/docs/pyats/)
- [Genie Documentation](https://developer.cisco.com/docs/genie-docs/)
- [pyATS GitHub](https://github.com/CiscoTestAutomation/pyats)

---

## Video 11: NetBox + MCP Integration

[▶️ Watch on YouTube](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

### 📋 Overview

Connect Claude AI to NetBox using Model Context Protocol (MCP) for natural language infrastructure queries.

### 🎯 What You'll Learn

- What is MCP (Model Context Protocol)
- MCP architecture and connectivity methods
- Install Claude Code CLI on Linux
- Setup NetBox MCP Server
- Query NetBox using natural language

### 🏗️ Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Claude Code    │────▶│   MCP Server    │────▶│     NetBox      │
│  (AI Assistant) │◀────│   (Bridge)      │◀────│     (API)       │
└─────────────────┘     └─────────────────┘     └─────────────────┘
     Natural               Translates            Returns
     Language              to API calls          Data
```

### 💻 Commands

<details>
<summary>1. Install Node.js 20+</summary>

```bash
# Remove old Node.js (if any conflicts)
sudo apt remove -y libnode-dev nodejs npm
sudo apt autoremove -y

# Add NodeSource repository for Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -

# Install Node.js
sudo apt install -y nodejs

# Verify installation
node --version    # Should show v20.x.x
npm --version     # Should show 10.x.x
```

</details>

<details>
<summary>2. Install Claude Code CLI</summary>

```bash
# Install Claude Code globally
sudo npm install -g @anthropic-ai/claude-code

# Verify installation
claude --version

# Check help
claude --help
```

</details>

<details>
<summary>3. Install UV (Python Package Manager)</summary>

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH
source $HOME/.local/bin/env

# Or add to ~/.bashrc permanently
echo 'source $HOME/.local/bin/env' >> ~/.bashrc
source ~/.bashrc

# Verify installation
uv --version
```

</details>

<details>
<summary>4. Clone NetBox MCP Server</summary>

```bash
# Create MCP servers directory
mkdir -p ~/mcp-servers && cd ~/mcp-servers

# Clone official NetBox MCP server
git clone https://github.com/netboxlabs/netbox-mcp-server.git
cd netbox-mcp-server

# Install dependencies with uv
uv sync

# Verify files
ls -la
```

</details>

<details>
<summary>5. Get NetBox API Token</summary>

```bash
# In NetBox UI:
# 1. Login to NetBox: http://192.168.1.120:8000
# 2. Go to: Profile (top right) > API Tokens
# 3. Click "Add a token"
# 4. Description: "claude-mcp"
# 5. Click Create
# 6. Copy the token immediately!
```

</details>

<details>
<summary>6. Test MCP Server Connection</summary>

```bash
# Test MCP server (replace with your NetBox URL and token)
NETBOX_URL=http://192.168.1.120:8000/ \
NETBOX_TOKEN=your-netbox-api-token \
uv run netbox-mcp-server

# If it starts without errors, press Ctrl+C to stop
# You should see no errors - just waiting for connections
```

</details>

<details>
<summary>7. Configure Claude Code with MCP</summary>

```bash
# Add NetBox MCP server to Claude Code
claude mcp add netbox \
  -e NETBOX_URL=http://192.168.1.120:8000/ \
  -e NETBOX_TOKEN=your-netbox-api-token \
  -- uv --directory ~/mcp-servers/netbox-mcp-server run netbox-mcp-server

# Verify MCP server is added
claude mcp list

# Should show:
# netbox: uv --directory /home/user/mcp-servers/netbox-mcp-server run netbox-mcp-server
```

</details>

<details>
<summary>8. Start Claude Code and Query NetBox</summary>

```bash
# Launch Claude Code CLI
claude

# Now you can ask natural language questions:
# "What devices are in my network?"
# "Show me all IP addresses in the 192.168.1.0/24 subnet"
# "What's connected to vIOS-R1?"
# "List all sites in NetBox"
# "Show me devices with role Router"
# "What interfaces does vIOS-R2 have?"
```

</details>

<details>
<summary>9. MCP Server Management</summary>

```bash
# List all MCP servers
claude mcp list

# Remove an MCP server
claude mcp remove netbox

# Re-add with different settings
claude mcp add netbox \
  -e NETBOX_URL=http://new-ip:8000/ \
  -e NETBOX_TOKEN=new-token \
  -- uv --directory ~/mcp-servers/netbox-mcp-server run netbox-mcp-server
```

</details>

### 🔗 Resources

- [NetBox MCP Server](https://github.com/netboxlabs/netbox-mcp-server)
- [Claude Code](https://claude.ai/download)
- [FastMCP Documentation](https://gofastmcp.com)
- [MCP Protocol](https://modelcontextprotocol.io/)

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
| MCP Protocol | [modelcontextprotocol.io](https://modelcontextprotocol.io/) |

---

## 🤝 Connect With Me

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@NetworkCoder)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/hadeek)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ **If you find this helpful, please star the repo!** ⭐

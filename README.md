  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=45&pause=1000&color=00E5FF&center=true&vCenter=true&width=1500&lines=Network+Automation+Series;Building+Intent-Based+Networks;AI-Powered+Networking+with+MCP" alt="Network Automation Series" />
  </a>
</p>

<p align="center">
  <img src="assets/Series Thumpnail.png" alt="Network Coder Banner" width="800">
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
| 8 | [NetBox Dynamic Inventory](#video-8-netbox-dynamic-inventory---core-concepts-explained) | DIODE, ORB, Architecture | [▶️ YouTube](https://www.youtube.com/watch?v=nD9FeG8A44o) |
| 9 | [NetBox Auto-Discovery](#video-9-netbox-auto-discovery---complete-setup-guide) | DIODE, ORB Agent, OAuth | [▶️ YouTube](https://www.youtube.com/watch?v=DODzEsMTmKQ) |
| 10 | [pyATS + NetBox](#video-10-pyats--netbox-integration) | pyATS, Testing, NetBox | [▶️ YouTube](https://www.youtube.com/watch?v=V_PmWxC2QDA) |
| 11 | [MCP Fundamentals](#video-11-mcp-fundamentals---connect-ai-to-network-tools) | MCP Core Concepts, Architecture | [▶️ YouTube](https://www.youtube.com/watch?v=YOUR_VIDEO_ID) |
| 12 | [NetBox + MCP Hands-On](#video-12-netbox--mcp-hands-on-setup) | Claude CLI, NetBox MCP | [▶️ YouTube](https://www.youtube.com/watch?v=1CImPJ6g0ns) |
| 13 | [Custom Device MCP](#video-13-custom-mcp-server---network-device-automation) | Netmiko, SSH, FastMCP | [▶️ YouTube](https://www.youtube.com/watch?v=vtDuhAP-KfQ) |
| 14 | [Ansible Dynamic Inventory](#video-14-ansible-dynamic-inventory-with-netbox) | Ansible, NetBox Plugin | 🔜 Coming Soon |
| 15 | [Ansible MCP Integration](#video-15-ansible-mcp-integration) | Ansible + Claude | 🔜 Coming Soon |
| 16 | [pyATS MCP Server](#video-16-pyats-mcp-server) | pyATS + Claude | 🔜 Coming Soon |

---

## Video 13: Custom MCP Server - Network Device Automation

🔜 **Coming Soon**

### 📋 Overview

Build a custom MCP server using FastMCP and Netmiko to SSH into network devices and run commands via Claude CLI.

### 🎯 What You'll Build

- Custom Python MCP server with FastMCP
- SSH connectivity using Netmiko
- Device inventory from YAML file
- Natural language → Live device commands

### 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│   ┌─────────────────┐    STDIO    ┌────────────────────┐   SSH   ┌───────────┐│
│   │  Claude CLI     │◄──────────►│  device_mcp.py     │◄───────►│  Routers  ││
│   │                 │             │                    │         │           ││
│   │  🤖 "Show       │             │  🐍 Python         │         │ 📡 vIOS-R1││
│   │   version on    │             │  ⚡ FastMCP        │         │ 📡 vIOS-R2││
│   │   R1"           │             │  🔌 Netmiko        │         │ 📡 vIOS-R3││
│   └─────────────────┘             └────────────────────┘         └───────────┘│
│                                            ▲                                   │
│                                       devices.yaml                             │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 💻 Commands

<details>
<summary>1. Project Setup</summary>

```bash
# Navigate to MCP servers directory
cd ~/mcp-servers

# Create project directory
mkdir device-mcp
cd device-mcp

# Initialize Python project with UV
uv init

# Add dependencies
uv add fastmcp netmiko pyyaml

# Verify installation
uv pip list | grep -E "fastmcp|netmiko"
```

</details>

<details>
<summary>2. devices.yaml - Device Inventory</summary>

```yaml
vIOS-R1:
  host: 192.168.1.101
  
vIOS-R2:
  host: 192.168.1.102
  
vIOS-R3:
  host: 192.168.1.103
```

</details>

<details>
<summary>3. device_mcp.py - Custom MCP Server</summary>

```python
#!/usr/bin/env python3
from fastmcp import FastMCP
from netmiko import ConnectHandler
import yaml

# Initialize MCP server
mcp = FastMCP("DeviceCommands")

# Credentials (for demo - use env vars in production)
CREDENTIALS = {
    "username": "ansible",
    "password": "ansible@123",
    "device_type": "cisco_ios"
}

# Load device inventory
def load_inventory(path: str = "devices.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

DEVICES = load_inventory()

@mcp.tool()
def list_devices() -> str:
    """List all available network devices"""
    return "\n".join(DEVICES.keys())

@mcp.tool()
def run_command(device_name: str, command: str) -> str:
    """Run a show command on a network device via SSH.
    
    Args:
        device_name: Name of the device (e.g., vIOS-R1)
        command: The show command to run
    """
    if device_name not in DEVICES:
        return f"Error: Device {device_name} not found"
    
    device_info = DEVICES[device_name]
    connection_params = {
        "host": device_info["host"],
        **CREDENTIALS
    }
    
    try:
        with ConnectHandler(**connection_params) as conn:
            output = conn.send_command(command)
            return output
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_device_info(device_name: str) -> dict:
    """Get connection info for a device"""
    if device_name not in DEVICES:
        return {"error": f"Device {device_name} not found"}
    return DEVICES[device_name]

if __name__ == "__main__":
    mcp.run()
```

</details>

<details>
<summary>4. Test MCP Server Locally</summary>

```bash
# Test the server runs without errors
uv run python device_mcp.py

# You should see FastMCP banner with "DeviceCommands"
# Press Ctrl+C to stop
```

</details>

<details>
<summary>5. Register MCP Server with Claude CLI</summary>

```bash
# Add MCP server to Claude CLI
claude mcp add device-commands -- uv --directory ~/mcp-servers/device-mcp run python device_mcp.py

# Verify registration
claude mcp list

# Expected output shows device-commands as connected
```

</details>

<details>
<summary>6. Launch Claude CLI and Test</summary>

```bash
# Start Claude CLI
claude

# Demo Query 1: List devices
"List the available devices"

# Demo Query 2: Show version
"Show me the IOS version on vIOS-R1"

# Demo Query 3: Interface info
"What interfaces are configured on vIOS-R2?"

# Demo Query 4: Multi-device query
"Show the routing table on all three routers"
```

</details>

<details>
<summary>7. MCP Server Management</summary>

```bash
# List all registered MCP servers
claude mcp list

# Remove an MCP server
claude mcp remove device-commands

# Re-add with different path
claude mcp add device-commands -- uv --directory /new/path run python device_mcp.py

# View MCP logs (for troubleshooting)
# Check ~/.claude/mcp-logs/
```

</details>

### 📦 Example Queries

```bash
# List available devices
"What devices can you connect to?"

# Run show commands
"Show the version on vIOS-R1"
"What interfaces are on vIOS-R2?"
"Show me the routing table on vIOS-R3"

# Multi-device queries
"Show version on all routers"
"Check OSPF neighbors on R1 and R2"
"Compare the interface status across all routers"
```

### 🔗 Resources

- [FastMCP Documentation](https://gofastmcp.com)
- [Netmiko GitHub](https://github.com/ktbyers/netmiko)
- [Claude CLI Download](https://claude.ai/download)

---

## Video 14: Ansible Dynamic Inventory with NetBox

🔜 **Coming Soon**

### 📋 Overview

Configure Ansible to pull device inventory directly from NetBox instead of static files. Add a device in NetBox → automatically available in Ansible. No more manual inventory updates!

### 🎯 What You'll Learn

- Static vs Dynamic Inventory comparison
- Install and configure NetBox Ansible collection
- Create netbox.yml inventory plugin configuration
- Auto-group devices by role, site, platform
- Run playbooks against dynamic inventory
- Troubleshoot common issues (including Redis Docker bug)

### 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│   STATIC INVENTORY (Old Way)              DYNAMIC INVENTORY (New Way)           │
│   ──────────────────────────              ───────────────────────────           │
│                                                                                 │
│   ┌──────────────────────┐                ┌─────────────────┐                  │
│   │ inventory/hosts      │                │     NetBox      │                  │
│   │                      │                │   (Source of    │                  │
│   │ [routers]            │                │     Truth)      │                  │
│   │ R1 ansible_host=...  │                └────────┬────────┘                  │
│   │ R2 ansible_host=...  │                         │                           │
│   │ R3 ansible_host=...  │                         │ API Call                  │
│   └──────────┬───────────┘                         ▼                           │
│              │                            ┌─────────────────┐                  │
│              │                            │  netbox.yml     │                  │
│              ▼                            │  (Plugin Config)│                  │
│   ┌──────────────────────┐                └────────┬────────┘                  │
│   │      Ansible         │                         │                           │
│   │    (Runs Playbook)   │◄────────────────────────┘                           │
│   └──────────────────────┘                                                     │
│                                                                                 │
│   ❌ Manual updates required              ✅ Always current                     │
│   ❌ Config drift risk                    ✅ Single source of truth             │
│   ❌ Duplicate effort                     ✅ Auto-grouping by role/site         │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 🔄 How Dynamic Inventory Works

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│   You run:                                                                      │
│   $ ansible-inventory --graph                                                   │
│                    │                                                            │
│                    ▼                                                            │
│   Ansible reads: inventory/netbox.yml                                           │
│                    │                                                            │
│                    ▼                                                            │
│   Ansible calls: NetBox API automatically                                       │
│   GET http://<netbox>/api/dcim/devices/                                         │
│                    │                                                            │
│                    ▼                                                            │
│   NetBox returns: Device list (JSON)                                            │
│                    │                                                            │
│                    ▼                                                            │
│   Ansible shows: Inventory graph                                                │
│                                                                                 │
│   @all:                                                                         │
│     |--@device_roles_router:                                                    │
│     |  |--vIOS-R1                                                               │
│     |  |--vIOS-R2                                                               │
│     |  |--vIOS-R3                                                               │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Key Concept:** The `netbox.yml` file is NOT the inventory itself - it's the CONFIG that tells Ansible HOW to get inventory from NetBox. Every time you run an Ansible command, it queries NetBox in real-time!

### 📋 Prerequisites

| Requirement | Details |
|-------------|---------|
| NetBox | Running with devices configured |
| Devices | Primary IP assigned, Status = Active |
| Platform | Set for each device |
| API Token | NetBox API token ready |
| Ansible | Installed in virtual environment |

### 💻 Commands

<details>
<summary>1. Verify NetBox is Running</summary>

```bash
# Access NetBox via VS Code Remote SSH or terminal
# Start NetBox Docker if not running
cd ~/netbox-docker
docker-compose up -d

# Test NetBox is accessible
curl -I http://192.168.1.20:8000
# Expected: HTTP/1.1 302 Found

# Test API with your token
curl -s -H "Authorization: Token YOUR_NETBOX_TOKEN" \
  http://192.168.1.20:8000/api/dcim/devices/ | jq

# This returns full device details including:
# - Device names (vIOS-R1, vIOS-R2, vIOS-R3)
# - Primary IPs (192.168.1.101, .102, .103)
# - Device roles, platforms, sites
# - Status (active)
```

</details>

<details>
<summary>2. Prepare Ansible Environment</summary>

```bash
# Activate your ansible virtual environment
netdev

# Navigate to ansible project
cd ~/ansible-project

# Check current project structure
ls -l

# View current static inventory
cat ./inventory/hosts

# Backup static inventory before changes
cp ./inventory/hosts ./inventory/hosts.backup

# Verify backup created
ls -l ./inventory/
# hosts.backup should now exist
```

</details>

<details>
<summary>3. Install NetBox Ansible Collection</summary>

```bash
# Install NetBox collection
ansible-galaxy collection install netbox.netbox

# If already installed, force update to latest
ansible-galaxy collection install netbox.netbox --force

# Verify installation
ansible-galaxy collection list | grep netbox
# Expected: netbox.netbox  3.20.0 (or newer)

# Install required Python dependency
pip install pytz

# Verify pytz installed
pip show pytz
# Expected: Version: 2025.x
```

</details>

<details>
<summary>4. Create NetBox Inventory File</summary>

```bash
# Create the inventory file
code ./inventory/netbox.yml
```

**inventory/netbox.yml:**
```yaml
---
plugin: netbox.netbox.nb_inventory

# NetBox connection settings
api_endpoint: http://192.168.1.20:8000
token: YOUR_NETBOX_TOKEN_HERE
validate_certs: false

# Group devices automatically by these attributes
group_by:
  - device_roles    # Creates groups like: device_roles_router
  - platforms       # Creates groups like: platforms_cisco_ios
  - sites           # Creates groups like: sites_main_dc
  - tags            # Creates groups based on device tags

# Only fetch active devices
query_filters:
  - status: active

# Map NetBox fields to Ansible variables
compose:
  # Extract IP without subnet mask (192.168.1.101/24 → 192.168.1.101)
  ansible_host: primary_ip4.address | split('/') | first
  # Use platform slug for network_os
  ansible_network_os: platform.slug

# Only include devices that have a primary IP assigned
device_query_filters:
  - has_primary_ip: true
```

**Configuration Breakdown:**

| Setting | Purpose |
|---------|---------|
| `plugin` | Tells Ansible to use NetBox inventory plugin |
| `api_endpoint` | Your NetBox server URL |
| `token` | API authentication token |
| `validate_certs` | Skip SSL verification (for lab) |
| `group_by` | Auto-create groups from device attributes |
| `query_filters` | Only fetch devices with status=active |
| `compose` | Transform NetBox data into Ansible variables |
| `device_query_filters` | Only devices with IP addresses |

</details>

<details>
<summary>5. Update ansible.cfg</summary>

```bash
# Edit ansible configuration
code ./ansible.cfg
```

**Change inventory path:**
```ini
[defaults]
# OLD: inventory = inventory/hosts
inventory = inventory/netbox.yml    # NEW: Point to NetBox plugin
host_key_checking = False
timeout = 30
```

</details>

<details>
<summary>6. Create Group Variables</summary>

```bash
# Create group_vars directory if it doesn't exist
mkdir -p group_vars

# Create common variables for all devices
code ./group_vars/all.yml
```

**group_vars/all.yml:**
```yaml
---
# Connection settings for all devices
ansible_user: ansible
ansible_password: ansible@123
ansible_connection: network_cli
ansible_network_os: cisco.ios.ios
ansible_become: yes
ansible_become_method: enable
```

</details>

<details>
<summary>7. Test Dynamic Inventory</summary>

```bash
# View inventory as a tree graph
ansible-inventory --graph

# Expected output:
# @all:
#   |--@ungrouped:
#   |--@sites_main_dc:
#   |  |--vIOS-R1
#   |  |--vIOS-R2
#   |  |--vIOS-R3
#   |--@device_roles_router:
#   |  |--vIOS-R1
#   |  |--vIOS-R2
#   |  |--vIOS-R3
#   |--@platforms_cisco_ios:
#   |  |--vIOS-R1
#   |  |--vIOS-R2
#   |  |--vIOS-R3

# View full inventory as JSON
ansible-inventory --list

# Check variables for specific host
ansible-inventory --host vIOS-R1

# Test connectivity to all devices
ansible all -m ping
```

</details>

<details>
<summary>8. Run Playbook with Dynamic Inventory</summary>

```bash
# Create test playbook
cat << 'EOF' > playbooks/show_version.yml
---
- name: Show Version - Dynamic Inventory Test
  hosts: all
  gather_facts: no

  tasks:
    - name: Run show version
      cisco.ios.ios_command:
        commands:
          - show version
      register: version

    - name: Display output
      debug:
        msg: "{{ version.stdout_lines[0][:5] }}"
EOF

# Run on all devices
ansible-playbook playbooks/show_version.yml

# Run on specific group (by device role)
ansible-playbook playbooks/show_version.yml --limit device_roles_router

# Run on specific site
ansible-playbook playbooks/show_version.yml --limit sites_main_dc

# Run on single device
ansible-playbook playbooks/show_version.yml --limit vIOS-R1
```

</details>

<details>
<summary>9. Demo: Add Device in NetBox → Auto Appears in Ansible</summary>

```bash
# THE MAGIC OF DYNAMIC INVENTORY:

# Step 1: Check current inventory
ansible-inventory --graph
# Shows: vIOS-R1, vIOS-R2, vIOS-R3

# Step 2: Add new device in NetBox UI
# - Go to NetBox → Devices → Add
# - Name: vIOS-R4
# - Assign Primary IP
# - Set Status = Active
# - Set Device Role = Router
# - Set Platform = cisco-ios

# Step 3: Run inventory again (NO FILE CHANGES NEEDED!)
ansible-inventory --graph

# Step 4: New device appears automatically!
# @all:
#   |--@device_roles_router:
#   |  |--vIOS-R1
#   |  |--vIOS-R2
#   |  |--vIOS-R3
#   |  |--vIOS-R4  ← NEW DEVICE!

# Step 5: Run playbook - includes new device
ansible-playbook playbooks/show_version.yml
```

</details>

### ⚠️ Troubleshooting

<details>
<summary>🔴 Redis Connection Error (NetBox Docker 4.4.5+)</summary>

**Error Message:**
```
[WARNING]: Failed to parse inventory/netbox.yml with auto plugin: 
{"error": "Error -3 connecting to redis:6379. Temporary failure in name resolution.", 
"exception": "ConnectionError", "netbox_version": "4.4.5-Docker-3.4.1", "python_version": "3.12.3"}
```

**Root Cause Analysis:**

| Step | What Happens |
|------|--------------|
| 1 | NetBox Docker exposes `/api/status/` endpoint |
| 2 | Ansible plugin calls `self._fetch_information(api_endpoint + "/api/status/")` |
| 3 | Response contains: `"netbox-version": "4.4.5-Docker-3.4.1"` |
| 4 | Plugin detects "Docker" in version string |
| 5 | Plugin tries internal Redis probe to `redis:6379` |
| 6 | Your Ansible host can't resolve "redis" (Docker-internal hostname) |
| 7 | **Plugin CRASHES** before `cache: false` or `group_by` config loads |

**The Fix - Modify NetBox Inventory Plugin:**

```bash
# Find the plugin file location
find ~/.ansible -name "nb_inventory.py" 2>/dev/null

# Typical location:
# ~/.ansible/collections/ansible_collections/netbox/netbox/plugins/inventory/nb_inventory.py

# Edit the file
code ~/.ansible/collections/ansible_collections/netbox/netbox/plugins/inventory/nb_inventory.py
```

**Replace the `_fetch_information` call with a direct mock:**

Find the section that calls `_fetch_information` for status and replace with:

```python
# ORIGINAL CODE (causes Redis error):
# status = self._fetch_information(self.api_endpoint + "/api/status/")

# FIXED CODE (bypasses Redis probe):
status = {
    "netbox-version": "4.4.5",
    "netbox-version-docker": "3.4.1", 
    "python-version": "3.12.3"
}
netbox_api_version = "4.4"
```

**Result After Fix:**

```bash
ansible-inventory --graph
# [WARNING]: Invalid characters were found in group names but not replaced
# [WARNING]: Unable to load the facts cache plugin ().
# @all:
#   |--@ungrouped:
#   |--@sites_main_dc:
#   |  |--vIOS-R1
#   |  |--vIOS-R2
#   |  |--vIOS-R3
#   |--@device_roles_router:
#   |  |--vIOS-R1
#   |  |--vIOS-R2
#   |  |--vIOS-R3
#   |--@platforms_ios_iosv_software...:
#   |  |--vIOS-R1
#   |  |--vIOS-R2
#   |  |--vIOS-R3
```

✅ Bypasses Redis probe entirely  
✅ Sets correct NetBox version (4.4) for schema selection  
✅ `group_by`, `compose`, and all config options work perfectly

</details>

<details>
<summary>🔴 No Hosts Found</summary>

```bash
# Check 1: Devices have Primary IP in NetBox
# Go to NetBox → Devices → Check "Primary IPv4" column

# Check 2: Devices Status = Active
# Go to NetBox → Devices → Check "Status" column

# Check 3: Test API directly
curl -s -H "Authorization: Token YOUR_TOKEN" \
  http://192.168.1.20:8000/api/dcim/devices/ | jq '.results[].name'
```

</details>

<details>
<summary>🔴 Authentication Failed</summary>

```bash
# Verify group_vars/all.yml has correct credentials
cat group_vars/all.yml

# Test SSH manually
ssh ansible@192.168.1.101
# Password: ansible@123
```

</details>

<details>
<summary>🔴 Plugin Not Found</summary>

```bash
# Reinstall NetBox collection
ansible-galaxy collection install netbox.netbox --force

# Verify installation
ansible-galaxy collection list | grep netbox
```

</details>

### 📁 Final Project Structure

```
ansible-project/
├── ansible.cfg                    # Updated: inventory = inventory/netbox.yml
├── inventory/
│   ├── hosts.backup              # Old static inventory (backup)
│   └── netbox.yml                # NEW: Dynamic inventory config
├── group_vars/
│   └── all.yml                   # Connection credentials
├── playbooks/
│   ├── show_version.yml
│   └── backup_configs.yml
└── backups/                      # Created by backup playbook
```

### 🔗 Resources

- [NetBox Ansible Collection](https://galaxy.ansible.com/netbox/netbox)
- [NetBox Inventory Plugin Docs](https://netbox-ansible-collection.readthedocs.io/)
- [NetBox API Documentation](https://demo.netbox.dev/api/docs/)

---

## Video 15: Ansible MCP Integration

🔜 **Coming Soon**

### 📋 Overview

Integrate MCP with Ansible to trigger playbooks via natural language using Claude CLI.

### 🎯 What You'll Build

- MCP server that runs Ansible playbooks
- Natural language → Ansible automation
- Integration with NetBox dynamic inventory

### 🏗️ Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Claude CLI     │────▶│  Ansible MCP    │────▶│     Ansible     │
│                 │     │  Server         │     │   Playbooks     │
│  "Backup all    │     │                 │     │                 │
│   routers"      │◀────│  🐍 FastMCP     │◀────│  backup.yml     │
│                 │     │                 │     │  config.yml     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                │                       │
                                ▼                       ▼
                        ┌─────────────────┐    ┌─────────────────┐
                        │     NetBox      │    │ Network Devices │
                        │ (Dynamic Inv)   │    │  R1, R2, R3     │
                        └─────────────────┘    └─────────────────┘
```

### 📦 Example Queries

```bash
# Run playbooks via natural language
"Run the backup playbook on all routers"
"Deploy the SNMP configuration to FortiGate"
"Execute the interface verification playbook"

# Combine with NetBox dynamic inventory
"Run the backup playbook on all devices in Main-DC site"
"Configure NTP on all routers in the production site"
```

---

## Video 16: pyATS MCP Server

🔜 **Coming Soon**

### 📋 Overview

Build a pyATS MCP server to run network tests and validation via Claude - connecting back to Video 10!

### 🎯 What You'll Build

- MCP server wrapping pyATS/Genie
- Natural language network testing
- Learn/Parse/Diff operations via Claude

### 🏗️ Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Claude CLI     │────▶│   pyATS MCP     │────▶│ Network Devices │
│                 │     │   Server        │     │                 │
│  "Learn OSPF    │     │                 │     │  vIOS-R1        │
│   state on R1"  │◀────│  🐍 FastMCP     │◀────│  vIOS-R2        │
│                 │     │  🧪 pyATS       │     │  vIOS-R3        │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

### 📦 Example Queries

```bash
# pyATS operations via natural language
"Learn the interface state on vIOS-R1"
"Parse show ip route on all routers"
"Compare the OSPF state before and after the change"
"Run a health check on all devices"
```

---

## 📝 Changelog (ADD TO EXISTING)

### v15.0 (2025-01-XX)
- ✅ Video 13: Added Claude CLI commands (`claude mcp add`, `claude mcp list`, `claude`)
- ✅ Video 14: NEW - Ansible Dynamic Inventory with NetBox
  - Complete step-by-step setup guide
  - NetBox inventory plugin configuration
  - Auto-grouping by role, site, platform
  - Redis Docker bug fix documentation
- ✅ Video 15: Renamed from "Ansible MCP Integration" (was Video 14)
- ✅ Video 16: Renamed from "pyATS MCP Server" (was Video 15)
- ✅ Updated video index to 16 videos
- ✅ Added comprehensive troubleshooting for NetBox Docker 4.4.5+

### v14.0 (2025-01-26)
- ✅ Restructured MCP content into multi-video series
- ✅ Video 11: MCP Fundamentals (theory, architecture, concepts)
- ✅ Video 12: NetBox + MCP Hands-On Setup
- ✅ Video 13: Custom MCP Server - Network Device Automation (preview)
- ✅ Added comprehensive MCP architecture diagrams
- ✅ Added FastMCP code examples

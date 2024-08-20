# Custom CheckMK Scripts

This repository contains a collection of my custom CheckMK scripts designed to monitor various services and components within my network.

### Windows Hosts

Windows hosts uses PowerShell scripts (`.ps1` files). Theses should be placed in a directory accessible to your Windows monitoring agents. Typically, these would be located in the **`C:\ProgramData\checkmk\Agent\local`** directory.

### Linux Hosts

Linux hosts uses Python scripts (`.py` files). Theses should be placed in a directory accessible to your Linux monitoring agents.
Typically, these would be located in the **`/usr/lib/check_mk_agent/local`** directory.

**Ensure these scripts are made executable** by running the following command:
```bash
chmod +x /path/to/your/script.py
```

### Activate Windows/Linux scripts

1. Open your CheckMK Webinterface.
2. Click on ```Setup``` in the left side-bar
3. Click on ```Hosts```
4. Click on ```Run service discovery``` on your desired host
5. Check for ```Undecided services``` and add them *(Multiple refreshes may be needed!)*
6. Click on Change in the upper right corner
7. Click on ```Activate in selected sites```


------------


### Script Descriptions

------------

#### check_anti_idle.ps1
**Description:** Checks if a registered anti-idle service is running on Windows clients.
**Use Case:** Ensures critical services remain active.
**How:** PowerShell command: ```Get-ScheduledTask```
**Return code OK:** <span style="color:#1dd1a1">0 - Anti Idle - %serviceName% is running</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - Anti Idle - $serviceName is not running</span>

------------

#### check_bridge.py
**Description:** Monitors a Phillips-Hue Bridge's status.
**Use Case:** Useful in environments where smarthome bridges are used extensively.
**How:** Protocol: ```ICMP```
**Return code OK:** <span style="color:#1dd1a1">0 - Bridge - Bridge is available</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - Bridge - Bridge is not available $httpCode</span>

------------

#### check_cloudflare_updater_task.ps1
**Description:** Checks the status of the Cloudflare updater task on a Windows server.
**Use Case:** Ensures Cloudflare DNS records are updated regularly.
**How:** PowerShell command: ```Get-ScheduledTask```
**Return code OK:** <span style="color:#1dd1a1">0 - DNS Updater - Last run: $runTime</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - DNS Updater - Last run: $runTime</span>

[*Link to Cloudflare DNS Updater*](https://github.com/PIN0L33KZ/CloudflareDnsUpdater "Link to Cloudflare DNS Updater")

------------

#### check_discord.ps1
**Description:** Monitors the status of a Discord client.
**Use Case:** Useful for managing Discord services on a Windows server.
**How:** PowerShell command: ```Get-ScheduledTask```
**Return code OK:** <span style="color:#1dd1a1">0 - Discord - Instance is running</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - Discord - Instance is not running</span>

------------

#### check_doorbell.py
**Description:** Monitors Ring™ doorbell's status.
**Use Case:** Integrates smart home devices with CheckMK.
**How:** Protocol: ```ICMP```
**Return code OK:** <span style="color:#1dd1a1">0 - Doorbell - Doorbell is reachable</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - Doorbell - Doorbell is not reachable</span>

------------

#### check_minecraft_server.py
**Description:** Monitors the status and player count of a Minecraft server.
**Use Case:** Ensures the Minecraft server is up and running without issues.
**How:** API: [api.mcsrvstat.us](https://api.mcsrvstat.us/ "api.mcsrvstat.us") & Protocol: ```HTTPS```
**Return code OK:** <span style="color:#1dd1a1">0 - Minecraft Server - Server is Available, Players online: $playerOn/$maxPlayer</span>
**Return code WARNING:** <span style="color:#ff9f43">1 - Minecraft Server - Could not reach API. HTTP Status Code: $httpCode</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - Minecraft Server - Server is not Available</span>

------------

#### check_pihole_services.py
**Description:** Monitors the Pi-hole services to ensure they are running correctly.
**Use Case:** Vital for networks using Pi-hole for ad blocking and DNS filtering.
**How:** Linux command: ```pgrep```
**Return code OK:** <span style="color:#1dd1a1">0 - $serviceName - $serviceName is running</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - $serviceName - $serviceName is not running</span>

------------

#### check_rpc_server.ps1
**Description:** Monitors Discord-RPC server availability.
**Use Case:** Ensures that the Discord RPC Server is functioning properly.
**How:** PowerShell command: ```Get-ScheduledTask```
**Return code OK:** <span style="color:#1dd1a1">0 - RPC Server - Discord RPC Server is running</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - RPC Server - Discord RPC Server is not running</span>

[*Link to Discord RPC Server*](https://github.com/PIN0L33KZ/DiscordRPCServer "Link to Discord RPC Server")

------------

#### check_smb_disk_space.py
**Description:** Checks available disk space on a SMB share.
**Use Case:** Prevents disk space issues on shared network drives.
**How:** APT-Package: ```smbclient```
**Return code OK:** <span style="color:#1dd1a1">0 - SMB disk space - $usedSpace% used, $freeSpace% free</span>
**Return code WARNING:** <span style="color:#ff9f43">1 - SMB disk space - $usedSpace% used, $freeSpace% free</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - SMB disk space - $usedSpace% used, $freeSpace% free</span>

------------

#### check_smb_share.py
**Description:** Monitors the availability of a SMB share.
**Use Case:** Ensures network shares are accessible.
**How:** APT-Package: ```smbclient```
**Return code OK:** <span style="color:#1dd1a1">0 - SMB share - Share is available</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - SMB share - Share is not available</span>

------------

#### check_ssl_cert.py
**Description:** Checks the validity and expiration of SSL certificates.
**Use Case:** Critical for ensuring SSL certificates are valid and up-to-date.
**How:** Python-Package ```ssl```
**Return code OK:** <span style="color:#1dd1a1">0 - SSL Certificate - $daysRemaining days remaining</span>
**Return code WARNING:** <span style="color:#ff9f43">1 - SSL Certificate - $daysRemaining days remaining</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - SSL Certificate - $daysRemaining days remaining</span>

------------

#### check_statuspage.py
**Description:** Monitors the status page of a nextcloud instance.
**Use Case:** Useful for tracking the health of the nextcloud services.
**How:** Protocol: ```HTTP/S```
**Return code OK:** <span style="color:#1dd1a1">0 - Nextcloud - Nextcloud is running and not in maintenance mode</span>
**Return code WARNING:** <span style="color:#ff9f43">1 - Nextcloud - Nextcloud is in maintenance mode</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - Nextcloud - Nextcloud is unavailable</span>

------------

#### check_unifi_network_console.py
**Description:** Monitors a UniFi Network Console's status.
**Use Case:** Ensures Unifi network devices and consoles are operating correctly.
**How:** Linux command: ```pgrep```
**Return code OK:** <span style="color:#1dd1a1">0 - Unifi Console - Network Console is running</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - Unifi Console - Network Console is not running</span>

------------

#### check_vms.py
**Description:** Monitors Proxmox virtual machines' status.
**Use Case:** Essential for environments heavily reliant on virtualization.
**How:** Linux command: ```qm```
**Return code OK:** <span style="color:#1dd1a1">0 - VM Status - All VMs are running</span>
**Return code WARNING:** <span style="color:#ff9f43">1 - VM Status - No returned no data</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - VM Status - $criticalVms</span>

------------

#### check_vpn_server.py
**Description:** Monitors the availability of a OpenVPN server.
**Use Case:** Ensures VPN services are operational and accessible.
**How:** Linux command: ```pgrep```)
**Return code OK:** <span style="color:#1dd1a1">0 - VPN Server - VPN Server is running</span>
**Return code CRITICAL:** <span style="color:#ee5253">2 - VPN Server - VPN Server is not running</span>

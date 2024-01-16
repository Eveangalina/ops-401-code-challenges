# Script Name: Ops Lab 04: Systems Hardening with CIS Standards
# Author: Eve Campos
# Date of latest revision: 01/12/2024      
# Purpose: This PowerShell script automates the configuration of the required settings in Windows Server 2019.
# Configure: Automates CIS Benchmarks 1.1.5(L1) and 18.4.3(L1)

# Define the path for the security configuration file
$secConfigPath = "C:\SecConfig.cfg"

# Export the current security configuration
secedit /export /cfg $secConfigPath

# Read the content of the security configuration file
$secConfigContent = Get-Content -Path $secConfigPath

# Update 'Password must meet complexity requirements' (Benchmark 1.1.5 L1)
$secConfigContent = $secConfigContent -Replace "PasswordComplexity\s*=\s*0", "PasswordComplexity=1"

# Write the updated configuration back to the file
$secConfigContent | Set-Content -Path $secConfigPath

# Apply the updated security configuration
secedit /configure /db "C:\Windows\security\local.sdb" /cfg $secConfigPath /areas SECURITYPOLICY

# Configure 'Disable SMB v1 server' (Benchmark 18.4.3 L1)
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force

# Cleanup: Remove the temporary security configuration file
Remove-Item -Path $secConfigPath -Force

# Output result to the console
Write-Host "CIS Benchmark configurations for 1.1.5(L1) and 18.4.3(L1) have been applied."

# Resources
# This script was improved with assistance from ChatGPT, OpenAI's language model and a fellow classmate; Juan Cano's help

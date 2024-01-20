# PowerShell Script to Enable Automatic Windows Updates for Windows 10 Pro
# Date: 1/20/24
# Author: Eveangalina Campos
# Purpose: This script configures Windows 10 Pro to automatically download and install updates daily at 10 AM.

# Define the path for the registry key
# This is the location in the registry where Windows Update settings are stored
$autoUpdateKey = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"

# Create the registry key if it doesn't exist
# This checks if the specified registry key exists and creates it if it does not
If (-Not (Test-Path $autoUpdateKey)) {
    New-Item -Path $autoUpdateKey -Force | Out-Null
}

# Set values to enable automatic updates
# AUOptions: 4 = Schedule the install every day
# This setting configures Windows to automatically download and install updates every day
Set-ItemProperty -Path $autoUpdateKey -Name "AUOptions" -Value 4

# ScheduledInstallDay: 0 = Every day
# This setting specifies that updates should be installed every day
Set-ItemProperty -Path $autoUpdateKey -Name "ScheduledInstallDay" -Value 0

# ScheduledInstallTime: 10 = 10 AM (Can be changed to preferred time)
# This setting specifies the time of day when updates are installed, here set to 10 AM
Set-ItemProperty -Path $autoUpdateKey -Name "ScheduledInstallTime" -Value 10

# Restart Windows Update service
# This restarts the Windows Update service to apply the new settings
Restart-Service wuauserv

# Output to indicate completion of the script
Write-Host "Automatic Windows Updates have been enabled for Windows 10 Pro."

# End of Script

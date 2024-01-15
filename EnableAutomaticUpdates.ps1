# PowerShell Script to Enable Automatic Windows Updates for Windows 10 Pro
# Define the path for the registry key
$autoUpdateKey = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"

# Create the registry key if it doesn't exist
If (-Not (Test-Path $autoUpdateKey)) {
    New-Item -Path $autoUpdateKey -Force | Out-Null
}

# Set values to enable automatic updates
# AUOptions: 4 = Schedule the install every day
# ScheduledInstallDay: 0 = Every day
# ScheduledInstallTime: 10 = 10 AM (Can be changed to preferred time)
Set-ItemProperty -Path $autoUpdateKey -Name "AUOptions" -Value 4
Set-ItemProperty -Path $autoUpdateKey -Name "ScheduledInstallDay" -Value 0
Set-ItemProperty -Path $autoUpdateKey -Name "ScheduledInstallTime" -Value 10

# Restart Windows Update service
Restart-Service wuauserv

Write-Host "Automatic Windows Updates have been enabled for Windows 10 Pro."
# This PowerShell script is designed to automate the configuration of automatic Windows updates for Windows 10 Pro machines within the Initrobe organization. By modifying specific registry settings related to Windows Update, the script ensures that updates are scheduled to install every day at 10 AM. This approach helps maintain the security and performance of our Windows 10 Pro systems by promptly applying the latest updates provided by Microsoft. Additionally, the script restarts the Windows Update service to immediately implement the changes. This streamlined process aims to enhance the efficiency of our update management strategy, contributing to a more secure and up-to-date computing environment for Initrobe's operations.

# End of Script

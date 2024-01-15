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

# End of Script

# Resources 
[ChatGPT](https://chat.openai.com/share/691fa0b7-2270-4f15-9105-9c468ebc2d1b)
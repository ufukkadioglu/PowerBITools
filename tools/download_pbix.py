import subprocess


def run_powershell_command(command, success_message="", fail_message="", exit_if_fails=True):
    process = subprocess.Popen(command)
    output, error = process.communicate()

    if process.returncode != 0:
        print(f"Command failed: {' '.join(command)}")
        if fail_message:
            print(fail_message)
        print(f"Output: {output}")
        print(f"Error: {error}")

        if exit_if_fails:
            exit()
    elif success_message:
        print(success_message)


print("Checking if powershell installed")
run_powershell_command(
    command=["pwsh", "--version"],
    fail_message="Script needs powershell to be installed, check for installation: "
                 "https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell")

powerbi_module_install_cmd = ["pwsh", "-c", """
if (!(Get-Module -ListAvailable -Name MicrosoftPowerBIMgmt)) {
    Write-Host "MicrosoftPowerBIMgmt does not exists, will be insatlled:"
    Install-Module -Name MicrosoftPowerBIMgmt
}
else
{
    Write-Host "MicrosoftPowerBIMgmt is already installed, proceeding to download reports"
}
"""]

print("Checking if MicrosoftPowerBIMgmt module is installed")
run_powershell_command(
    command=powerbi_module_install_cmd,
    fail_message="Could not install powershell MicrosoftPowerBIMgmt module")

print("Running pbix downloader")
run_powershell_command(
    command=["pwsh", "download_powerbi_reports.ps1"],
    fail_message="Downloader failed!")

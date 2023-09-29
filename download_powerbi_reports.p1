$workspace_id = Read-Host "Please enter workspace id (it is the uuid on the url when you visit a powerbi workspace)"
$download_folder = Read-Host "Please specify a directory to download reports (DO NOT USE QUOTES, just write the directory)"

Login-PowerBIServiceAccount

New-Item -ItemType Directory -Force -Path $download_folder| Out-Null

$reports = Get-PowerBIReport -WorkspaceId $workspace_id 

echo "Starting to download reports"

foreach ($report in $reports)
{
	echo "# Downloading $($report.Name)"
	Export-PowerBIReport -WorkspaceId $workspace_id -Id $report.Id -OutFile "$($download_folder)/$($report.Name).pbix"
}

echo "Downloads completed"

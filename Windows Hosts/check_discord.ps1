$processName = "Discord" #Check if your Instance's name is Discord indeed.

$process = Get-Process -Name $processName -ErrorAction SilentlyContinue

if ($process) {
    Write-Output "0 ""Discord"" - Instance is running"
} else {
    Write-Output "2 ""Discord"" - Instance is not running"
}

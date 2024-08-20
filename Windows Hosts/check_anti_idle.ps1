$processName = "ANTI_IDLE_SERVICE_NAME" #Change to your anti idle handler.
$process = Get-Process -Name $processName -ErrorAction SilentlyContinue

if ($process) {
    Write-Output "0 ""Anti Idle"" - ANTI_IDLE_SERVICE_NAME is running" #Change to your anti idle handler.
} else {
    Write-Output "2 ""Anti Idle"" - ANTI_IDLE_SERVICE_NAME is not running" #Change to your anti idle handler.
}

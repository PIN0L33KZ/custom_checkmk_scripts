$processName = "Discord RPC Server"
$process = Get-Process -Name $processName -ErrorAction SilentlyContinue

if ($process) {
    Write-Output "1 ""RPC Server"" - Discord RPC Server is running"
} else {
    Write-Output "0 ""RPC Server"" - Discord RPC Server is not running"
}

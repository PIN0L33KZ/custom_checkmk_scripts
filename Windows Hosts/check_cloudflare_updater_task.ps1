$TaskName = "Update Cloudflare DNS"
$Task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue

if ($Task) {
    if ($Task.State -eq 'Disabled') {
        Write-Output "2 ""DNS Updater"" - Task is disabled."
        exit 2
    }
    else {
        try {
            # Attempt to retrieve the task info
            $TaskInfo = Get-ScheduledTaskInfo -TaskName $TaskName -ErrorAction Stop
            $LastRunTime = $TaskInfo.LastRunTime
            $FormattedTime = $LastRunTime.ToString("yyyy-MM-dd HH:mm:ss")
            $CurrentTime = Get-Date
            $TimeDifference = $CurrentTime - $LastRunTime

            if ($LastRunTime -eq $null) {
                Write-Output "1 ""DNS Updater"" - Task has never run."
                exit 1
            }
            elseif ($TimeDifference.TotalHours -le 24) {
                Write-Output "0 ""DNS Updater"" - Last run: $FormattedTime"
                exit 0
            }
            else {
                Write-Output "2 ""DNS Updater"" - Last run: $FormattedTime"
                exit 2
            }
        }
        catch {
            Write-Output "2 ""DNS Updater"" - Error: $_"
            exit 2
        }
    }
}
else {
    Write-Output "2 ""DNS Updater"" - '$TaskName' was not found."
    exit 2
}

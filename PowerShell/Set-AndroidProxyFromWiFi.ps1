
function Set-AndroidProxyFromWiFi {
    param(
        [int]$Port = 8080
    )

    # Get the IPv4 address of the Wi-Fi adapter
    $wifiIP = (ipconfig.exe |
        Select-String -Pattern "Wi-Fi" -Context 0,10 |
        ForEach-Object {
            $_.Context.PostContext |
                Select-String "IPv4 Address.*: ([\d.]+)"
        } |
        ForEach-Object {
            $_.Matches.Groups[1].Value
        }
    )

    if (-not $wifiIP) {
        Write-Error "Could not detect Wi-Fi IPv4 address."
        return
    }

    $proxy = "$wifiIP`:$Port"

    Write-Host "Setting Android proxy to: $proxy" -ForegroundColor Cyan

    adb shell settings delete global http_proxy | Out-Null
    adb shell settings put global http_proxy $proxy

    Write-Host "Done!" -ForegroundColor Green
}

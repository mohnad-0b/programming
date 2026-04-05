function UnSet-AndroidProxy {
    Write-Host "Removing Android proxy settings..." -ForegroundColor Cyan

    adb shell settings delete global http_proxy | Out-Null
    adb shell settings put global http_proxy :0

    Write-Host "Done!" -ForegroundColor Green
}

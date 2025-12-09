function adb-remote-connection {
    Write-Host "Starting ADB remote connection process..." -ForegroundColor Blue
    
    try {
        Write-Host "Step 1: Restarting ADB in TCP mode on port 5555" -ForegroundColor Yellow
        adb tcpip 5555
        if ($LASTEXITCODE -eq 0) {
            Write-Host "   ADB TCP mode restarted successfully" -ForegroundColor Green
        } else {
            Write-Host "   ADB TCP mode command returned error code: $LASTEXITCODE" -ForegroundColor DarkYellow
        }
        
        Write-Host "Step 2: Waiting 5 seconds for device restart" -ForegroundColor Yellow
        Start-Sleep 5
        
        Write-Host "Step 3: Getting device IP address from wlan0 interface" -ForegroundColor Yellow
        $ip = adb shell "ip addr show wlan0 | grep inet | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | head -1"
        Write-Host "   IP found: $ip" -ForegroundColor Gray
        
        if ($ip -and $ip -match '\d+\.\d+\.\d+\.\d+') {
            Write-Host "Step 4: Connecting to device at ${ip}:5555" -ForegroundColor Yellow
            adb connect "${ip}:5555"
            if ($LASTEXITCODE -eq 0) {
                Write-Host "   Successfully connected to device!" -ForegroundColor Green
            } else {
                Write-Host "   Failed to connect to device" -ForegroundColor Red
            }
        } else {
            Write-Host "   No valid IP address found or command failed" -ForegroundColor Red
            throw "IP extraction failed"
        }
    } 
    catch {
        Write-Host "First attempt failed. Error: $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "Starting recovery process..." -ForegroundColor Blue
        
        Write-Host "Step 1: Checking for existing TCP connections on port 5555" -ForegroundColor Yellow
        $device = adb devices -l | Select-String "5555"
        if ($device) {
            $deviceId = ($device -split '\s+')[0]
            Write-Host "   Found device: $deviceId" -ForegroundColor Gray
            Write-Host "   Disconnecting $deviceId" -ForegroundColor Yellow
            adb disconnect $deviceId
            Write-Host "   Disconnected" -ForegroundColor Green
        } else {
            Write-Host "   No existing TCP connection found" -ForegroundColor Gray
        }
        
        Write-Host "Step 2: Restarting ADB in TCP mode again" -ForegroundColor Yellow
        adb tcpip 5555
        Write-Host "Step 3: Waiting 5 seconds" -ForegroundColor Yellow
        Start-Sleep 5
        
        Write-Host "Step 4: Getting device IP address again" -ForegroundColor Yellow
        $ip = adb shell "ip addr show wlan0 | grep inet | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | head -1"
        Write-Host "   IP found: $ip" -ForegroundColor Gray
        
        if ($ip -and $ip -match '\d+\.\d+\.\d+\.\d+') {
            Write-Host "Step 5: Connecting to device at ${ip}:5555" -ForegroundColor Yellow
            $result = adb connect "${ip}:5555"
            Write-Host "   Connection result: $result" -ForegroundColor Gray
            
            if ($LASTEXITCODE -eq 0) {
                Write-Host "   Successfully connected to device on second attempt!" -ForegroundColor Green
            } else {
                Write-Host "   Failed to connect to device" -ForegroundColor Red
                Write-Error "Failed to get device IP address or connect to device"
            }
        } 
        else {
            Write-Host "   No valid IP address found" -ForegroundColor Red
            Write-Error "Failed to get device IP address"
        }
    }
    
    Write-Host "Final device list:" -ForegroundColor Blue
    adb devices -l
}

try {
    try {
        oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\microverse-power.omp.json" | Invoke-Expression
    } catch {
        Write-Warning "Failed to initialize Oh My Posh: $_"
    }
    try {
        Import-Module -Name Terminal-Icons -ErrorAction Stop
    } catch {
       Write-Warning "Failed to load Terminal Icons module: $_"
      #Fix:# Install-Module -Name Terminal-Icons -Repository PSGallery -Scope CurrentUser
    }

    try {
        Set-PSReadLineOption -PredictionSource History
        Set-PSReadLineOption -PredictionViewStyle ListView
        Set-PSReadLineOption -EditMode Windows
    } catch {
        Write-Warning "Failed to configure PSReadLine: $_"
    }

} catch {
    Write-Warning "An error occurred while loading profile: $_"
} finally {
    [Console]::OutputEncoding = $previousOutputEncoding
}

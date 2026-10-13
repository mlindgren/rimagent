# Windows counterpart of start.sh: make sure RimWorld is running with RimBridge, then start the agent + dashboard.
#   powershell -ExecutionPolicy Bypass -File script\start.ps1              # play forever (episodes back to back)
#   powershell -ExecutionPolicy Bypass -File script\start.ps1 --max-days 3 # extra args go to `rimagent play`
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
$env:PYTHONUNBUFFERED = '1'
$env:PYTHONUTF8 = '1'   # skills/brain files are UTF-8; Windows' default code page is not

function Test-Bridge {
    try { Invoke-WebRequest -UseBasicParsing -TimeoutSec 2 'http://127.0.0.1:8765/health' | Out-Null; return $true } catch { return $false }
}

if (-not (Test-Bridge)) {
    if (-not (Get-Process -Name 'RimWorldWin64' -ErrorAction SilentlyContinue)) {
        Write-Host 'launching RimWorld via Steam...'
        Start-Process 'steam://rungameid/294100'
    }
    Write-Host 'waiting for RimBridge on :8765...'
    for ($i = 0; $i -lt 120; $i++) {
        Start-Sleep -Seconds 3
        if (Test-Bridge) { break }
    }
}

New-Item -ItemType Directory -Force runs | Out-Null
$log = "runs\play-$(Get-Date -Format 'yyyyMMdd-HHmmss').log"
Write-Host "agent log: $log ; dashboard: http://127.0.0.1:8770"
Set-Location agent
uv run rimagent play -v @args 2>&1 | Tee-Object -FilePath "..\$log"

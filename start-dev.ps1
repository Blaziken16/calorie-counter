$container = "calorie-counter-db"

$running = docker ps --filter "name=^/$container$" --format "{{.Names}}"

if ($running -ne $container) {
    Write-Host "Starting Postgres container..."
    docker start $container
}
else {
    Write-Host "Postgres container is already running."
}

Set-Location "$PSScriptRoot\backend"

Write-Host "Starting FastAPI..."
uv run fastapi dev`
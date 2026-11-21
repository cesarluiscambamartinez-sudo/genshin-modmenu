# Builds the C# DX11 overlay host.
$ErrorActionPreference = "Stop"
Push-Location "$PSScriptRoot/.."
try {
    dotnet build src/ModMenu.Overlay.Host/ModMenu.Overlay.Host.csproj -c Release
} finally {
    Pop-Location
}
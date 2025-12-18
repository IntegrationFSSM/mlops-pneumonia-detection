# Script de test rapide - Lance uniquement Airflow et MLflow (sans build complet)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Test Rapide - Infrastructure MLOps" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "ATTENTION: Ce script utilise les images pre-construites" -ForegroundColor Yellow
Write-Host "Pour un build complet avec PyTorch, utilisez start.ps1" -ForegroundColor Yellow
Write-Host ""

# Vérifier Docker
Write-Host "[1/3] Verification de Docker..." -ForegroundColor Yellow
try {
    docker --version | Out-Null
    Write-Host "      Docker OK" -ForegroundColor Green
} catch {
    Write-Host "      ERREUR: Docker requis" -ForegroundColor Red
    exit 1
}

# Utiliser docker-compose-light.yaml si disponible, sinon le normal
$composeFile = "docker-compose.yaml"
if (Test-Path "docker-compose-light.yaml") {
    $composeFile = "docker-compose-light.yaml"
    Write-Host "      Utilisation de la config legere" -ForegroundColor Cyan
}

# Initialisation rapide
Write-Host ""
Write-Host "[2/3] Initialisation d'Airflow..." -ForegroundColor Yellow
docker-compose -f $composeFile up airflow-init

# Démarrage
Write-Host ""
Write-Host "[3/3] Demarrage des services..." -ForegroundColor Yellow
docker-compose -f $composeFile up -d

Write-Host ""
Write-Host "Attente de 20 secondes..." -ForegroundColor Yellow
Start-Sleep -Seconds 20

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "SERVICES DEMARRES!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Acces aux interfaces:" -ForegroundColor Cyan
Write-Host "  - Airflow: http://localhost:8080 (airflow/airflow)" -ForegroundColor White
Write-Host "  - MLflow:  http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "Pour arreter: docker-compose down" -ForegroundColor Yellow
Write-Host ""

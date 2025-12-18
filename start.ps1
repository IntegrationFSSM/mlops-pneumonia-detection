# Script de demarrage rapide pour le projet MLOps (Windows PowerShell)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Demarrage du Projet MLOps" -ForegroundColor Cyan
Write-Host "Detection de Pneumonie sur X-Ray" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Verifier que Docker est en cours d'execution
Write-Host ""
Write-Host "[1/5] Verification des prerequis..." -ForegroundColor Yellow
try {
    docker --version | Out-Null
    Write-Host "      Docker detecte - OK" -ForegroundColor Green
} catch {
    Write-Host "      ERREUR: Docker n'est pas installe ou n'est pas en cours d'execution" -ForegroundColor Red
    exit 1
}

# Construction de l'image
Write-Host ""
Write-Host "[2/5] Construction de l'image Docker personnalisee..." -ForegroundColor Yellow
docker-compose build

# Initialisation d'Airflow
Write-Host ""
Write-Host "[3/5] Initialisation d'Airflow..." -ForegroundColor Yellow
docker-compose up airflow-init

# Demarrage des services
Write-Host ""
Write-Host "[4/5] Demarrage de tous les services..." -ForegroundColor Yellow
docker-compose up -d

# Attendre que les services soient prets
Write-Host ""
Write-Host "[5/5] Attente du demarrage des services (30 secondes)..." -ForegroundColor Yellow
Start-Sleep -Seconds 30

# Verifier le statut
Write-Host ""
Write-Host "Statut des services:" -ForegroundColor Yellow
docker-compose ps

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "DEMARRAGE TERMINE AVEC SUCCES!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Acces aux interfaces:" -ForegroundColor Cyan
Write-Host "  - Airflow UI: http://localhost:8080" -ForegroundColor White
Write-Host "    Username: airflow" -ForegroundColor White
Write-Host "    Password: airflow" -ForegroundColor White
Write-Host ""
Write-Host "  - MLflow UI:  http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "Commandes utiles:" -ForegroundColor Cyan
Write-Host "  - Voir les logs:        docker-compose logs -f" -ForegroundColor White
Write-Host "  - Arreter les services: docker-compose down" -ForegroundColor White
Write-Host "  - Redemarrer:           docker-compose restart" -ForegroundColor White
Write-Host ""

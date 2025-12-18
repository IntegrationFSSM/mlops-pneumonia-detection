# Script de démarrage rapide pour le projet MLOps (Windows PowerShell)

Write-Host "🚀 Démarrage du Projet MLOps - Détection de Pneumonie" -ForegroundColor Cyan
Write-Host "======================================================" -ForegroundColor Cyan

# Vérifier que Docker est en cours d'exécution
Write-Host ""
Write-Host "📋 Vérification des prérequis..." -ForegroundColor Yellow
try {
    docker --version | Out-Null
    Write-Host "✅ Docker détecté" -ForegroundColor Green
} catch {
    Write-Host "❌ Docker n'est pas installé ou n'est pas en cours d'exécution" -ForegroundColor Red
    exit 1
}

# Construction de l'image
Write-Host ""
Write-Host "🔨 Construction de l'image Docker personnalisée..." -ForegroundColor Yellow
docker-compose build

# Initialisation d'Airflow
Write-Host ""
Write-Host "⚙️  Initialisation d'Airflow..." -ForegroundColor Yellow
docker-compose up airflow-init

# Démarrage des services
Write-Host ""
Write-Host "🎬 Démarrage de tous les services..." -ForegroundColor Yellow
docker-compose up -d

# Attendre que les services soient prêts
Write-Host ""
Write-Host "⏳ Attente du démarrage des services (30 secondes)..." -ForegroundColor Yellow
Start-Sleep -Seconds 30

# Vérifier le statut
Write-Host ""
Write-Host "📊 Statut des services:" -ForegroundColor Yellow
docker-compose ps

Write-Host ""
Write-Host "✅ Démarrage terminé!" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Accès aux interfaces:" -ForegroundColor Cyan
Write-Host "   - Airflow UI: http://localhost:8080 (airflow/airflow)" -ForegroundColor White
Write-Host "   - MLflow UI:  http://localhost:5000" -ForegroundColor White
Write-Host ""
Write-Host "💡 Commandes utiles:" -ForegroundColor Cyan
Write-Host "   - Voir les logs:        docker-compose logs -f" -ForegroundColor White
Write-Host "   - Arrêter les services: docker-compose down" -ForegroundColor White
Write-Host "   - Redémarrer:           docker-compose restart" -ForegroundColor White
Write-Host ""

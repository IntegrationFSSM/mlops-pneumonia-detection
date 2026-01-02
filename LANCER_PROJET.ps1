# 🚀 SCRIPT COMPLET - AIRFLOW + MLFLOW

# Aller dans le projet
cd C:\Users\yassine\Desktop\PROJET_MLOPS

# Tout arrêter et nettoyer
Write-Host "🧹 Nettoyage..." -ForegroundColor Yellow
docker-compose down -v
docker system prune -f

# Démarrer TOUS les services (Airflow + MLflow)
Write-Host "🚀 Démarrage Airflow + MLflow..." -ForegroundColor Green
docker-compose up -d

# Attendre que tout démarre
Write-Host "⏳ Attente 2 minutes pour que tout démarre..." -ForegroundColor Yellow
Start-Sleep -Seconds 120

# Vérifier
Write-Host "📊 Vérification des services..." -ForegroundColor Cyan
docker-compose ps

# Copier les fichiers DAG
Write-Host "📁 Copie des fichiers DAG..." -ForegroundColor Cyan
docker cp "C:\Users\yassine\Desktop\PROJET_MLOPS\dags\train_model.py" projet_mlops-airflow-scheduler-1:/opt/airflow/dags/train_model.py
docker cp "C:\Users\yassine\Desktop\PROJET_MLOPS\dags\pneumonia_pipeline_fast.py" projet_mlops-airflow-scheduler-1:/opt/airflow/dags/pneumonia_pipeline_fast.py
docker cp "C:\Users\yassine\Desktop\PROJET_MLOPS\dags\pneumonia_pipeline_fast.py" projet_mlops-airflow-webserver-1:/opt/airflow/dags/pneumonia_pipeline_fast.py

# Redémarrer Airflow pour détecter les DAGs
Write-Host "🔄 Redémarrage Airflow..." -ForegroundColor Cyan
docker-compose restart airflow-scheduler airflow-webserver

# Attendre
Write-Host "⏳ Attente 30 secondes..." -ForegroundColor Yellow
Start-Sleep -Seconds 30

# Lancer l'entraînement
Write-Host "🏋️ Lancement entraînement RAPIDE..." -ForegroundColor Green
docker-compose exec airflow-scheduler bash -c "cd /opt/airflow/dags && python -c 'from train_model import train; train(epochs=1, batch_size=512, sample_fraction=0.01)'"

# Message final
Write-Host ""
Write-Host "✅ ✅ ✅ TERMINÉ ! ✅ ✅ ✅" -ForegroundColor Green
Write-Host ""
Write-Host "📊 OUVREZ CES 2 INTERFACES :" -ForegroundColor Yellow
Write-Host ""
Write-Host "1️⃣  AIRFLOW : le" -ForegroundColor Cyan
Write-Host "    Login: airflow" -ForegroundColor White
Write-Host "    Password: airflow" -ForegroundColor White
Write-Host ""
Write-Host "2️⃣  MLFLOW : http://localhost:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "MONTREZ AU PROF :" -ForegroundColor Yellow
Write-Host "  ✅ Airflow : Le DAG 'pneumonia_pipeline_fast'" -ForegroundColor White
Write-Host "  ✅ MLflow : L'experiment 'pneumonia_detection'" -ForegroundColor White
Write-Host "  ✅ Les métriques d'entraînement" -ForegroundColor White
Write-Host ""
Write-Host "BON COURAGE ! 🍀" -ForegroundColor Green

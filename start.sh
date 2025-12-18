#!/bin/bash
# Script de démarrage rapide pour le projet MLOps

echo "🚀 Démarrage du Projet MLOps - Détection de Pneumonie"
echo "======================================================"

# Vérifier que Docker est en cours d'exécution
echo ""
echo "📋 Vérification des prérequis..."
docker --version > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "❌ Docker n'est pas installé ou n'est pas en cours d'exécution"
    exit 1
fi
echo "✅ Docker détecté"

# Construction de l'image
echo ""
echo "🔨 Construction de l'image Docker personnalisée..."
docker-compose build

# Initialisation d'Airflow
echo ""
echo "⚙️  Initialisation d'Airflow..."
docker-compose up airflow-init

# Démarrage des services
echo ""
echo "🎬 Démarrage de tous les services..."
docker-compose up -d

# Attendre que les services soient prêts
echo ""
echo "⏳ Attente du démarrage des services (30 secondes)..."
sleep 30

# Vérifier le statut
echo ""
echo "📊 Statut des services:"
docker-compose ps

echo ""
echo "✅ Démarrage terminé!"
echo ""
echo "🌐 Accès aux interfaces:"
echo "   - Airflow UI: http://localhost:8080 (airflow/airflow)"
echo "   - MLflow UI:  http://localhost:5000"
echo ""
echo "💡 Commandes utiles:"
echo "   - Voir les logs:        docker-compose logs -f"
echo "   - Arrêter les services: docker-compose down"
echo "   - Redémarrer:           docker-compose restart"
echo ""

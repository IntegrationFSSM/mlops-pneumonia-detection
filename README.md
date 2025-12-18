# 🫁 Projet MLOps - Détection de Pneumonie sur X-Ray

Projet MLOps complet pour la détection automatique de pneumonie sur des radiographies thoraciques, utilisant PyTorch, MLflow, Airflow et DVC.

## 🏗️ Architecture

- **Orchestration** : Apache Airflow
- **Tracking ML** : MLflow
- **Versioning des données** : DVC
- **Framework IA** : PyTorch
- **Infrastructure** : Docker Compose

## 📁 Structure du Projet

```
PROJET_MLOPS/
├── dags/                    # DAGs Airflow
│   ├── data/               # Données (géré par DVC)
│   ├── train_model.py      # Script d'entraînement
│   └── pipeline.py         # DAG principal
├── logs/                    # Logs Airflow
├── plugins/                 # Plugins Airflow
├── config/                  # Configurations
├── storage/                 # Stockage distant DVC (local)
├── docker-compose.yaml      # Configuration Docker
├── Dockerfile              # Image personnalisée
└── requirements.txt        # Dépendances Python
```

## 🚀 Démarrage Rapide

### 1. Prérequis

- Docker Desktop installé et démarré
- Git installé
- Au moins 8 GB de RAM disponible

### 2. Lancement de l'infrastructure

```bash
# Construire l'image personnalisée
docker-compose build

# Initialiser Airflow
docker-compose up airflow-init

# Démarrer tous les services
docker-compose up -d
```

### 3. Accès aux interfaces

- **Airflow UI** : http://localhost:8080
  - Username: `airflow`
  - Password: `airflow`
  
- **MLflow UI** : http://localhost:5000

## 📊 Pipeline MLOps

Le pipeline automatisé comprend :

1. **Récupération des données** : `dvc pull` pour obtenir la dernière version
2. **Entraînement** : Modèle CNN (ResNet18) avec PyTorch
3. **Tracking** : Métriques et modèles enregistrés dans MLflow
4. **Validation** : Promotion automatique si accuracy > 80%

## 🔧 Commandes Utiles

```bash
# Voir les logs
docker-compose logs -f

# Arrêter les services
docker-compose down

# Arrêter et supprimer les volumes
docker-compose down -v

# Reconstruire après modification
docker-compose up -d --build
```

## 📦 Gestion des Données avec DVC

```bash
# Initialiser DVC (première fois)
dvc init

# Ajouter des données
dvc add dags/data/chest_xray

# Configurer le stockage distant
dvc remote add -d local_storage ./storage

# Pousser les données
dvc push

# Récupérer les données
dvc pull
```

## 🧠 Modèle IA

- **Architecture** : ResNet18 (pré-entraîné)
- **Classes** : NORMAL / PNEUMONIA
- **Framework** : PyTorch
- **Métriques** : Accuracy, Loss, Precision, Recall

## 📈 Suivi des Expériences

Toutes les expériences sont trackées dans MLflow :
- Hyperparamètres (learning rate, batch size, epochs)
- Métriques (accuracy, loss)
- Modèles (.pth)
- Artefacts (graphiques, matrices de confusion)

## 🔄 Workflow Git

```bash
# Initialiser le repo
git init
git add .
git commit -m "Initial MLOps Pipeline"

# Pousser vers GitHub
git remote add origin <votre-repo>
git push -u origin main
```

## 🐛 Troubleshooting

### Problème de permissions
```bash
# Sur Windows, définir AIRFLOW_UID
echo AIRFLOW_UID=50000 > .env
```

### Airflow ne voit pas les DAGs
- Vérifier que les fichiers sont dans `./dags/`
- Redémarrer le scheduler : `docker-compose restart airflow-scheduler`

### MLflow inaccessible
- Vérifier que le service est démarré : `docker-compose ps`
- Vérifier les logs : `docker-compose logs mlflow`

## 📝 Licence

Projet éducatif - MLOps Pipeline

## 👥 Auteur

Yassine - Projet MLOps X-Ray Detection

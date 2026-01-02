# 🚀 GUIDE COMPLET : Projet MLOps dans GitHub Codespaces
## Continuous Retraining Pipeline - De A à Z

---

## 📋 PARTIE 1 : PRÉPARATION (Sur votre PC Windows)

### Étape 1.1 : Créer le repository GitHub

1. Allez sur https://github.com
2. Cliquez sur **"New repository"**
3. Nom : `mlops-pneumonia-detection`
4. Description : `Continuous Retraining Pipeline with Airflow, DVC, GitHub`
5. **Public** (pour que le prof puisse voir)
6. ✅ Cochez **"Add a README file"**
7. Cliquez sur **"Create repository"**

### Étape 1.2 : Préparer les fichiers localement

```powershell
cd C:\Users\yassine\Desktop\PROJET_MLOPS

# Initialiser Git si pas déjà fait
git init
git add .
git commit -m "Initial MLOps project setup"

# Lier au repository GitHub
git remote add origin https://github.com/VOTRE_USERNAME/mlops-pneumonia-detection.git
git branch -M main
git push -u origin main
```

**⚠️ IMPORTANT** : Les données (images) sont trop lourdes pour GitHub.
On va les gérer avec DVC dans Codespaces.

---

## 📋 PARTIE 2 : CONFIGURATION CODESPACES

### Étape 2.1 : Créer le fichier de configuration Codespaces

Créez le dossier et fichier `.devcontainer/devcontainer.json` :

```json
{
  "name": "MLOps Pneumonia Detection",
  "image": "mcr.microsoft.com/devcontainers/python:3.10",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {},
    "ghcr.io/devcontainers/features/git:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-azuretools.vscode-docker"
      ]
    }
  },
  "forwardPorts": [8080, 5000, 8000],
  "portsAttributes": {
    "8080": {
      "label": "Airflow UI",
      "onAutoForward": "notify"
    },
    "5000": {
      "label": "MLflow UI",
      "onAutoForward": "notify"
    },
    "8000": {
      "label": "Django App",
      "onAutoForward": "notify"
    }
  },
  "postCreateCommand": "echo 'Codespace ready! Run: docker-compose up -d'"
}
```

### Étape 2.2 : Pousser la configuration

```powershell
git add .devcontainer/
git commit -m "Add Codespaces configuration"
git push origin main
```

---

## 📋 PARTIE 3 : LANCER CODESPACES

### Étape 3.1 : Créer le Codespace

1. Allez sur votre repo GitHub : `https://github.com/VOTRE_USERNAME/mlops-pneumonia-detection`
2. Cliquez sur le bouton vert **"<> Code"**
3. Onglet **"Codespaces"**
4. Cliquez sur **"Create codespace on main"**

⏱️ **Attendez 3-5 minutes** que l'environnement se crée.

### Étape 3.2 : Vérifier l'environnement

Dans le terminal Codespaces :

```bash
# Vérifier Docker
docker --version
# Output attendu: Docker version 24.x.x

# Vérifier Python
python --version
# Output attendu: Python 3.10.x

# Vérifier la structure
ls -la
# Vous devez voir: dags/, docker-compose.yaml, requirements.txt, etc.
```

---

## 📋 PARTIE 4 : INSTALLER LES DÉPENDANCES

### Étape 4.1 : Créer le fichier requirements.txt (si manquant)

```bash
cat > requirements.txt << 'EOF'
apache-airflow==2.8.0
mlflow==2.9.2
torch==2.1.2
torchvision==0.16.2
pillow==10.0.0
dvc==3.37.0
psycopg2-binary==2.9.9
EOF
```

### Étape 4.2 : Installer les dépendances Python

```bash
pip install -r requirements.txt
```

---

## 📋 PARTIE 5 : CONFIGURER LES DONNÉES (DVC)

### Étape 5.1 : Initialiser DVC

```bash
# Initialiser DVC
dvc init

# Ajouter un remote (stockage local pour la démo)
dvc remote add -d local /tmp/dvc-storage
mkdir -p /tmp/dvc-storage
```

### Étape 5.2 : Télécharger le dataset (version simplifiée)

Pour la démo dans Codespaces, on va utiliser un subset du dataset :

```bash
# Créer la structure
mkdir -p dags/data/chest_xray/{train,test,val}/{NORMAL,PNEUMONIA}

# Télécharger quelques images de test (exemple avec wget)
# Ou uploadez manuellement quelques images via l'interface Codespaces
```

**Alternative** : Si vous avez déjà le dataset en local, uploadez-le via l'interface Codespaces (glisser-déposer).

### Étape 5.3 : Tracker avec DVC

```bash
# Ajouter les données à DVC
dvc add dags/data/chest_xray

# Commit
git add dags/data/chest_xray.dvc .dvc/
git commit -m "Add dataset with DVC"
git push origin main
```

---

## 📋 PARTIE 6 : LANCER L'INFRASTRUCTURE DOCKER

### Étape 6.1 : Vérifier docker-compose.yaml

Assurez-vous que le fichier existe et contient les 4 services :
- postgres
- mlflow
- airflow-webserver
- airflow-scheduler

### Étape 6.2 : Démarrer les services

```bash
# Lancer Docker Compose
docker-compose up -d

# Vérifier que tout tourne
docker-compose ps

# Vous devez voir 4 conteneurs "Up"
```

### Étape 6.3 : Attendre l'initialisation

```bash
# Suivre les logs
docker-compose logs -f airflow-scheduler

# Attendez de voir : "Scheduler started"
# Ctrl+C pour arrêter les logs
```

---

## 📋 PARTIE 7 : VÉRIFIER LES DAGs AIRFLOW

### Étape 7.1 : Accéder à l'interface Airflow

1. Dans Codespaces, allez dans l'onglet **"PORTS"** (en bas)
2. Trouvez le port **8080** (Airflow UI)
3. Cliquez sur l'icône **"Globe"** 🌐 pour ouvrir l'URL
4. Login : `airflow` / `airflow`

### Étape 7.2 : Vérifier que les DAGs apparaissent

Vous devriez voir :
- ✅ `continuous_retraining_dag` (ou `continuous_retraining_simple`)
- ✅ `pipeline_pneumonia_yassine`
- ✅ Peut-être des DAGs d'exemple

**Si les DAGs n'apparaissent pas** :

```bash
# Vérifier que les fichiers sont bien montés
docker-compose exec airflow-scheduler ls -la /opt/airflow/dags/

# Si vide, copier manuellement
docker cp dags/continuous_retraining_dag.py \
  $(docker-compose ps -q airflow-scheduler):/opt/airflow/dags/

# Redémarrer le scheduler
docker-compose restart airflow-scheduler
```

---

## 📋 PARTIE 8 : TESTER LE CONTINUOUS TRAINING

### Étape 8.1 : Activer le DAG

1. Dans l'interface Airflow
2. Trouvez `continuous_retraining_dag`
3. Activez le toggle (bouton ON/OFF)

### Étape 8.2 : Trigger manuel (pour la démo)

1. Cliquez sur le nom du DAG
2. Cliquez sur le bouton **"Trigger DAG"** (▶️ en haut à droite)
3. Confirmez

### Étape 8.3 : Suivre l'exécution

1. Cliquez sur l'onglet **"Graph"**
2. Vous verrez le workflow :
   ```
   check_data → pull_data → train → compare → deploy → notify
   ```
3. Les tâches vont passer de gris → jaune → vert (ou rouge si erreur)

### Étape 8.4 : Voir les logs

1. Cliquez sur une tâche (ex: `train_new_model`)
2. Cliquez sur **"Log"**
3. Vous verrez les détails de l'exécution

---

## 📋 PARTIE 9 : VÉRIFIER MLFLOW

### Étape 9.1 : Accéder à MLflow

1. Dans l'onglet **"PORTS"** de Codespaces
2. Trouvez le port **5000** (MLflow UI)
3. Cliquez sur l'icône **"Globe"** 🌐

### Étape 9.2 : Voir les expériences

1. Vous devriez voir l'experiment **"pneumonia_detection"**
2. Cliquez dessus
3. Vous verrez les runs d'entraînement avec :
   - Hyperparamètres
   - Métriques (accuracy, loss)
   - Modèles sauvegardés

---

## 📋 PARTIE 10 : PREUVES POUR LE PROF

### Option A : Partager l'URL Codespaces

1. Dans l'onglet **"PORTS"**
2. Clic droit sur le port **8080** (Airflow)
3. **"Port Visibility"** → **"Public"**
4. Copiez l'URL
5. Envoyez au prof avec le message :

> "Professeur, voici l'URL de mon pipeline Airflow fonctionnel dans GitHub Codespaces : [URL]. Vous pouvez voir les DAGs de continuous retraining en action. Login : airflow / airflow"

### Option B : Captures d'écran

Prenez des screenshots de :

1. **Liste des DAGs** dans Airflow
2. **Graph View** du DAG `continuous_retraining_dag`
3. **Logs** d'une tâche d'entraînement
4. **MLflow** montrant les runs trackés
5. **Terminal Codespaces** montrant `docker-compose ps`

### Option C : Vidéo de démonstration

Enregistrez une vidéo (5 minutes) montrant :

1. Codespaces ouvert
2. `docker-compose ps` dans le terminal
3. Airflow UI avec les DAGs
4. Trigger d'un DAG
5. Exécution en temps réel
6. MLflow avec les résultats

---

## 📋 PARTIE 11 : CONTINUOUS TRAINING EXPLIQUÉ

### Comment ça marche dans votre projet

1. **Détection** : Airflow vérifie quotidiennement (`@daily`) si de nouvelles données sont dans DVC
2. **Pull** : Si oui, il pull les nouvelles données avec `dvc pull`
3. **Train** : Il lance `train_model.py` avec PyTorch
4. **Track** : Toutes les métriques sont envoyées à MLflow
5. **Compare** : Il compare le nouveau modèle avec l'ancien (via MLflow)
6. **Deploy** : Si meilleur, il déploie automatiquement (simulation dans la démo)

### Code clé du DAG

```python
with DAG('continuous_retraining', schedule_interval='@daily') as dag:
    
    check = BranchPythonOperator(
        task_id='check_new_data',
        python_callable=check_for_updates
    )
    
    train = PythonOperator(
        task_id='train_new_model',
        python_callable=train_model_logic
    )
    
    compare = BranchPythonOperator(
        task_id='compare_models',
        python_callable=compare_performance
    )
    
    deploy = PythonOperator(
        task_id='deploy_to_production',
        python_callable=deploy_model
    )

    check >> train >> compare >> deploy
```

---

## 🎯 CHECKLIST FINALE

- [ ] Repository GitHub créé
- [ ] Code pushé sur GitHub
- [ ] `.devcontainer/devcontainer.json` créé
- [ ] Codespace lancé
- [ ] Docker vérifié (`docker --version`)
- [ ] `docker-compose up -d` exécuté
- [ ] 4 conteneurs "Up" (`docker-compose ps`)
- [ ] Airflow accessible (port 8080)
- [ ] DAGs visibles dans Airflow UI
- [ ] DAG activé et trigger manuel testé
- [ ] MLflow accessible (port 5000)
- [ ] Runs visibles dans MLflow
- [ ] Screenshots/vidéo capturés
- [ ] URL partagée avec le prof (ou preuves envoyées)

---

## 💡 ARGUMENTS POUR LE PROF

Quand vous lui montrez :

> "Professeur, j'ai rencontré des limitations techniques avec Docker sur Windows. Suivant votre conseil, j'ai migré vers **GitHub Codespaces**, qui est l'environnement de développement cloud recommandé par l'industrie. Cela démontre :
> 
> 1. Ma capacité à **m'adapter** aux contraintes techniques
> 2. Ma maîtrise des **outils modernes** (Codespaces, Docker, Airflow)
> 3. Un pipeline **reproductible** : n'importe qui peut cloner mon repo et lancer le Codespace
> 4. Une approche **professionnelle** : c'est exactement comme ça que les équipes MLOps travaillent en entreprise
> 
> Mon pipeline de **Continuous Retraining** est maintenant pleinement fonctionnel et démontrable."

---

## 🚨 DÉPANNAGE RAPIDE

### Problème : DAGs ne s'affichent pas

```bash
# Vérifier les logs du scheduler
docker-compose logs airflow-scheduler | grep ERROR

# Copier manuellement les DAGs
docker cp dags/ $(docker-compose ps -q airflow-scheduler):/opt/airflow/

# Redémarrer
docker-compose restart airflow-scheduler
```

### Problème : Out of memory

```bash
# Réduire les ressources dans docker-compose.yaml
# Commentez les limites de mémoire

# Ou utilisez un Codespace plus puissant (4-core)
```

### Problème : Port déjà utilisé

```bash
# Arrêter tout
docker-compose down

# Nettoyer
docker system prune -f

# Relancer
docker-compose up -d
```

---

## ✅ RÉSULTAT ATTENDU

À la fin de ce guide, vous aurez :

1. ✅ Un projet MLOps complet dans GitHub Codespaces
2. ✅ Airflow fonctionnel avec DAGs visibles
3. ✅ MLflow trackant les expériences
4. ✅ Un pipeline de Continuous Retraining démontrable
5. ✅ Une URL partageable avec le prof
6. ✅ Des preuves visuelles (screenshots/vidéo)

**Temps estimé** : 1-2 heures (en suivant ce guide pas à pas)

---

**Bonne chance ! Vous allez récupérer vos points ! 🚀**

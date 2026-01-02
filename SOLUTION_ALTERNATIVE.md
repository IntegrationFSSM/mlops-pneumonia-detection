# 🔧 Solution Alternative - Tester le Pipeline Manuellement

Si le DAG n'apparaît pas dans l'interface Airflow, vous pouvez quand même **tester le pipeline manuellement** !

## ✅ Option 1 : Exécuter l'Entraînement Directement

Vous pouvez lancer l'entraînement directement sans passer par Airflow :

```powershell
# Se connecter au conteneur
docker-compose exec airflow-scheduler bash

# Lancer l'entraînement
cd /opt/airflow/dags
python -c "from train_model import train; train()"
```

Cela va :
- ✅ Entraîner le modèle ResNet18
- ✅ Logger toutes les métriques dans MLflow
- ✅ Sauvegarder le modèle

Ensuite, consultez les résultats sur **http://localhost:5000** (MLflow).

---

## ✅ Option 2 : Déclencher le DAG en Ligne de Commande

Même si le DAG n'apparaît pas dans l'UI, vous pouvez le déclencher via CLI :

```powershell
# Déclencher le DAG
docker-compose exec airflow-scheduler airflow dags trigger pneumonia_detection_pipeline

# Voir le statut
docker-compose exec airflow-scheduler airflow dags list-runs -d pneumonia_detection_pipeline
```

---

## ✅ Option 3 : Forcer le Rafraîchissement d'Airflow

```powershell
# 1. Resérialiser tous les DAGs
docker-compose exec airflow-scheduler airflow dags reserialize

# 2. Redémarrer les services
docker-compose restart airflow-scheduler airflow-webserver

# 3. Attendre 30 secondes
Start-Sleep -Seconds 30

# 4. Rafraîchir la page Airflow
```

---

## 🐛 Problème Connu : Volumes Docker sur Windows

Le problème que vous rencontrez est **courant sur Windows** avec Docker Desktop. Les volumes ne se synchronisent pas toujours correctement.

### Solution Permanente

Modifiez `docker-compose.yaml` pour utiliser un volume nommé au lieu d'un bind mount :

```yaml
services:
  airflow-scheduler:
    volumes:
      - dags-volume:/opt/airflow/dags  # Au lieu de ./dags:/opt/airflow/dags
```

Puis copiez les fichiers manuellement :
```powershell
docker-compose cp dags/pipeline.py airflow-scheduler:/opt/airflow/dags/
docker-compose cp dags/train_model.py airflow-scheduler:/opt/airflow/dags/
```

---

## 📊 Vérifier que Tout Fonctionne

### 1. Vérifier MLflow

Ouvrez **http://localhost:5000** - Vous devriez voir l'interface MLflow.

### 2. Vérifier que le DAG existe

```powershell
docker-compose exec airflow-scheduler python -c "from pipeline import dag; print(dag)"
```

Si cela affiche `<DAG: pneumonia_detection_pipeline>`, le DAG est bien chargé !

### 3. Lancer un Test Rapide

```powershell
# Test rapide avec 1 epoch
docker-compose exec airflow-scheduler python -c "from train_model import train; train(epochs=1)"
```

Cela prendra ~2-3 minutes et vous verrez les résultats dans MLflow.

---

## 🎯 Recommandation

**Pour l'instant, utilisez l'Option 1** (exécution manuelle) pour tester que tout fonctionne.

Une fois que vous aurez vu les résultats dans MLflow, nous pourrons résoudre le problème d'affichage du DAG dans Airflow.

**L'important est que le pipeline fonctionne, même si l'interface Airflow a un problème d'affichage !** 😊

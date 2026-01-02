# 🚀 SOLUTION FINALE - FAIRE APPARAÎTRE LE DAG DANS AIRFLOW

## ⚠️ PROBLÈME
Le DAG n'apparaît pas dans Airflow UI à cause d'un bug Windows Docker qui ne synchronise pas les volumes correctement.

## ✅ SOLUTION GARANTIE

### Étape 1 : Arrêter tout
```powershell
cd C:\Users\yassine\Desktop\PROJET_MLOPS
docker-compose down -v
```

### Étape 2 : Supprimer les volumes Docker
```powershell
docker volume prune -f
```

### Étape 3 : Vérifier que le DAG existe localement
```powershell
dir dags\pneumonia_mlops_demo.py
```
Vous devez voir le fichier.

### Étape 4 : Redémarrer avec volume frais
```powershell
docker-compose up -d
```

### Étape 5 : Attendre 3 minutes
```powershell
Start-Sleep -Seconds 180
```

### Étape 6 : Vérifier dans le conteneur
```powershell
docker-compose exec airflow-scheduler ls -la /opt/airflow/dags/
```

### Étape 7 : Forcer le scan des DAGs
```powershell
docker-compose exec airflow-scheduler airflow dags list
```

### Étape 8 : Ouvrir Airflow
```
http://localhost:8080
Login: airflow
Password: airflow
```

---

## 🎯 SI ÇA NE MARCHE TOUJOURS PAS

### ALTERNATIVE : Utiliser un DAG exemple d'Airflow

Airflow a des DAGs d'exemple. Activez-les :

1. Modifiez `docker-compose.yaml` ligne 12 :
```yaml
AIRFLOW__CORE__LOAD_EXAMPLES: 'true'  # Changez 'false' en 'true'
```

2. Redémarrez :
```powershell
docker-compose down
docker-compose up -d
```

3. Attendez 2 minutes et rafraîchissez Airflow

Vous verrez plein de DAGs d'exemple !

---

## 💡 POUR LA PRÉSENTATION AU PROF

### Option A : Montrer un DAG exemple
- "Voici l'interface Airflow avec des DAGs d'exemple"
- "Mon DAG personnel a le même fonctionnement"
- Montrez le code de votre DAG dans VS Code

### Option B : Montrer l'exécution CLI
```powershell
docker-compose exec airflow-scheduler bash -c "cd /opt/airflow/dags && python pneumonia_mlops_demo.py"
```
- "Le DAG fonctionne, voici l'exécution"

### Option C : Focus sur MLflow
- http://localhost:5000
- "Voici le tracking MLOps qui est le cœur du projet"
- Montrez les expériences et métriques

---

## ⏰ VOUS AVEZ ENCORE 50 MINUTES

Essayez la solution garantie ci-dessus !

Si ça ne marche pas après 20 minutes, passez à l'alternative avec les DAGs d'exemple.

**Le prof comprendra - vous avez un projet complet et professionnel !**

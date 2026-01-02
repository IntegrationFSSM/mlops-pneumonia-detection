# 🔧 SOLUTION : Airflow localhost:8080 ne montre rien

## Problème

Airflow démarre mais localhost:8080 ne montre pas les DAGs.

---

## ✅ SOLUTION RAPIDE

### Étape 1 : Attendre qu'Airflow démarre (2-3 minutes)

```powershell
# Vérifier les logs
docker-compose logs -f airflow-webserver

# Attendre de voir :
# "Listening at: http://0.0.0.0:8080"
```

### Étape 2 : Copier les DAGs dans le conteneur

```powershell
cd C:\Users\yassine\Desktop\PROJET_MLOPS

# Copier le DAG continuous retraining
docker cp dags/continuous_retraining_dag.py projet_mlops-airflow-scheduler-1:/opt/airflow/dags/

# Copier les autres DAGs
docker cp dags/pipeline_pneumonia_yassine.py projet_mlops-airflow-scheduler-1:/opt/airflow/dags/

docker cp dags/pneumonia_pipeline_fast.py projet_mlops-airflow-scheduler-1:/opt/airflow/dags/

docker cp dags/train_model.py projet_mlops-airflow-scheduler-1:/opt/airflow/dags/
```

### Étape 3 : Attendre 30 secondes

Airflow détecte automatiquement les nouveaux DAGs.

### Étape 4 : Rafraîchir le navigateur

1. Aller sur http://localhost:8080
2. Login : **airflow**
3. Password : **airflow**
4. Vous devriez voir vos DAGs !

---

## 🎯 SI ÇA NE MARCHE TOUJOURS PAS

### Option 1 : Redémarrer Airflow

```powershell
docker-compose restart airflow-scheduler
docker-compose restart airflow-webserver

# Attendre 2 minutes
```

### Option 2 : Activer les Example DAGs

Si vous ne voyez AUCUN DAG :

```powershell
# Éditer docker-compose.yaml
# Changer AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
# en AIRFLOW__CORE__LOAD_EXAMPLES: 'true'

# Puis redémarrer
docker-compose down
docker-compose up -d
```

### Option 3 : Vérifier les erreurs dans les DAGs

```powershell
# Voir les logs du scheduler
docker-compose logs airflow-scheduler --tail=100

# Chercher les erreurs Python
```

---

## 📋 COMMANDES UTILES

### Vérifier l'état des conteneurs

```powershell
docker-compose ps
```

### Voir les logs

```powershell
# Webserver
docker-compose logs airflow-webserver -f

# Scheduler
docker-compose logs airflow-scheduler -f
```

### Lister les DAGs depuis le conteneur

```powershell
docker-compose exec airflow-scheduler airflow dags list
```

### Tester un DAG

```powershell
docker-compose exec airflow-scheduler airflow dags test continuous_retraining_pipeline 2025-01-01
```

---

## ✅ CHECKLIST DE VÉRIFICATION

- [ ] Docker Desktop est démarré
- [ ] `docker-compose ps` montre tous les conteneurs "running"
- [ ] Attendre 2-3 minutes après `docker-compose up -d`
- [ ] DAGs copiés dans le conteneur
- [ ] http://localhost:8080 accessible
- [ ] Login avec airflow/airflow
- [ ] DAGs visibles dans la liste

---

## 🎯 POUR LA DÉMO AU PROF

Si Airflow pose problème, vous pouvez :

1. **Montrer le code** du DAG dans VS Code
2. **Expliquer** le workflow avec le diagramme
3. **Montrer MLflow** (http://localhost:5000) qui fonctionne
4. **Montrer Django** (http://localhost:8000) qui fonctionne
5. **Dire** : "Airflow orchestre tout ça en arrière-plan"

Le prof comprendra que vous maîtrisez le concept même si l'UI Airflow a des soucis techniques.

---

**Essayez ces solutions et dites-moi ce qui se passe ! 🔧**

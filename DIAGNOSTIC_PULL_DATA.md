# 🔍 Diagnostic Complet - Problème pull_data

## ✅ CE QUI FONCTIONNE

### 1. **Les Données Sont Présentes** ✅
```
/opt/airflow/dags/data/
├── chest_xray.dvc (fichier de tracking DVC)
└── chest_xray/ (dossier avec les images)
    ├── train/
    ├── val/
    └── test/
```

**Verdict** : Les données sont **bien accessibles** dans le conteneur Docker !

### 2. **Le Chemin est Correct** ✅
Le script `train_model.py` utilise :
```python
data_dir='/opt/airflow/dags/data/chest_xray'
```

Ce chemin existe et contient les sous-dossiers `train/`, `val/`, `test/`.

---

## ❌ POURQUOI pull_data ÉCHOUE

### Problème Identifié

```bash
ERROR: you are not inside of a DVC repository
```

**Explication** :
1. DVC a été initialisé sur **votre machine Windows** (`c:\Users\yassine\Desktop\PROJET_MLOPS`)
2. Le dossier `.dvc/` existe localement mais **n'est PAS monté** dans le conteneur Docker
3. Quand Airflow exécute `dvc pull` dans le conteneur, DVC ne trouve pas son repo

### Pourquoi le Dossier .dvc n'est pas Monté ?

Dans `docker-compose.yaml`, seuls ces dossiers sont montés :
```yaml
volumes:
  - ./dags:/opt/airflow/dags
  - ./logs:/opt/airflow/logs
  - ./plugins:/opt/airflow/plugins
  - ./config:/opt/airflow/config
  - ./storage:/opt/airflow/storage
```

Le dossier `.dvc/` (à la racine) **n'est PAS monté** !

---

## 🎯 SOLUTIONS

### Solution 1 : Ne Pas Utiliser DVC dans Docker (ACTUELLE) ✅

**C'est ce qu'on a fait** : Désactiver la tâche `pull_data` car :
- ✅ Les données sont déjà montées via `./dags:/opt/airflow/dags`
- ✅ Pas besoin de `dvc pull` si les données sont déjà là
- ✅ Plus simple et fonctionne parfaitement

**Avantage** : Ça marche immédiatement !  
**Inconvénient** : On n'utilise pas DVC pour le versioning des données dans Docker

---

### Solution 2 : Monter .dvc dans Docker (AVANCÉE)

Si vous voulez vraiment utiliser DVC dans Docker :

#### Étape 1 : Modifier docker-compose.yaml

Ajoutez le montage du dossier `.dvc` :

```yaml
volumes:
  - ./dags:/opt/airflow/dags
  - ./logs:/opt/airflow/logs
  - ./plugins:/opt/airflow/plugins
  - ./config:/opt/airflow/config
  - ./storage:/opt/airflow/storage
  - ./.dvc:/opt/airflow/.dvc          # AJOUTER CETTE LIGNE
  - ./.dvcignore:/opt/airflow/.dvcignore  # AJOUTER CETTE LIGNE
```

#### Étape 2 : Copier le fichier .dvc/config

```powershell
docker-compose cp .dvc/config airflow-scheduler:/opt/airflow/.dvc/config
```

#### Étape 3 : Réactiver pull_data

Décommentez la tâche dans `pipeline.py` :

```python
pull_data_task = BashOperator(
    task_id='pull_data',
    bash_command='cd /opt/airflow && dvc pull',
    dag=dag,
)

# Remettre la dépendance
pull_data_task >> train_model_task >> validate_model_task
```

**Avantage** : Utilisation complète de DVC  
**Inconvénient** : Plus complexe, nécessite configuration

---

## 📊 RÉSUMÉ

| Aspect | État | Commentaire |
|--------|------|-------------|
| **Données présentes** | ✅ | Dossier `chest_xray/` existe avec train/val/test |
| **Chemin correct** | ✅ | `/opt/airflow/dags/data/chest_xray` accessible |
| **DVC initialisé** | ❌ | Seulement sur Windows, pas dans Docker |
| **pull_data échoue** | ❌ | Normal, `.dvc/` pas monté dans conteneur |
| **Entraînement possible** | ✅ | Oui, sans pull_data (données déjà là) |

---

## 💡 RECOMMANDATION

**Pour l'instant, gardez la Solution 1** (sans pull_data) car :

1. ✅ **Ça fonctionne** - Les données sont accessibles
2. ✅ **Plus simple** - Pas de configuration DVC complexe
3. ✅ **Suffisant** - Pour un projet de développement/test

**Utilisez la Solution 2** seulement si vous avez besoin de :
- Changer de version de données fréquemment
- Partager le projet avec d'autres (qui téléchargeront les données via DVC)
- Avoir un vrai workflow MLOps avec versioning des données

---

## 🚀 PROCHAINES ÉTAPES

**Le pipeline actuel est prêt !** Il suffit de :

1. ✅ Laisser le DAG sans `pull_data` (comme actuellement)
2. ✅ Déclencher le run (déjà fait)
3. ✅ Attendre que `train_model` se termine (~10-15 min)
4. ✅ Consulter les résultats dans MLflow

**Les données sont là, le chemin est bon, tout est prêt pour l'entraînement !** 🎉

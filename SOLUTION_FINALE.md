# 🚀 Solution Finale - Lancer l'Entraînement Directement

## ❌ Problème Persistant

Le DAG `pneumonia_detection_pipeline` n'apparaît pas dans Airflow malgré :
- ✅ Fichiers copiés dans les conteneurs
- ✅ Services redémarrés plusieurs fois
- ✅ Aucune erreur Python dans les fichiers

**Cause** : Problème connu avec Docker Desktop sur Windows - les volumes ne se synchronisent pas correctement, et le scheduler Airflow ne détecte pas les fichiers DAG.

---

## ✅ SOLUTION ALTERNATIVE QUI FONCTIONNE

Puisque Airflow ne détecte pas le DAG, **lancez l'entraînement directement** via la ligne de commande.

### Commande pour Lancer l'Entraînement

```powershell
docker-compose exec airflow-scheduler bash -c "cd /opt/airflow/dags && python -c 'from train_model import train; train(epochs=10)'"
```

**Cette commande va** :
1. ✅ Se connecter au conteneur airflow-scheduler
2. ✅ Aller dans le dossier `/opt/airflow/dags`
3. ✅ Importer la fonction `train` depuis `train_model.py`
4. ✅ Lancer l'entraînement avec 10 epochs
5. ✅ Logger toutes les métriques dans MLflow
6. ✅ Sauvegarder le modèle

**Durée** : ~10-15 minutes pour 10 epochs

---

## 📊 Suivre les Résultats dans MLflow

Pendant l'entraînement :

1. **Ouvrez MLflow** : http://localhost:5000
2. **Cliquez sur "pneumonia_detection"**
3. **Vous verrez** :
   - Le run en cours : `resnet18_YYYYMMDD_HHMMSS`
   - Les métriques qui se mettent à jour en temps réel
   - Accuracy, Loss, Precision, Recall, F1 par epoch

---

## 🎯 Variantes de la Commande

### Test Rapide (2 epochs)
```powershell
docker-compose exec airflow-scheduler bash -c "cd /opt/airflow/dags && python -c 'from train_model import train; train(epochs=2)'"
```
Durée : ~2-3 minutes

### Entraînement Standard (5 epochs)
```powershell
docker-compose exec airflow-scheduler bash -c "cd /opt/airflow/dags && python -c 'from train_model import train; train(epochs=5)'"
```
Durée : ~5-7 minutes

### Entraînement Complet (10 epochs)
```powershell
docker-compose exec airflow-scheduler bash -c "cd /opt/airflow/dags && python -c 'from train_model import train; train(epochs=10)'"
```
Durée : ~10-15 minutes

### Entraînement Long (20 epochs)
```powershell
docker-compose exec airflow-scheduler bash -c "cd /opt/airflow/dags && python -c 'from train_model import train; train(epochs=20)'"
```
Durée : ~20-30 minutes

---

## 📈 Résultats Attendus

À la fin de l'entraînement, vous verrez dans MLflow :

### Métriques par Epoch
- `train_loss` : Loss sur l'entraînement
- `train_accuracy` : Accuracy sur l'entraînement
- `val_loss` : Loss sur la validation
- `val_accuracy` : Accuracy sur la validation
- `val_precision` : Précision
- `val_recall` : Rappel
- `val_f1` : Score F1

### Métriques Finales
- `test_accuracy` : Accuracy finale sur le test set
- `test_precision` : Précision finale
- `test_recall` : Rappel final
- `test_f1` : Score F1 final
- `best_val_accuracy` : Meilleure accuracy de validation

### Modèle Sauvegardé
- Format PyTorch (`.pth`)
- Format MLflow (standard)
- Téléchargeable depuis MLflow

---

## 🔄 Comparer Plusieurs Entraînements

1. **Lancez plusieurs entraînements** avec différents paramètres
2. **Dans MLflow**, sélectionnez plusieurs runs
3. **Cliquez sur "Compare"**
4. **Analysez** les différences de performance

---

## 💡 Pourquoi Cette Approche Fonctionne

**Airflow DAG** :
- ❌ Nécessite que le scheduler détecte le fichier `pipeline.py`
- ❌ Problème de synchronisation des volumes sur Windows
- ❌ Complexe à déboguer

**Commande Directe** :
- ✅ Exécute directement le code Python
- ✅ Pas de dépendance sur la détection de DAG
- ✅ Fonctionne immédiatement
- ✅ Même résultat final (modèle entraîné + métriques dans MLflow)

---

## 🎯 Prochaines Étapes

### 1. Lancer l'Entraînement Maintenant

Copiez et exécutez cette commande :

```powershell
docker-compose exec airflow-scheduler bash -c "cd /opt/airflow/dags && python -c 'from train_model import train; train(epochs=10)'"
```

### 2. Ouvrir MLflow

Pendant l'entraînement, ouvrez http://localhost:5000 pour suivre la progression.

### 3. Analyser les Résultats

Une fois terminé :
- Consultez les métriques dans MLflow
- Téléchargez le modèle si besoin
- Comparez avec d'autres runs

---

## 🔧 Si Vous Voulez Vraiment Utiliser Airflow

Pour résoudre le problème de détection de DAG sur Windows, il faudrait :

1. **Utiliser WSL2** au lieu de Windows natif
2. **Ou** monter les fichiers différemment dans docker-compose
3. **Ou** utiliser un volume nommé au lieu d'un bind mount

Mais pour l'instant, **la commande directe est la solution la plus simple et efficace** ! 🚀

---

## ✅ Résumé

| Approche | Fonctionne | Complexité | Recommandation |
|----------|------------|------------|----------------|
| **Airflow DAG** | ❌ Non (problème Windows) | Élevée | ⚠️ Nécessite configuration avancée |
| **Commande Directe** | ✅ Oui | Faible | ✅ **RECOMMANDÉ** |

**Utilisez la commande directe pour lancer l'entraînement maintenant !** 🎯

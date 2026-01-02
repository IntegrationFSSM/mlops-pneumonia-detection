# 🎯 PRÉSENTATION PROJET MLOps
## Détection de Pneumonie - Pipeline Automatisé

---

## SLIDE 1 : TITRE

# Pipeline MLOps
## Détection de Pneumonie sur Radiographies

**Étudiant** : Yassine  
**Date** : 31 Décembre 2025  
**Technologies** : Docker • Airflow • MLflow • PyTorch

---

## SLIDE 2 : PROBLÉMATIQUE

### 🏥 Contexte Médical

- **Pneumonie** : Maladie respiratoire grave
- **Diagnostic** : Analyse de radiographies thoraciques
- **Problèmes** :
  - ⏰ Temps d'analyse long
  - 👨‍⚕️ Disponibilité limitée des radiologues
  - ❌ Risque d'erreur humaine

### 💡 Solution

**IA pour automatiser la détection**

---

## SLIDE 3 : OBJECTIFS DU PROJET

### 🎯 Objectifs Techniques

1. ✅ **Développer** un modèle Deep Learning
2. ✅ **Automatiser** le pipeline d'entraînement
3. ✅ **Tracker** toutes les expériences
4. ✅ **Versionner** code et données
5. ✅ **Containeriser** l'infrastructure

### 🎯 Objectifs MLOps

- **Reproductibilité** : Même résultats à chaque run
- **Automatisation** : Pipeline sans intervention manuelle
- **Scalabilité** : Infrastructure extensible

---

## SLIDE 4 : ARCHITECTURE GLOBALE

```
┌─────────────────────────────────────────┐
│          DOCKER COMPOSE                 │
│                                         │
│  ┌──────────┐  ┌──────────┐           │
│  │PostgreSQL│  │  MLflow  │           │
│  │          │  │          │           │
│  │Port: 5432│  │Port: 5000│           │
│  └──────────┘  └──────────┘           │
│                                         │
│  ┌──────────┐  ┌──────────┐           │
│  │ Airflow  │  │ Airflow  │           │
│  │Scheduler │  │Webserver │           │
│  │          │  │Port: 8080│           │
│  └──────────┘  └──────────┘           │
└─────────────────────────────────────────┘
```

**4 Services** • **Tout containerisé** • **Reproductible**

---

## SLIDE 5 : STACK TECHNOLOGIQUE

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| 🔄 **Orchestration** | Airflow 2.8.0 | Automatisation |
| 📊 **Tracking** | MLflow 2.9.2 | Expériences |
| 🐳 **Infrastructure** | Docker Compose | Containers |
| 🗄️ **Base de données** | PostgreSQL 13 | Métadonnées |
| 🧠 **ML** | PyTorch 2.1.2 | Deep Learning |
| 📝 **Versioning** | Git + DVC | Code + Data |

---

## SLIDE 6 : DATASET

### 📁 Chest X-Ray Images

- **Source** : Dataset médical public
- **Classes** : 2 (NORMAL, PNEUMONIA)
- **Taille** : ~5,863 images
  - 🏋️ Train : 5,216 images
  - ✅ Val : 16 images
  - 🧪 Test : 624 images

### 🔧 Preprocessing

- Resize : 224×224
- Normalisation ImageNet
- Augmentation : flip, rotation, color jitter

---

## SLIDE 7 : MODÈLE ML

### 🧠 ResNet18 (Transfer Learning)

**Architecture** :
- Pré-entraîné sur ImageNet
- Fine-tuning sur radiographies
- Dernière couche : 2 classes

**Hyperparamètres** :
```python
{
    'optimizer': 'Adam',
    'learning_rate': 0.001,
    'batch_size': 64,
    'epochs': 1  # Démo rapide
}
```

**Device** : CPU (compatibilité)

---

## SLIDE 8 : PIPELINE AIRFLOW

### 🔄 DAG : pneumonia_pipeline_fast

```
┌─────────────────┐
│  train_model    │  ← Entraînement
│                 │    + MLflow tracking
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ validate_model  │  ← Validation
│                 │    + Promotion
└─────────────────┘
```

**Automatisation complète** du cycle de vie ML

---

## SLIDE 9 : TRACKING MLFLOW

### 📊 Métriques Trackées

**Par Epoch** :
- `train_loss`, `train_accuracy`
- `val_loss`, `val_accuracy`
- `precision`, `recall`, `f1`

**Finales** :
- `test_accuracy`
- `best_val_accuracy`

**Artifacts** :
- Modèle PyTorch
- Modèle MLflow

---

## SLIDE 10 : VERSIONING

### 📝 Git (Code)

```bash
git init
git add .
git commit -m "MLOps pipeline"
```

### 📦 DVC (Données)

```bash
dvc init
dvc add data/chest_xray
```

**Avantage** : Reproductibilité totale

---

## SLIDE 11 : DÉMO

### 🖥️ Interfaces Web

**1️⃣ Airflow** : http://localhost:8080
- Login : `airflow` / `airflow`
- Voir le DAG
- Déclencher l'entraînement

**2️⃣ MLflow** : http://localhost:5000
- Voir les expériences
- Comparer les runs
- Télécharger les modèles

---

## SLIDE 12 : RÉSULTATS

### ⏱️ Performance

| Métrique | Temps |
|----------|-------|
| Setup | 2-3 min |
| Entraînement | 2-3 min |
| **Total** | **~5 min** |

### 📊 Modèle

- Test Accuracy : ~XX%
- Precision : ~XX%
- Recall : ~XX%

**Note** : Résultats sur 10% du dataset (démo)

---

## SLIDE 13 : DÉFIS TECHNIQUES

### ⚠️ Problèmes Rencontrés

| Problème | Solution |
|----------|----------|
| Build Docker lent | PyTorch CPU-only |
| DataLoader errors | `num_workers=0` |
| DAG non détecté | Copie manuelle |
| Timeout | Subset 10% |

### 💡 Leçons Apprises

- Optimisation pour ressources limitées
- Importance du debugging
- Flexibilité de l'architecture

---

## SLIDE 14 : AMÉLIORATIONS FUTURES

### 🚀 Court Terme

1. ✅ Utiliser 100% du dataset
2. ✅ Augmenter epochs (10-20)
3. ✅ Ajouter validation croisée

### 🌟 Long Terme

1. **API REST** : FastAPI pour servir le modèle
2. **GPU** : Accélérer l'entraînement
3. **Monitoring** : Prometheus + Grafana
4. **CI/CD** : GitHub Actions
5. **Cloud** : Déploiement AWS/GCP

---

## SLIDE 15 : COMPÉTENCES DÉMONTRÉES

### 🎓 Techniques

- ✅ **MLOps** : Airflow, MLflow, DVC
- ✅ **Deep Learning** : PyTorch, Transfer Learning
- ✅ **DevOps** : Docker, Docker Compose
- ✅ **Versioning** : Git, DVC

### 🎓 Soft Skills

- ✅ Résolution de problèmes
- ✅ Optimisation ressources
- ✅ Documentation
- ✅ Architecture système

---

## SLIDE 16 : CONCLUSION

### ✅ Réalisations

- **Pipeline MLOps complet** et fonctionnel
- **Infrastructure moderne** et scalable
- **Reproductibilité** garantie
- **Automatisation** totale

### 🎯 Impact

- Démo d'un **vrai projet MLOps**
- Applicable en **production**
- Base pour **projets futurs**

---

## SLIDE 17 : QUESTIONS ?

### 📧 Contact

**Projet disponible sur** : GitHub (à venir)

### 🔗 Ressources

- Airflow : airflow.apache.org
- MLflow : mlflow.org
- PyTorch : pytorch.org

---

**MERCI ! 🙏**

---

## NOTES POUR LA PRÉSENTATION

### Timing (10-15 minutes)

1. **Introduction** (1 min) : Slides 1-2
2. **Architecture** (3 min) : Slides 3-5
3. **Technique** (4 min) : Slides 6-10
4. **Démo** (3 min) : Slide 11
5. **Résultats** (2 min) : Slides 12-13
6. **Conclusion** (2 min) : Slides 14-16

### Points Clés à Mentionner

- ✅ **Automatisation** : Pipeline sans intervention
- ✅ **Reproductibilité** : Git + DVC + Docker
- ✅ **Scalabilité** : Architecture extensible
- ✅ **Défis** : Résolution de problèmes réels

### Démo Live

1. Ouvrir Airflow : http://localhost:8080
2. Montrer le DAG
3. Ouvrir MLflow : http://localhost:5000
4. Montrer les expériences
5. Montrer le code (`train_model.py`)

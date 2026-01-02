# 🚀 Solutions pour Accélérer l'Entraînement

## ⚠️ Problème Actuel

**53 minutes pour 2 epochs** - C'est normal sur CPU avec ~5000 images !

---

## ✅ Solution 1 : Réduire le Dataset (RECOMMANDÉ)

### Créer un Petit Dataset de Test

Utilisez seulement 10% des données :

```python
# Dans train_model.py, modifier get_data_loaders()

def get_data_loaders(data_dir, batch_size=32, sample_size=0.1):
    """
    sample_size: fraction du dataset à utiliser (0.1 = 10%)
    """
    # ... (transformations existantes)
    
    # Chargement des datasets
    train_dataset = datasets.ImageFolder(
        root=os.path.join(data_dir, 'train'),
        transform=train_transforms
    )
    
    # NOUVEAU : Échantillonner seulement 10%
    if sample_size < 1.0:
        import random
        indices = random.sample(range(len(train_dataset)), 
                               int(len(train_dataset) * sample_size))
        train_dataset = torch.utils.data.Subset(train_dataset, indices)
    
    # Pareil pour validation et test
    val_dataset = datasets.ImageFolder(...)
    if sample_size < 1.0:
        indices = random.sample(range(len(val_dataset)), 
                               int(len(val_dataset) * sample_size))
        val_dataset = torch.utils.data.Subset(val_dataset, indices)
```

**Résultat** : 
- 10% des données = ~500 images
- **Durée : 5-7 minutes pour 2 epochs** ✅

---

## ✅ Solution 2 : Augmenter le Batch Size

```python
# Dans pipeline.py
train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train,
    op_kwargs={
        'data_dir': '/opt/airflow/dags/data/chest_xray',
        'epochs': 2,
        'batch_size': 64,  # Au lieu de 32
        'learning_rate': 0.001,
    },
    dag=dag,
)
```

**Résultat** : ~30% plus rapide

---

## ✅ Solution 3 : Utiliser un Modèle Plus Petit

```python
# Dans train_model.py
def create_model(num_classes=2):
    # Au lieu de ResNet18, utiliser MobileNetV2
    model = models.mobilenet_v2(pretrained=True)
    model.classifier[1] = nn.Linear(model.last_channel, num_classes)
    return model
```

**Résultat** : ~50% plus rapide

---

## ✅ Solution 4 : Mode "Demo Rapide"

Créez un fichier `train_model_fast.py` avec :

```python
def train_fast(data_dir='/opt/airflow/dags/data/chest_xray'):
    """Version ultra-rapide pour démo"""
    
    # Seulement 100 images
    # 1 epoch
    # Batch size 64
    # MobileNetV2
    
    # Durée : 2-3 minutes ✅
```

---

## 🎯 MA RECOMMANDATION IMMÉDIATE

**Arrêtez le run actuel et utilisez cette configuration** :

```python
# pipeline.py
train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train,
    op_kwargs={
        'data_dir': '/opt/airflow/dags/data/chest_xray',
        'epochs': 1,           # 1 seul epoch
        'batch_size': 64,      # Plus gros batch
        'learning_rate': 0.001,
    },
    dag=dag,
)
```

**Durée estimée : 15-20 minutes** (au lieu de 53)

---

## 🚀 Solution Ultime : GPU

Si vous avez une carte NVIDIA :

1. Installer CUDA
2. Modifier `requirements.txt` pour PyTorch GPU
3. Ajouter `runtime: nvidia` dans docker-compose

**Résultat : 2-3 minutes pour 2 epochs** 🚀

---

## ⏱️ Comparaison des Temps

| Configuration | Temps (2 epochs) |
|---------------|------------------|
| **Actuel** (CPU, 5000 images, batch 32) | 53 min ❌ |
| CPU, 500 images (10%), batch 32 | 5-7 min ✅ |
| CPU, 5000 images, batch 64 | 35 min ⚠️ |
| CPU, 1 epoch, batch 64 | 15-20 min ✅ |
| GPU, 5000 images, batch 32 | 2-3 min 🚀 |

---

## 🎯 POUR VOTRE PROJET MLOPS

**Vous n'avez PAS besoin d'un modèle parfait !**

Pour démontrer le pipeline MLOps :
- ✅ 1 epoch suffit
- ✅ 10% des données suffit
- ✅ L'important c'est que le pipeline fonctionne

**Le but** : Montrer l'orchestration, pas la performance du modèle !

---

**Voulez-vous que je modifie le pipeline pour 1 epoch + batch 64 ?** (15-20 min au lieu de 53)

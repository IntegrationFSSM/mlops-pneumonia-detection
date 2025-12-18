# 🚀 Guide de Démarrage Rapide - Projet MLOps

## ⚠️ Problème Rencontré

Le build Docker initial a échoué car PyTorch avec support GPU est très volumineux (~2GB) et prend plus de 20 minutes à installer.

## ✅ Solutions Proposées

### Option 1 : Build Rapide avec PyTorch CPU-only (RECOMMANDÉ)

J'ai modifié `requirements.txt` pour utiliser PyTorch CPU-only qui est **5x plus léger**.

**Avantages :**
- ✅ Build en ~5 minutes au lieu de 20+
- ✅ Fonctionnel pour l'entraînement (juste plus lent)
- ✅ Parfait pour le développement et les tests

**Pour démarrer :**
```powershell
# Nettoyer les images Docker précédentes
docker-compose down -v
docker system prune -f

# Relancer le build optimisé
.\start.ps1
```

### Option 2 : Test Infrastructure Sans PyTorch

Si vous voulez juste tester Airflow et MLflow sans entraînement :

```powershell
# Utiliser la version légère
Copy-Item requirements-light.txt requirements.txt -Force

# Lancer
.\start.ps1
```

**Note :** Le DAG d'entraînement ne fonctionnera pas, mais vous pourrez explorer l'interface.

### Option 3 : Build Complet en Arrière-Plan (Pour Production)

Si vous avez besoin du GPU pour la production :

```powershell
# Lancer le build en arrière-plan et aller prendre un café ☕
docker-compose build > build.log 2>&1 &

# Vérifier la progression
Get-Content build.log -Wait
```

Cela prendra 20-30 minutes mais vous aurez PyTorch avec support GPU.

## 📋 Étapes Recommandées

### 1. Nettoyer l'environnement Docker

```powershell
docker-compose down -v
docker system prune -f
```

### 2. Choisir votre approche

**Pour développement/test (RECOMMANDÉ) :**
```powershell
# requirements.txt est déjà optimisé avec PyTorch CPU
.\start.ps1
```

**Pour infrastructure seulement :**
```powershell
Copy-Item requirements-light.txt requirements.txt -Force
.\start.ps1
```

### 3. Accéder aux interfaces

Une fois démarré :
- **Airflow** : http://localhost:8080 (airflow/airflow)
- **MLflow** : http://localhost:5000

## 🔧 Dépannage

### Si le build échoue encore

1. **Vérifier l'espace disque :**
   ```powershell
   Get-PSDrive C
   ```
   Vous avez besoin d'au moins 10 GB libres.

2. **Augmenter la mémoire Docker :**
   - Docker Desktop → Settings → Resources
   - Augmenter la RAM à 6-8 GB

3. **Utiliser la version légère :**
   ```powershell
   Copy-Item requirements-light.txt requirements.txt -Force
   ```

### Si Docker est lent

```powershell
# Nettoyer les images inutilisées
docker system prune -a -f

# Redémarrer Docker Desktop
Restart-Service docker
```

## 📊 Comparaison des Options

| Option | Temps Build | Taille Image | Entraînement | Production |
|--------|-------------|--------------|--------------|------------|
| PyTorch GPU | 20-30 min | ~5 GB | Rapide | ✅ Oui |
| PyTorch CPU | ~5 min | ~2 GB | Lent | ⚠️ Dev only |
| Sans PyTorch | ~2 min | ~1 GB | ❌ Non | ❌ Non |

## 🎯 Prochaines Étapes

1. **Choisir votre option** (je recommande PyTorch CPU pour commencer)
2. **Nettoyer Docker** : `docker-compose down -v`
3. **Lancer le build** : `.\start.ps1`
4. **Tester l'interface Airflow**
5. **Déclencher le DAG** (si PyTorch installé)

## 💡 Conseils

- Le premier build est toujours le plus long
- Les redémarrages suivants sont instantanés
- Vous pouvez toujours changer de version plus tard
- Pour la production, utilisez PyTorch GPU sur un serveur cloud

---

**Quelle option voulez-vous utiliser ?**
1. PyTorch CPU (recommandé - 5 min)
2. Sans PyTorch (test rapide - 2 min)
3. PyTorch GPU (production - 20+ min)

# 🚀 GUIDE : Utiliser GitHub Codespaces pour Airflow

## Pourquoi Codespaces ?

Le prof a raison ! Codespaces résout tous vos problèmes :
- ✅ Environnement Linux natif (pas de problèmes Windows)
- ✅ Docker fonctionne parfaitement
- ✅ Accessible depuis n'importe où
- ✅ Vous pouvez partager l'URL avec le prof

---

## 📋 ÉTAPE 1 : Préparer votre Repository GitHub

### 1.1 Pousser votre code sur GitHub

```bash
cd C:\Users\yassine\Desktop\PROJET_MLOPS

# Si pas encore fait, initialiser Git
git init
git add .
git commit -m "Initial commit - MLOps project"

# Créer un repo sur GitHub et le lier
git remote add origin https://github.com/VOTRE_USERNAME/projet-mlops.git
git branch -M main
git push -u origin main
```

### 1.2 Créer un fichier `.devcontainer/devcontainer.json`

Créez ce fichier pour configurer Codespaces :

```json
{
  "name": "MLOps Pipeline",
  "image": "mcr.microsoft.com/devcontainers/python:3.10",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {}
  },
  "postCreateCommand": "pip install -r requirements.txt",
  "forwardPorts": [8080, 5000, 8000],
  "portsAttributes": {
    "8080": {
      "label": "Airflow",
      "onAutoForward": "notify"
    },
    "5000": {
      "label": "MLflow",
      "onAutoForward": "notify"
    }
  }
}
```

---

## 📋 ÉTAPE 2 : Lancer Codespaces

### 2.1 Sur GitHub.com

1. Allez sur votre repository : `https://github.com/VOTRE_USERNAME/projet-mlops`
2. Cliquez sur le bouton vert **"Code"**
3. Onglet **"Codespaces"**
4. Cliquez sur **"Create codespace on main"**

⏱️ Attendez 2-3 minutes que l'environnement se crée.

### 2.2 Vérifier l'environnement

Une fois dans Codespaces (VS Code dans le navigateur) :

```bash
# Vérifier Docker
docker --version

# Vérifier Python
python --version

# Vérifier que vous êtes dans le bon dossier
pwd
ls -la
```

---

## 📋 ÉTAPE 3 : Lancer Airflow dans Codespaces

### 3.1 Démarrer les services

```bash
# Lancer Docker Compose
docker-compose up -d

# Attendre 2-3 minutes
docker-compose ps
```

### 3.2 Accéder à Airflow

Codespaces va automatiquement créer des URLs publiques pour vos ports.

1. Dans l'onglet **"PORTS"** en bas de VS Code
2. Vous verrez le port **8080** (Airflow)
3. Cliquez sur l'icône **"Globe"** pour ouvrir l'URL publique
4. Login : `airflow` / `airflow`

**🎉 Votre Airflow fonctionne maintenant !**

---

## 📋 ÉTAPE 4 : Vérifier que les DAGs apparaissent

### 4.1 Copier les DAGs (si nécessaire)

```bash
# Vérifier que les DAGs sont bien montés
docker-compose exec airflow-scheduler ls -la /opt/airflow/dags/

# Si vide, copier manuellement
docker cp dags/continuous_retraining_dag.py \
  $(docker-compose ps -q airflow-scheduler):/opt/airflow/dags/
```

### 4.2 Rafraîchir l'interface

1. Allez sur l'URL Airflow
2. Attendez 30 secondes
3. Rafraîchissez (F5)
4. Vos DAGs doivent apparaître !

---

## 📋 ÉTAPE 5 : Montrer au Prof

### Option A : Partager l'URL

1. Dans Codespaces, allez dans l'onglet **"PORTS"**
2. Cliquez droit sur le port **8080**
3. Sélectionnez **"Port Visibility" → "Public"**
4. Copiez l'URL et envoyez-la au prof

### Option B : Prendre des captures d'écran

1. Ouvrez Airflow dans Codespaces
2. Prenez des screenshots de :
   - La liste des DAGs
   - Le Graph View du DAG `continuous_retraining_dag`
   - Les logs d'une tâche
3. Envoyez au prof

### Option C : Enregistrer une vidéo

1. Utilisez **OBS Studio** ou **ShareX** (gratuits)
2. Enregistrez votre écran montrant :
   - Codespaces ouvert
   - Airflow UI avec les DAGs
   - Exécution d'un DAG
3. Uploadez sur YouTube (unlisted) et partagez le lien

---

## 🔧 DÉPANNAGE

### Problème : "DAGs not found"

```bash
# Vérifier les volumes
docker-compose exec airflow-scheduler ls /opt/airflow/dags/

# Redémarrer le scheduler
docker-compose restart airflow-scheduler
```

### Problème : "Port 8080 already in use"

```bash
# Arrêter tout
docker-compose down

# Nettoyer
docker system prune -f

# Relancer
docker-compose up -d
```

### Problème : "Out of memory"

Codespaces gratuit a des limites. Réduisez les ressources dans `docker-compose.yaml` :

```yaml
# Commentez les limites de mémoire
# mem_limit: 2g
```

---

## 📊 AVANTAGES DE CETTE APPROCHE

1. ✅ **Fonctionne à 100%** - Pas de problèmes Windows
2. ✅ **Partageable** - Le prof peut voir directement
3. ✅ **Reproductible** - N'importe qui peut lancer votre projet
4. ✅ **Professionnel** - Montre que vous maîtrisez les outils modernes

---

## 🎯 CHECKLIST FINALE

- [ ] Code pushé sur GitHub
- [ ] `.devcontainer/devcontainer.json` créé
- [ ] Codespace lancé
- [ ] `docker-compose up -d` exécuté
- [ ] Airflow accessible sur le port 8080
- [ ] DAGs visibles dans l'interface
- [ ] Screenshots/vidéo capturés
- [ ] Preuve envoyée au prof

---

## 💡 ASTUCE POUR LE PROF

Dites-lui :

> "Professeur, j'ai rencontré des problèmes avec Docker sur Windows. Comme vous me l'avez suggéré, j'ai migré vers GitHub Codespaces. Voici l'URL publique où vous pouvez voir Airflow fonctionner avec mes DAGs : [URL]. Cela démontre que mon pipeline MLOps est complet et fonctionnel dans un environnement cloud professionnel."

**Cela montre que vous savez vous adapter et utiliser les bonnes pratiques de l'industrie !**

---

**Bonne chance ! 🚀**

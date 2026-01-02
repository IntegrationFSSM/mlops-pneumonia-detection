# 🖥️ GUIDE DE DÉMONSTRATION - INTERFACES

## 🎯 Ce qu'il faut montrer au Prof

Vous devez montrer **3 interfaces principales** pour prouver que tout fonctionne :

1. ✅ **Airflow UI** - Orchestration
2. ✅ **MLflow UI** - Tracking
3. ✅ **Django** - Application web

---

## 🚀 PRÉPARATION AVANT LA DÉMO

### 1. Démarrer l'Infrastructure

```powershell
cd C:\Users\yassine\Desktop\PROJET_MLOPS

# Démarrer tous les services
docker-compose up -d

# Attendre 2-3 minutes que tout démarre
```

### 2. Vérifier que tout fonctionne

```powershell
# Vérifier les conteneurs
docker-compose ps

# Devrait afficher :
# - postgres (running)
# - mlflow (running)
# - airflow-webserver (running)
# - airflow-scheduler (running)
```

---

## 1️⃣ AIRFLOW UI - http://localhost:8080

### Accès

1. Ouvrir le navigateur
2. Aller sur : **http://localhost:8080**
3. Login : **airflow**
4. Password : **airflow**

### Ce qu'il faut montrer

#### A. Page d'accueil - Liste des DAGs

**Points à montrer** :
- ✅ DAG `continuous_retraining_pipeline` (votre nouveau DAG)
- ✅ DAG `pneumonia_pipeline_fast` (pipeline optimisé)
- ✅ DAG `pipeline_pneumonia_yassine` (pipeline simple)
- ✅ Toggle ON/OFF pour activer les DAGs
- ✅ Dernière exécution
- ✅ Statut (success/failed)

**Ce que vous dites** :
> "Voici l'interface Airflow. J'ai créé plusieurs DAGs, dont le principal 'continuous_retraining_pipeline' qui s'exécute automatiquement tous les jours pour réentraîner le modèle."

#### B. Vue du DAG (Graph View)

**Comment y accéder** :
1. Cliquer sur `continuous_retraining_pipeline`
2. Cliquer sur l'onglet "Graph"

**Points à montrer** :
- ✅ Workflow visuel du pipeline
- ✅ Tâches : check_data → pull_data → train → compare → deploy
- ✅ Dépendances entre les tâches
- ✅ Statut de chaque tâche (vert = success, rouge = failed)

**Ce que vous dites** :
> "Voici le workflow complet. Le pipeline vérifie d'abord s'il y a de nouvelles données, puis entraîne un nouveau modèle, le compare avec l'ancien, et déploie automatiquement s'il est meilleur."

#### C. Exécuter le DAG (Trigger)

**Comment faire** :
1. Retourner à la liste des DAGs
2. Cliquer sur le bouton "Play" (▶️) à droite de `continuous_retraining_pipeline`
3. Confirmer "Trigger DAG"

**Points à montrer** :
- ✅ Le DAG démarre
- ✅ Aller dans "Graph View"
- ✅ Voir les tâches s'exécuter en temps réel (couleur change)
- ✅ Cliquer sur une tâche → "Log" pour voir les détails

**Ce que vous dites** :
> "Je vais maintenant déclencher manuellement le pipeline. En production, il s'exécute automatiquement tous les jours. Regardez, les tâches s'exécutent dans l'ordre défini."

#### D. Logs d'une Tâche

**Comment faire** :
1. Dans "Graph View", cliquer sur une tâche (ex: `train_new_model`)
2. Cliquer sur "Log"

**Points à montrer** :
- ✅ Logs détaillés de l'exécution
- ✅ Messages de progression
- ✅ Métriques affichées
- ✅ Timestamps

**Ce que vous dites** :
> "Voici les logs détaillés de l'entraînement. On voit toutes les étapes : chargement des données, entraînement, validation, et sauvegarde du modèle dans MLflow."

---

## 2️⃣ MLFLOW UI - http://localhost:5000

### Accès

1. Ouvrir un nouvel onglet
2. Aller sur : **http://localhost:5000**
3. Pas de login requis

### Ce qu'il faut montrer

#### A. Page d'accueil - Experiments

**Points à montrer** :
- ✅ Experiment "pneumonia_detection"
- ✅ Liste des runs (entraînements)
- ✅ Nombre de runs
- ✅ Dernière exécution

**Ce que vous dites** :
> "MLflow tracke automatiquement toutes mes expériences d'entraînement. Chaque run est enregistré avec ses hyperparamètres et ses métriques."

#### B. Liste des Runs

**Comment y accéder** :
1. Cliquer sur "pneumonia_detection"

**Points à montrer** :
- ✅ Tableau avec tous les runs
- ✅ Colonnes : Start Time, Duration, User, Source, Version
- ✅ Métriques : test_accuracy, test_loss, etc.
- ✅ Paramètres : epochs, batch_size, learning_rate

**Ce que vous dites** :
> "Voici tous mes entraînements. Je peux voir les hyperparamètres utilisés et les résultats obtenus pour chaque run."

#### C. Détails d'un Run

**Comment faire** :
1. Cliquer sur un run (une ligne du tableau)

**Points à montrer** :
- ✅ **Parameters** : epochs, batch_size, learning_rate, etc.
- ✅ **Metrics** : test_accuracy, train_loss, precision, recall, F1
- ✅ **Artifacts** : Modèle sauvegardé
- ✅ **Tags** : Informations supplémentaires
- ✅ **Graphiques** : Courbes de métriques

**Ce que vous dites** :
> "Pour ce run, j'ai utilisé 10 epochs, batch size 64, learning rate 0.001, et j'ai obtenu 85% d'accuracy. Le modèle est automatiquement sauvegardé."

#### D. Comparer des Runs

**Comment faire** :
1. Retourner à la liste des runs
2. Cocher 2-3 runs (checkbox à gauche)
3. Cliquer sur "Compare"

**Points à montrer** :
- ✅ Tableau comparatif côte à côte
- ✅ Différences de paramètres
- ✅ Différences de métriques
- ✅ Graphiques de comparaison

**Ce que vous dites** :
> "Je peux facilement comparer plusieurs runs pour voir quel ensemble d'hyperparamètres donne les meilleurs résultats. C'est essentiel pour l'optimisation du modèle."

#### E. Télécharger un Modèle

**Comment faire** :
1. Dans un run, aller dans "Artifacts"
2. Cliquer sur "model"
3. Voir les fichiers du modèle

**Points à montrer** :
- ✅ Fichiers du modèle PyTorch
- ✅ Métadonnées
- ✅ Bouton "Download"

**Ce que vous dites** :
> "Le modèle est sauvegardé avec tous ses fichiers. Je peux le télécharger et le déployer n'importe où."

---

## 3️⃣ DJANGO - http://localhost:8000

### Accès

1. Ouvrir un nouvel onglet
2. Aller sur : **http://localhost:8000**

### Ce qu'il faut montrer

#### A. Page d'Accueil

**Points à montrer** :
- ✅ Design moderne et professionnel
- ✅ Présentation du projet
- ✅ Liste des technologies utilisées
- ✅ Bouton "Commencer l'Analyse"

**Ce que vous dites** :
> "Voici l'interface web de mon application. Elle présente le projet et permet aux utilisateurs d'uploader des radiographies pour analyse."

#### B. Page Upload

**Comment y accéder** :
1. Cliquer sur "Commencer l'Analyse"

**Points à montrer** :
- ✅ Formulaire d'upload
- ✅ Bouton "Choisir un fichier"
- ✅ Bouton "Analyser"
- ✅ Design responsive

**Ce que vous dites** :
> "L'utilisateur peut simplement uploader une radiographie thoracique."

#### C. Faire une Prédiction

**Comment faire** :
1. Cliquer sur "Choisir un fichier"
2. Sélectionner une image de radiographie (ou n'importe quelle image pour la démo)
3. Cliquer sur "Analyser"

**Points à montrer** :
- ✅ Image uploadée affichée
- ✅ Résultat de la prédiction (NORMAL ou PNEUMONIA)
- ✅ Niveau de confiance (%)
- ✅ Barres de progression pour les probabilités
- ✅ Design clair et lisible

**Ce que vous dites** :
> "Le modèle analyse l'image et retourne instantanément le diagnostic : NORMAL ou PNEUMONIA, avec le niveau de confiance. Les probabilités sont affichées visuellement."

---

## 4️⃣ HEROKU (Production)

### Accès

1. Ouvrir un nouvel onglet
2. Aller sur : **https://pneumonia-yassine.herokuapp.com**

### Ce qu'il faut montrer

**Points à montrer** :
- ✅ Même interface que local
- ✅ Application accessible publiquement
- ✅ URL Heroku
- ✅ Fonctionnement identique

**Ce que vous dites** :
> "L'application est déployée en production sur Heroku. Elle est accessible publiquement via cette URL. C'est exactement la même interface, mais hébergée sur le cloud."

---

## 📋 ORDRE DE DÉMONSTRATION RECOMMANDÉ

### Scénario de Présentation (10-15 minutes)

1. **Introduction** (2 min)
   - Expliquer le projet
   - Montrer l'architecture (slide PowerPoint)

2. **Airflow** (4 min)
   - Montrer la liste des DAGs
   - Ouvrir `continuous_retraining_pipeline`
   - Montrer le Graph View
   - Trigger le DAG (si temps)
   - Montrer les logs d'une tâche

3. **MLflow** (3 min)
   - Montrer les experiments
   - Ouvrir un run
   - Montrer les métriques
   - Comparer 2 runs

4. **Django Local** (2 min)
   - Page d'accueil
   - Upload une image
   - Montrer la prédiction

5. **Heroku** (1 min)
   - Montrer l'app en production
   - Expliquer le déploiement

6. **Code** (2 min)
   - Ouvrir `continuous_retraining_dag.py` dans VS Code
   - Montrer le code du workflow

7. **Questions** (2 min)

---

## 💡 CONSEILS POUR LA DÉMO

### Préparation

1. ✅ **Tester avant** : Faire la démo complète une fois avant
2. ✅ **Ouvrir les onglets** : Préparer tous les onglets à l'avance
3. ✅ **Avoir une image** : Préparer une radiographie à uploader
4. ✅ **Vérifier Docker** : S'assurer que tout tourne

### Pendant la Démo

1. ✅ **Parler en montrant** : Expliquer ce que vous faites
2. ✅ **Pointer avec la souris** : Montrer clairement les éléments
3. ✅ **Être confiant** : Vous connaissez votre projet !
4. ✅ **Gérer les erreurs** : Si quelque chose ne marche pas, expliquer pourquoi

### Phrases Clés

- "Voici l'interface Airflow qui orchestre tout le pipeline..."
- "MLflow tracke automatiquement chaque entraînement..."
- "Le continuous retraining s'exécute quotidiennement..."
- "L'application est déployée en production sur Heroku..."
- "Tout est versionné avec Git et DVC pour la reproductibilité..."

---

## 🎬 SCRIPT DE DÉMONSTRATION

### Minute 0-2 : Introduction

> "Bonjour Professeur. Je vais vous présenter mon projet de Continuous Retraining Pipeline pour la détection de pneumonie. Le système est composé de plusieurs interfaces que je vais vous montrer."

### Minute 2-6 : Airflow

> "Commençons par Airflow. [Ouvrir http://localhost:8080] Voici l'interface d'orchestration. J'ai créé plusieurs DAGs, dont le principal 'continuous_retraining_pipeline'. [Cliquer sur le DAG] Voici le workflow complet : vérification des données, entraînement, comparaison, et déploiement automatique. [Montrer Graph View] Tout s'exécute automatiquement tous les jours."

### Minute 6-9 : MLflow

> "Passons à MLflow. [Ouvrir http://localhost:5000] Ici, toutes mes expériences sont trackées automatiquement. [Cliquer sur un run] Pour cet entraînement, voici les hyperparamètres utilisés et les métriques obtenues. [Montrer comparaison] Je peux facilement comparer plusieurs runs pour optimiser le modèle."

### Minute 9-11 : Django

> "Voici l'interface web. [Ouvrir http://localhost:8000] Un utilisateur peut uploader une radiographie. [Upload et analyser] Le modèle retourne instantanément le diagnostic avec le niveau de confiance."

### Minute 11-12 : Heroku

> "L'application est déployée en production sur Heroku. [Ouvrir Heroku URL] Elle est accessible publiquement et fonctionne exactement pareil."

### Minute 12-14 : Code

> "Voici le code du continuous retraining. [Ouvrir VS Code] Le DAG définit tout le workflow : détection, entraînement, comparaison, déploiement."

### Minute 14-15 : Conclusion

> "En résumé, j'ai créé un pipeline MLOps complet avec continuous retraining automatique, tracking complet, et déploiement en production. Tout est reproductible grâce à Git, DVC et Docker."

---

## ✅ CHECKLIST AVANT LA DÉMO

- [ ] Docker démarré (`docker-compose up -d`)
- [ ] Airflow accessible (http://localhost:8080)
- [ ] MLflow accessible (http://localhost:5000)
- [ ] Django accessible (http://localhost:8000)
- [ ] Heroku accessible (URL)
- [ ] Image de radiographie prête
- [ ] VS Code ouvert sur le projet
- [ ] Onglets navigateur préparés
- [ ] Présentation PowerPoint ouverte

---

**Vous êtes prêt pour une démo parfaite ! 🎯🚀**

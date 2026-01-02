---
marp: true
theme: gaia
paginate: true
backgroundColor: #f0f4f8
color: #1a202c
style: |
  section {
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 30px;
    padding: 40px;
  }
  h1 {
    color: #2b6cb0;
    font-size: 60px;
    border-bottom: none;
  }
  h2 {
    color: #4a5568;
  }
  strong {
    color: #2b6cb0;
  }
  code {
    background: #e2e8f0;
    color: #d53f8c;
  }
  .lead {
    background: linear-gradient(135deg, #2b6cb0 0%, #2c5282 100%);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  .lead h1 {
    color: white;
    font-size: 80px;
  }
  .lead h2 {
    color: #bee3f8;
  }
---

<!-- _class: lead -->

# 🚀 MLOps Pipeline
## Continuous Retraining Automation

### Détection de Pneumonie par IA

**Yassine ENNHILI**
Université Cadi Ayyad
31 Décembre 2025

---

# 📋 Notre Mission Aujourd'hui

1.  **Le Défi Médical** : Pourquoi l'IA ?
2.  **La Solution MLOps** : Architecture Système
3.  **Continuous Retraining** : L'Innovation Majeure
4.  **Infrastructure** : Docker, Airflow & MLflow
5.  **Production** : Déploiement Django & Heroku
6.  **Démonstration** & Résultats

---

<div style="display: flex; align-items: center; justify-content: center; height: 100%;">
  <div style="text-align: center;">
    <h1>🚨 Le Problème</h1>
    <br>
    <div style="font-size: 150%;">2.5 Millions</div>
    <div style="color: #718096;">de décès par an dus à la pneumonie</div>
    <br>
    <div style="font-size: 40px;">⏱️ Diagnostic Trop Lent</div>
    <div style="font-size: 40px;">📉 Risque d'Erreur Humaine</div>
  </div>
</div>

---

<!-- _class: lead -->

# 💡 La Solution
## Un Pipeline Intelligent & Autonome

---

# 🏗️ Architecture "State of the Art"

Un écosystème complet pour garantir la **performance** et la **fiabilité**.

| Layer | Technologies | Rôle Project |
| :--- | :--- | :--- |
| **Data** | 🧱 **DVC** | Versioning des radiographies |
| **Code** | 💻 **Git/GitHub** | Versioning du code source |
| **Logic** | 🧠 **PyTorch** | Deep Learning (ResNet18) |
| **Orchestrator** | ⚡ **Airflow** | Automatisation des tâches |
| **Tracker** | 📊 **MLflow** | Suivi des expériences |
| **Deploy** | 🚀 **Heroku** | Mise en production globale |

---

<!-- _backgroundColor: #2d3748 -->
<!-- _color: white -->

# 🔄 THE CORE: Continuous Retraining

C'est **l'innovation centrale** de ce projet.
Le modèle ne vieillit jamais. Il **apprend en continu**.

---

# ⚙️ La Boucle d'Automatisation

Voici comment le système s'améliore tout seul, **chaque jour** :

1.  🔍 **WATCH** : Airflow surveille l'arrivée de nouvelles données.
2.  📥 **INGEST** : DVC télécharge le nouveau dataset sécurisé.
3.  🏋️ **TRAIN** : Lancement automatique du Fine-Tuning sur GPU/CPU.
4.  🧪 **EVALUATE** : Comparaison (New vs Old) via MLflow.
5.  🚀 **DEPLOY** : Si performance >, mise à jour sans interruption.

> *Zéro intervention humaine requise.*

---

# 🧠 Le Cerveau : Airflow DAG

Le chef d'orchestre qui pilote la boucle :

```python
# Extrait du DAG de Production
with DAG('continuous_retraining', schedule='@daily') as dag:
    
    check_data = BranchPythonOperator(task_id='check_new_data')
    
    train_model = PythonOperator(task_id='train_new_model')
    
    compare_models = BranchPythonOperator(task_id='compare_performance')
    
    deploy_prod = PythonOperator(task_id='deploy_to_heroku')

    # Workflow
    check_data >> train_model >> compare_models >> deploy_prod
```

---

# 📊 La Mémoire : MLflow Tracking

Nous ne perdons **aucune** information.

- **Hyperparamètres** : Learning rate, batch size, epochs...
- **Métriques** : Accuracy, Precision, Recall, F1-Score.
- **Artifacts** : Le fichier `.pth` du modèle est versionné.
- **History** : Possibilité de "Rollback" à tout moment.

> *Traçabilité totale de l'IA.*

---

<!-- _class: lead -->

# 🚀 Infrastructure & Déploiement
## De l'Entraînement à la Production

---

# 🐳 Containerisation (Docker)

L'environnement est **isolé** et **reproductible** partout.

- **Service 1 : Postgres** (Database MLOps)
- **Service 2 : MLflow Server** (Artifact Store)
- **Service 3 : Airflow Webserver** (Control Tower)
- **Service 4 : Airflow Scheduler** (The Engine)

*La commande `docker-compose up` suffit à lancer toute l'usine.*

---

# 🌐 Interface Utilisateur (Django)

Pour rendre l'IA accessible aux **médecins**.

- **Design Pro** : Interface épurée et médicale.
- **Upload Sécurisé** : Traitement des images DICOM/JPG.
- **Feedback Immédiat** : Prédiction + Confidence Score.

---

# ☁️ Production (Heroku)

L'application est **LIVE** et accessible dans le monde entier.

<div style="background: #ebf8ff; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #4299e1;">
  <strong>🌐 https://pneumonia-yassine.herokuapp.com</strong>
</div>

<br>

- **Buildpack** : Python 3.10
- **Runner** : Gunicorn (Production WSGI)
- **Scaling** : Prêt pour le passage à l'échelle.

---

<!-- _class: lead -->

# 🔴 DEMO TIME
## Voyons le système en action

---

# 📈 Résultats de Performance

Sur le jeu de test final :

<div style="display: flex; justify-content: space-around;">
  <div style="text-align: center;">
    <h1>90%</h1>
    <p>Accuracy</p>
  </div>
  <div style="text-align: center;">
    <h1>88%</h1>
    <p>Precision</p>
  </div>
  <div style="text-align: center;">
    <h1>92%</h1>
    <p>Recall</p>
  </div>
</div>

*Le Continuous Retraining permet de maintenir ces scores même si les données changent.*

---

# 🏆 Conclusion & Impact

Ce projet dépasse le simple cadre académique :

1.  ✅ **Technologiquement Complet** : MLOps A-to-Z.
2.  ✅ **Médicalement Utile** : Aide au diagnostic rapide.
3.  ✅ **Industriellement Viable** : Architecture scalable et autonome.

**L'IA ne remplace pas le médecin, elle lui donne des super-pouvoirs.**

---

<!-- _class: lead -->

# Merci de votre attention

### Avez-vous des questions ?

**Yassine ENNHILI**
*Projet MLOps 2025*

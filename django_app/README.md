# 🚀 Interface Web Django - Détection de Pneumonie

Application web Django pour la détection de pneumonie sur radiographies thoraciques.

## 📋 Fonctionnalités

- ✅ Upload de radiographies
- ✅ Prédiction en temps réel
- ✅ Interface moderne et responsive
- ✅ Affichage des probabilités
- ✅ Déployable sur Heroku

## 🛠️ Installation Locale

```bash
# Créer environnement virtuel
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Installer dépendances
pip install -r requirements.txt

# Migrations
python manage.py migrate

# Créer superuser (optionnel)
python manage.py createsuperuser

# Lancer serveur
python manage.py runserver
```

Ouvrir : http://localhost:8000

## 🌐 Déploiement Heroku

### Prérequis

1. Compte Heroku : https://signup.heroku.com/
2. Heroku CLI : https://devcenter.heroku.com/articles/heroku-cli

### Étapes

```bash
# 1. Login Heroku
heroku login

# 2. Créer app
heroku create pneumonia-detection-yassine

# 3. Initialiser Git
git init
git add .
git commit -m "Initial commit - Django pneumonia detector"

# 4. Déployer
git push heroku main

# 5. Migrer base de données
heroku run python manage.py migrate

# 6. Ouvrir app
heroku open
```

### Variables d'environnement (Production)

```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY="votre-secret-key-securisee"
heroku config:set ALLOWED_HOSTS="pneumonia-detection-yassine.herokuapp.com"
```

## 📁 Structure

```
django_app/
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── pneumonia_detector/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── detector/
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── templates/
        ├── base.html
        ├── index.html
        ├── upload.html
        └── result.html
```

## 🎯 Utilisation

1. **Accueil** : Présentation du projet
2. **Upload** : Sélectionner une radiographie
3. **Résultat** : Voir la prédiction et les probabilités

## 🔧 Technologies

- **Backend** : Django 4.2
- **Frontend** : HTML/CSS (responsive)
- **ML** : PyTorch (simulation pour démo)
- **Déploiement** : Heroku + Gunicorn + Whitenoise

## 📝 Notes

- Cette version utilise une **simulation** de prédiction pour démo rapide
- En production, charger le vrai modèle depuis MLflow
- Les images uploadées sont stockées dans `/media`

## 🚀 Améliorations Futures

- [ ] Intégration du vrai modèle PyTorch
- [ ] Chargement depuis MLflow
- [ ] API REST avec Django REST Framework
- [ ] Authentification utilisateur
- [ ] Historique des prédictions
- [ ] Export des résultats en PDF

---

**Projet MLOps Complet - Yassine**

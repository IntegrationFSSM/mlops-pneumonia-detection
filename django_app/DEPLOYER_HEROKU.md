# 🚀 DÉPLOIEMENT HEROKU - COMMANDES ÉTAPE PAR ÉTAPE

## ⚠️ IMPORTANT : Redémarrer PowerShell

Après l'installation de Heroku CLI, vous devez **fermer et rouvrir PowerShell**.

---

## 📋 ÉTAPES DE DÉPLOIEMENT

### 1. Ouvrir un NOUVEAU PowerShell

1. Fermer le PowerShell actuel
2. Ouvrir un nouveau PowerShell
3. Aller dans le dossier :

```powershell
cd C:\Users\yassine\Desktop\PROJET_MLOPS\django_app
```

---

### 2. Vérifier Heroku

```powershell
heroku --version
```

**Résultat attendu** : `heroku/8.x.x`

---

### 3. Login Heroku

```powershell
heroku login
```

**Ce qui se passe** :
- Appuyez sur une touche
- Une page web s'ouvre
- Cliquez sur "Log in"
- Retournez au terminal

---

### 4. Créer l'Application

```powershell
heroku create pneumonia-detection-yassine
```

**Si le nom est pris, essayez** :
```powershell
heroku create pneumonia-ml-yassine-2025
```

**Résultat** : URL de votre app (notez-la !)

---

### 5. Configurer les Variables

```powershell
heroku config:set DEBUG=False
heroku config:set SECRET_KEY="pneumonia-secret-2025"
```

---

### 6. Ajouter le Remote Heroku

```powershell
heroku git:remote -a pneumonia-detection-yassine
```

**OU** (si vous avez utilisé un autre nom) :
```powershell
heroku git:remote -a pneumonia-ml-yassine-2025
```

---

### 7. Déployer !

```powershell
git push heroku master
```

**OU** (si vous êtes sur main) :
```powershell
git push heroku main
```

**Temps** : 5-10 minutes (téléchargement des dépendances)

---

### 8. Migrer la Base de Données

```powershell
heroku run python manage.py migrate
```

---

### 9. Ouvrir l'Application

```powershell
heroku open
```

**OU** ouvrir manuellement l'URL notée à l'étape 4

---

## ✅ VÉRIFICATION

Votre application devrait s'ouvrir dans le navigateur !

- Page d'accueil visible ✅
- Upload fonctionne ✅
- Prédiction fonctionne ✅

---

## 🔧 SI PROBLÈME

### Voir les logs

```powershell
heroku logs --tail
```

### Redémarrer

```powershell
heroku restart
```

---

## 📝 RÉSUMÉ DES COMMANDES

```powershell
# Dans un NOUVEAU PowerShell
cd C:\Users\yassine\Desktop\PROJET_MLOPS\django_app

heroku --version
heroku login
heroku create pneumonia-detection-yassine
heroku config:set DEBUG=False
heroku config:set SECRET_KEY="pneumonia-secret-2025"
heroku git:remote -a pneumonia-detection-yassine
git push heroku master
heroku run python manage.py migrate
heroku open
```

---

**Temps total** : 10-15 minutes

**BONNE CHANCE ! 🚀**

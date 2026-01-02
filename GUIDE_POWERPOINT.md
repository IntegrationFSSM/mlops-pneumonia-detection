# 📊 GUIDE : Convertir en PowerPoint

## Fichier Créé

**`PRESENTATION_POWERPOINT.md`** - Présentation complète en format Marp

---

## 🔧 Méthode 1 : Marp (Recommandé)

### Installation

1. **VS Code Extension**
   - Installer "Marp for VS Code"
   - Ouvrir `PRESENTATION_POWERPOINT.md`
   - Cliquer sur "Export Slide Deck"
   - Choisir "PDF" ou "PPTX"

2. **Marp CLI**
```bash
npm install -g @marp-team/marp-cli

# Convertir en PDF
marp PRESENTATION_POWERPOINT.md --pdf

# Convertir en PPTX
marp PRESENTATION_POWERPOINT.md --pptx
```

---

## 🔧 Méthode 2 : Reveal.js (En Ligne)

1. Aller sur : https://slides.com/
2. Créer un compte gratuit
3. Importer le contenu Markdown
4. Exporter en PDF ou PPTX

---

## 🔧 Méthode 3 : Pandoc

```bash
# Installer Pandoc
# Windows: https://pandoc.org/installing.html

# Convertir
pandoc PRESENTATION_POWERPOINT.md -o PRESENTATION.pptx
```

---

## 🔧 Méthode 4 : Copier-Coller dans PowerPoint

1. Ouvrir PowerPoint
2. Créer une nouvelle présentation
3. Copier le contenu de chaque slide (entre les `---`)
4. Coller dans PowerPoint
5. Ajuster le formatage

---

## 📊 Contenu de la Présentation

### 40+ Slides Couvrant :

1. **Introduction** (4 slides)
   - Contexte médical
   - Objectifs

2. **Architecture** (3 slides)
   - Diagramme complet
   - Stack technologique

3. **Modèle ML** (4 slides)
   - ResNet18
   - Dataset
   - Hyperparamètres

4. **Continuous Retraining** (10 slides) ⭐
   - Workflow
   - Code détaillé
   - Chaque étape expliquée

5. **Infrastructure** (4 slides)
   - Docker
   - MLflow
   - Airflow
   - Versioning

6. **Déploiement** (3 slides)
   - Django
   - Heroku

7. **Démo** (2 slides)
   - URLs et accès

8. **Résultats** (2 slides)
   - Métriques
   - Fonctionnalités

9. **Conclusion** (6 slides)
   - Réalisations
   - Compétences
   - Améliorations
   - Impact

---

## 🎨 Personnalisation

### Changer le Thème

```markdown
---
marp: true
theme: gaia  # ou uncover, default
---
```

### Ajouter des Images

```markdown
![bg right:40%](chemin/vers/image.png)
```

### Changer les Couleurs

```markdown
---
backgroundColor: #1a1a1a
color: #ffffff
---
```

---

## ✅ Avantages du Format Marp

- ✅ **Markdown** : Facile à éditer
- ✅ **Versionnable** : Git-friendly
- ✅ **Export** : PDF, PPTX, HTML
- ✅ **Thèmes** : Personnalisables
- ✅ **Code** : Syntax highlighting

---

## 🚀 Utilisation Rapide

### Avec VS Code

1. Installer extension "Marp for VS Code"
2. Ouvrir `PRESENTATION_POWERPOINT.md`
3. Cliquer sur l'icône Marp en haut à droite
4. Prévisualiser les slides
5. Exporter en PPTX

**Temps** : 2 minutes !

---

**Votre présentation PowerPoint est prête ! 📊🎯**

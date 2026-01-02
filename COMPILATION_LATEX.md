# 📄 COMPILATION DES DOCUMENTS LATEX

## Fichiers Créés

1. **RAPPORT_LATEX.tex** : Rapport complet (tutoriel)
2. **PRESENTATION_LATEX.tex** : Présentation Beamer

---

## 🔧 Compilation

### Prérequis

Installer une distribution LaTeX :
- **Windows** : MiKTeX ou TeX Live
- **Mac** : MacTeX
- **Linux** : TeX Live

### Compiler le Rapport

```bash
cd C:\Users\yassine\Desktop\PROJET_MLOPS

# Compilation (3 fois pour les références)
pdflatex RAPPORT_LATEX.tex
pdflatex RAPPORT_LATEX.tex
pdflatex RAPPORT_LATEX.tex
```

**Résultat** : `RAPPORT_LATEX.pdf`

### Compiler la Présentation

```bash
# Compilation
pdflatex PRESENTATION_LATEX.tex
pdflatex PRESENTATION_LATEX.tex
```

**Résultat** : `PRESENTATION_LATEX.pdf`

---

## 📝 Contenu du Rapport

1. Introduction
2. Architecture du Système
3. Installation et Configuration
4. Modèle de Machine Learning
5. Orchestration avec Airflow
6. Tracking avec MLflow
7. Versioning (Git + DVC)
8. Interface Web Django
9. Déploiement sur Heroku
10. Résultats et Performance
11. Guide d'Utilisation
12. Troubleshooting
13. Améliorations Futures
14. Conclusion
15. Annexes

**Total** : ~30 pages

---

## 🎤 Contenu de la Présentation

1. Introduction (contexte, objectifs)
2. Architecture MLOps
3. Modèle ML (ResNet18, dataset)
4. MLOps (Airflow, MLflow, versioning)
5. Déploiement (Django, Heroku)
6. Résultats
7. Démonstration
8. Conclusion

**Total** : ~25 slides

---

## 🌐 Alternative : Overleaf

Si vous n'avez pas LaTeX installé :

1. Aller sur : https://www.overleaf.com/
2. Créer un compte gratuit
3. Créer un nouveau projet
4. Copier le contenu de `RAPPORT_LATEX.tex` ou `PRESENTATION_LATEX.tex`
5. Compiler en ligne
6. Télécharger le PDF

---

## ✅ Avantages LaTeX

- ✅ Rendu professionnel
- ✅ Formules mathématiques
- ✅ Code syntax highlighting
- ✅ Références automatiques
- ✅ Table des matières automatique
- ✅ Format académique standard

---

**Vos documents LaTeX sont prêts ! 📄🎓**

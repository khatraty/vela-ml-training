# 🎓 Formation IA & Machine Learning – SupNum Nouakchott

**Bienvenue dans la formation IA & Machine Learning !**  
*Organisée par Vela Learning et animée par Mohamed Beydia*

---

## 📚 Structure Simple de la Formation

```
AI & Machine Learning/
├── README.md                    # Ce fichier
├── LICENSE                      # Licence MIT  
├── .gitignore                   # Fichiers à ignorer
├── requirements.txt             # Dépendances Python
├── pyproject.toml              # Configuration du projet
├── Makefile                    # Commandes utiles
│
└── notebooks/                  # 📚 SESSIONS DE FORMATION
    ├── session-01/            # Introduction à l'IA et ML
    │   ├── 01_intro_starter.ipynb
    │   ├── 01_intro_solution.ipynb
    │   ├── 01_intro_slides.pdf
    │   └── data/              # Données pour cette session
    │       └── bac-mauritanie-2022-predictive-modeling-challeng.zip
    │
    ├── session-02-supervised-ml-1/  # Supervised ML Part 1: Régression
    │   ├── 02_supervised_ml_1_complete.ipynb
    │   ├── 02_regression_slides.pdf
    │   └── data/              # Données pour cette session
    │
    ├── session-03-supervised-ml-2/  # Supervised ML Part 2: Classification
    │   ├── 03_supervised_ml_2_starter.ipynb
    │   └── data/              # Données pour cette session
    ├── session-04/            # Clustering et Segmentation
    │   └── data/
    ├── session-05/            # Détection d'anomalies
    │   └── data/
    ├── session-06/            # Workflow ML & MLOps
    │   └── data/
    ├── session-07/            # Deep Learning
    │   └── data/
    ├── session-08/            # NLP et Traitement du langage
    │   └── data/
    ├── session-09/            # IA Générative & LLMs
    │   └── data/
    └── session-10/            # Capstone Project
        └── data/
```

---

## 🚀 Démarrage Rapide

### 1. Installation de l'environnement

```bash
# Cloner ou télécharger le projet
# Installer les dépendances
pip install -r requirements.txt

# Ou utiliser le Makefile
make install
```

### 2. Lancer Jupyter Lab

```bash
# Démarrer Jupyter
jupyter lab

# Ou utiliser le Makefile
make run-notebooks
```

### 3. Commencer par la Session 1

1. 📂 Allez dans `notebooks/session-01/`
2. 🚀 Ouvrez `01_intro_starter.ipynb` pour commencer
3. 📊 Les données sont dans le dossier `data/` de chaque session

---

## 📋 Plan de la Formation (10 sessions - 20h)

| Session | Sujet | Durée | Objectifs |
|---------|-------|-------|-----------|
| **01** | Introduction à l'IA et ML | 2h | Concepts de base, cas pratique BAC Mauritanie |
| **02** | Supervised ML 1: Régression | 2h | Régression linéaire, Ridge/Lasso, métriques + intro classification |
| **03** | Supervised ML 2: Classification | 2h | Logistic Regression, Decision Trees, Random Forest |
| **04** | Clustering et Segmentation | 2h | K-means, PCA, segmentation clients |
| **05** | Détection d'Anomalies | 2h | Isolation Forest, détection de fraude |
| **06** | Workflow ML & MLOps | 2h | Pipeline ML, versioning, CI/CD |
| **07** | Deep Learning | 2h | CNN, classification d'images |
| **08** | NLP | 2h | TF-IDF, analyse de sentiments |
| **09** | IA Générative & LLMs | 2h | GPT, prompt engineering, chatbot |
| **10** | Capstone Project | 2h | Projet final de synthèse |

---

## 💡 Comment Naviguer

### 🎯 Pour chaque session :

1. **Starter Notebook** : Point de départ avec exercices à compléter
2. **Solution Notebook** : Version corrigée avec explications
3. **Slides PDF** : Support de présentation
4. **Dossier data/** : Toutes les données nécessaires pour la session

### 🛠️ Commandes Utiles

```bash
# Installation complète
make install

# Lancer Jupyter Lab
make run-notebooks

# Formater le code
make format

# Lancer les tests
make test

# Nettoyer les fichiers temporaires
make clean
```

---

## 🎯 Objectifs Pédagogiques

À la fin de cette formation, vous saurez :

- 🤖 **Comprendre** les concepts fondamentaux de l'IA et du ML
- 📊 **Analyser** des données avec Python (pandas, matplotlib)
- 🧠 **Construire** des modèles ML supervisés et non-supervisés
- 📈 **Évaluer** la performance des modèles
- 🚀 **Déployer** des applications ML simples
- 💻 **Utiliser** les outils modernes (scikit-learn, TensorFlow)
- 🎯 **Appliquer** le ML à des cas d'usage concrets africains

---

## 📞 Support et Contact

- **👨‍🏫 Formateur** : Mohamed Beydia
- **📧 Email** : mohamed.beydia@vela-learning.com
- **🌐 Vela Learning** : [vela-learning.com](https://vela-learning.com)
- **🏫 Institution** : SupNum Nouakchott

---

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

**🎉 Bonne formation et amusez-vous bien avec l'IA ! 🎉**

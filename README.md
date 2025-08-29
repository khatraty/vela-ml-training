# 🎓 Formation IA & Machine Learning – SupNum Nouakchott

**Bienvenue dans la formation IA & Machine Learning !**  
*Organisée par Vela Learning et animée par Mohamed Beydia*

---

## 🚀 Démarrage Rapide

### Étape 1 : Obtenir le Code Source

**🔗 Option 1 : Cloner avec Git (Recommandé)**
```bash
git clone https://github.com/mlemineb/vela-ml-training.git
cd vela-ml-training
```

**📦 Option 2 : Télécharger le ZIP**
1. Aller sur [github.com/mlemineb/vela-ml-training](https://github.com/mlemineb/vela-ml-training)
2. Cliquer sur le bouton vert **"Code"**
3. Sélectionner **"Download ZIP"**
4. Extraire le fichier ZIP dans votre dossier de travail
5. Ouvrir le dossier extrait

### Étape 2 : Choisir Votre Environnement de Travail

Vous avez **3 options** pour suivre cette formation :

#### 🖥️ **Option A : Travail Local avec VS Code**

1. **Installer Python** (version 3.8 ou plus récente)
2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
3. **Ouvrir avec VS Code** :
   ```bash
   code .
   ```
4. **Installer l'extension** `Jupyter` dans VS Code
5. **Commencer** par ouvrir `notebooks/session-01/01_intro_starter.ipynb`

#### 📓 **Option B : Travail Local avec Jupyter Notebook**

1. **Installer Python** (version 3.8 ou plus récente)
2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
3. **Lancer Jupyter Lab** :
   ```bash
   jupyter lab
   ```
4. **Naviguer** vers `notebooks/session-01/` et ouvrir `01_intro_starter.ipynb`

#### ☁️ **Option C : Google Colab (Recommandé pour débuter)**

1. **Accéder à Google Colab** : [colab.research.google.com](https://colab.research.google.com)
2. **Se connecter** avec votre compte Google
3. **Importer depuis GitHub** :
   - Cliquer sur "File" → "Open notebook"
   - Sélectionner l'onglet "GitHub"
   - Coller l'URL : `https://github.com/mlemineb/vela-ml-training`
   - Choisir le notebook à ouvrir (commencer par `notebooks/session-01/01_intro_starter.ipynb`)

4. **Configuration Colab** (à faire au début de chaque notebook) :
   ```python
   # Cloner le repo (uniquement si nécessaire)
   !git clone https://github.com/mlemineb/vela-ml-training.git
   
   # Naviguer vers le dossier
   import os
   os.chdir('vela-ml-training')
   
   # Installer les dépendances
   !pip install -r requirements.txt
   ```

**💡 Avantages de Google Colab :**
- ✅ Pas d'installation requise sur votre ordinateur
- ✅ GPU/TPU gratuits disponibles
- ✅ Environnement Python préconfiguré
- ✅ Sauvegarde automatique dans Google Drive
- ✅ Collaboration facile avec d'autres étudiants

---

## 📚 Structure de la Formation

```
AI & Machine Learning/
├── README.md                    # Ce fichier
├── 00_setup_guide.md            # Guide pour congigurer VS code et Github
├── LICENSE                      # Licence MIT  
├── .gitignore                   # Fichiers à ignorer
├── requirements.txt             # Dépendances Python
│
└── notebooks/                  # 📚 SESSIONS DE FORMATION
    ├── session-01/            # Introduction à l'IA et ML
    │   ├── 01_intro_starter.ipynb
    │   ├── 01_intro_solution.ipynb
    │   ├── 01_intro_slides.pdf
    │   └── data/              # Données pour cette session
    │
    ├── session-02-supervised-ml-1/  # Supervised ML Part 1: Régression
    │   ├── 02_supervised_ml_1_complete.ipynb
    │   ├── 02_regression_slides.pdf
    │   └── data/
    │
    ├── session-03-supervised-ml-2/  # Supervised ML Part 2: Classification
    │   ├── 03_supervised_ml_2_starter.ipynb
    │   └── data/
    │
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
2. **Solution Notebook** : Version corrigée avec explications détaillées
3. **Slides PDF** : Support de présentation théorique
4. **Dossier data/** : Toutes les données nécessaires pour la session

### 📝 Conseils pour Google Colab :

- **Sauvegarde** : Vos notebooks modifiés seront sauvés dans votre Google Drive
- **Runtime** : Si votre session expire, relancez les cellules d'installation
- **GPU** : Activez le GPU gratuit via "Runtime" → "Change runtime type" → "Hardware accelerator" → "GPU"
- **Fichiers** : Utilisez le panneau de gauche pour explorer les fichiers du projet

---

## 🎯 Objectifs Pédagogiques

À la fin de cette formation, vous saurez :

- 🤖 **Comprendre** les concepts fondamentaux de l'IA et du ML
- 📊 **Analyser** des données avec Python (pandas, matplotlib, seaborn)
- 🧠 **Construire** des modèles ML supervisés et non-supervisés
- 📈 **Évaluer** la performance des modèles avec des métriques appropriées
- 🚀 **Déployer** des applications ML simples
- 💻 **Utiliser** les outils modernes (scikit-learn, TensorFlow, pandas)
- 🎯 **Appliquer** le ML à des cas d'usage concrets africains
- 🛠️ **Maîtriser** les environnements de développement (VS Code, Jupyter, Colab)

---

## 🆘 Support Technique

### Problèmes Courants et Solutions

1. **Erreur d'importation de modules** :
   ```python
   !pip install --upgrade package-name
   ```

2. **Mémoire insuffisante sur Colab** :
   - Redémarrer le runtime : "Runtime" → "Restart runtime"
   - Utiliser des échantillons de données plus petits

3. **Fichiers non trouvés** :
   - Vérifier que vous êtes dans le bon répertoire
   - Re-cloner le repository si nécessaire

---

## 📞 Contact et Support

- **👨‍🏫 Formateur** : Mohamed Beydia
- **📧 Email** : mohamed.beydia@gmail.com
- **🌐 Vela Learning** : [vela-learning.com](https://vela-learning.com)
- **🏫 Institution** : SupNum Nouakchott
- **💻 Repository** : [github.com/mlemineb/vela-ml-training](https://github.com/mlemineb/vela-ml-training)

---

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

**🎉 Bonne formation et amusez-vous bien avec l'IA ! 🎉**

*Dernière mise à jour : Août 2025*
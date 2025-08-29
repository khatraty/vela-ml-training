# 🚀 Guide de Configuration - Formation IA & ML

**Formation IA & ML - SupNum Nouakchott**  
**Formateur:** Mohamed Beydia - Vela Learning

---

## 📋 Vue d'ensemble

Ce guide vous accompagne dans la configuration de votre environnement de développement pour suivre la formation IA & ML. Vous apprendrez à :

1. **Installer Visual Studio Code** (éditeur de code)
2. **Créer un compte GitHub** (plateforme de collaboration)
3. **Cloner et utiliser le repository du cours** 
4. **Configurer Python et les extensions nécessaires**

⏱️ **Temps estimé :** 30-45 minutes

---

## 🖥️ ÉTAPE 1: Installation de Visual Studio Code

### 📥 Téléchargement et Installation

**1. Télécharger VS Code**
- Rendez-vous sur : https://code.visualstudio.com/
- Cliquez sur **"Download for Windows"** (ou votre OS)
- Téléchargez le fichier d'installation

**2. Installation**
- Exécutez le fichier téléchargé
- Suivez l'assistant d'installation
- ✅ **Important :** Cochez "Add to PATH" lors de l'installation
- ✅ Cochez "Create a desktop icon" si souhaité

**3. Premier lancement**
- Ouvrez VS Code
- Vous devriez voir l'écran de bienvenue

### 🔧 Extensions Essentielles

Installez ces extensions pour Python et Jupyter :

**1. Extension Python**
- Ouvrez VS Code
- Cliquez sur l'icône Extensions (carré avec 4 carrés) dans la barre latérale
- Recherchez "Python" 
- Installez l'extension officielle de Microsoft

**2. Extension Jupyter**
- Recherchez "Jupyter"
- Installez "Jupyter" par Microsoft
- Cela inclut le support des notebooks

**3. Extensions recommandées**
- **GitLens** : Meilleure intégration Git
- **Python Docstring Generator** : Génération automatique de docstrings
- **autoDocstring** : Documentation automatique

---

## 🐙 ÉTAPE 2: Création d'un Compte GitHub

### 📝 Inscription

**1. Aller sur GitHub**
- Rendez-vous sur : https://github.com/
- Cliquez sur **"Sign up"**

**2. Créer votre compte**
- **Username** : Choisissez un nom professionnel (ex: `prenom.nom` ou `prenomnom`)
- **Email** : Utilisez votre email personnel ou professionnel
- **Password** : Mot de passe fort (8+ caractères, majuscules, chiffres, symboles)

**3. Vérification**
- Vérifiez votre email
- Complétez le processus de vérification

**4. Configuration du profil**
- Ajoutez une photo de profil
- Complétez votre bio
- Indiquez votre localisation (Nouakchott, Mauritanie)

### 🔐 Configuration Git (Optionnel mais Recommandé)

Si vous voulez contribuer ou faire des modifications :

**1. Installer Git**
- Téléchargez Git depuis : https://git-scm.com/
- Installez avec les options par défaut

**2. Configuration initiale**
```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
```

---

## 📚 ÉTAPE 3: Utilisation du Repository du Cours

### 🔗 Repository du Cours

**URL :** https://github.com/mlemineb/vela-ml-training

Ce repository contient :
- 📓 **Notebooks de cours** (théorie et pratique)
- 💻 **Exercices pratiques** avec corrections
- 📊 **Datasets** pour les projets
- 📖 **Documentation** et guides

### 📥 Méthode 1: Téléchargement Direct (Recommandé pour Débutants)

**1. Télécharger le ZIP**
- Allez sur : https://github.com/mlemineb/vela-ml-training
- Cliquez sur le bouton vert **"Code"**
- Sélectionnez **"Download ZIP"**

**2. Extraire les fichiers**
- Téléchargez le fichier ZIP
- Extrayez-le dans un dossier de votre choix (ex: `C:\Formation-ML\`)
- Renommez le dossier en `vela-ml-training`

**3. Ouvrir dans VS Code**
- Ouvrez VS Code
- Menu **File > Open Folder**
- Sélectionnez le dossier `vela-ml-training`

### 🔄 Méthode 2: Clonage Git (Pour Utilisateurs Avancés)

**1. Cloner le repository**
```bash
git clone https://github.com/mlemineb/vela-ml-training.git
cd vela-ml-training
```

**2. Ouvrir dans VS Code**
```bash
code .
```

### 🔄 Mise à Jour du Contenu

**Pour la méthode ZIP :**
- Re-téléchargez le ZIP périodiquement
- Remplacez les anciens fichiers

**Pour la méthode Git :**
```bash
git pull origin main
```

---

## 🐍 ÉTAPE 4: Configuration Python

### 📦 Installation de Python

**1. Télécharger Python**
- Allez sur : https://www.python.org/downloads/
- Téléchargez Python 3.9+ (version recommandée : 3.10 ou 3.11)

**2. Installation**
- ✅ **IMPORTANT :** Cochez "Add Python to PATH"
- Choisissez "Install Now"

**3. Vérification**
- Ouvrez le terminal (CMD ou PowerShell)
- Tapez : `python --version`
- Vous devriez voir la version installée

### 📚 Installation des Bibliothèques

**1. Ouvrir le terminal dans VS Code**
- Dans VS Code : Menu **Terminal > New Terminal**

**2. Installer les packages essentiels**
```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

**3. Packages supplémentaires**
```bash
pip install jupytext plotly ipywidgets
```

**4. Vérification**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("✅ Toutes les bibliothèques sont installées !")
```

---

## 🎯 ÉTAPE 5: Test de Configuration

### 📓 Ouvrir un Notebook de Test

**1. Dans VS Code**
- Ouvrez le dossier du cours
- Naviguez vers `notebooks/session-01/`
- Ouvrez un fichier `.ipynb`

**2. Sélectionner l'interpréteur Python**
- VS Code devrait automatiquement détecter Python
- Si demandé, sélectionnez votre installation Python

**3. Exécuter une cellule**
- Cliquez sur une cellule de code
- Appuyez sur **Shift + Enter** pour l'exécuter
- Vous devriez voir le résultat s'afficher

### ✅ Checklist de Vérification

- [ ] VS Code installé et fonctionnel
- [ ] Extensions Python et Jupyter installées
- [ ] Compte GitHub créé
- [ ] Repository du cours téléchargé/cloné
- [ ] Python installé avec PATH configuré
- [ ] Bibliothèques essentielles installées
- [ ] Notebook de test exécuté avec succès

---

## 🆘 Résolution de Problèmes Courants

### ❌ Python non reconnu

**Problème :** `python` n'est pas reconnu comme commande
**Solution :**
1. Réinstallez Python en cochant "Add to PATH"
2. Ou ajoutez manuellement Python au PATH système

### ❌ Kernel non trouvé dans Jupyter

**Problème :** Jupyter ne trouve pas l'interpréteur Python
**Solution :**
1. Dans VS Code : **Ctrl+Shift+P**
2. Tapez "Python: Select Interpreter"
3. Sélectionnez votre installation Python

### ❌ Erreur d'importation de modules

**Problème :** `ModuleNotFoundError`
**Solution :**
```bash
pip install --upgrade pip
pip install nom_du_module
```

### ❌ VS Code lent ou qui plante

**Solution :**
1. Fermez les onglets inutiles
2. Redémarrez VS Code
3. Vérifiez la RAM disponible

---

## 📞 Support et Ressources

### 🔗 Liens Utiles

- **VS Code Documentation :** https://code.visualstudio.com/docs
- **GitHub Guides :** https://guides.github.com/
- **Python Documentation :** https://docs.python.org/3/
- **Jupyter Documentation :** https://jupyter.org/documentation

### 📧 Contact

**Formateur :** Mohamed Beydia  
**Email :** [Votre email de contact]  
**Repository du cours :** https://github.com/mlemineb/vela-ml-training

### 💬 Communauté

- Posez vos questions pendant les sessions
- Utilisez les Issues GitHub pour signaler des problèmes
- Partagez vos solutions avec la classe

---

## 🎉 Félicitations !

Vous avez maintenant un environnement de développement complet pour suivre la formation IA & ML !

**Prochaines étapes :**
1. 📚 Explorez les notebooks du cours
2. 💻 Commencez par la Session 1
3. 🤝 Rejoignez les sessions pratiques
4. 🚀 Lancez-vous dans vos premiers projets ML !

**Bon apprentissage ! 🎓**

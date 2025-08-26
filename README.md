# 🎓 Formation IA & Machine Learning – SupNum Nouakchott

Bienvenue dans le dépôt officiel de la **formation IA & Machine Learning** organisée par **Vela Learning** et animée par **Mohamed Beydia**.  
Ce repo contient l’ensemble des supports, notebooks, datasets et ressources nécessaires pour suivre la formation.

---

## 📚 Plan de la formation (10 cours – 20h)

### **Cours 1 – Introduction à l’IA et au Machine Learning**
- Définitions : IA, ML, Deep Learning
- IA symbolique vs statistique
- IA analytique vs générative
- Les grandes familles du ML (supervisé, non supervisé, renforcement)
- Workflow ML
- Cas d’usage (éducation, business, santé)

### **Cours 2 – Régression et Prédiction**
- Régression linéaire & polynomiale
- Regularisation (Ridge, Lasso)
- Évaluation (RMSE, MAE, R²)
- Cas pratique : prédiction numérique (notes, prix, ventes)

### **Cours 3 – Classification**
- Logistic Regression
- Decision Trees & Random Forests
- Évaluation (accuracy, precision, recall, F1-score)
- Cas pratique : churn prediction / détection de spam

### **Cours 4 – Clustering et Segmentation**
- K-means, DBSCAN, clustering hiérarchique
- Réduction de dimension (PCA)
- Cas pratique : segmentation clients / regroupement étudiants

### **Cours 5 – Détection d’anomalies**
- Isolation Forest, One-Class SVM, Local Outlier Factor
- Cas pratique : détection de fraude ou décrochage étudiant

### **Cours 6 – Workflow ML & MLOps (CI/CD Basics)**
- Pipeline ML (préparation → entraînement → évaluation → déploiement)
- GitHub & versioning
- Notebooks paramétrés
- Introduction au CI/CD pour ML

### **Cours 7 – Réseaux de Neurones & Deep Learning**
- Perceptron, couches cachées, fonctions d’activation
- CNN pour les images
- Cas pratique : classification d’images (MNIST ou CIFAR-10)

### **Cours 8 – NLP et Traitement du langage**
- TF-IDF, Bag-of-words
- Word embeddings (Word2Vec, GloVe)
- Classification de texte (sentiment analysis, spam)
- Cas pratique : analyse de sentiments sur des avis

### **Cours 9 – IA Générative & LLMs**
- GANs, Diffusion, LLMs
- Fonctionnement des Transformers
- Prompt engineering
- Cas pratique : mini chatbot avec API (OpenAI, Hugging Face)

### **Cours 10 – Capstone Project**
- Projet de synthèse end-to-end
- Choix libre (churn, segmentation, NLP, chatbot…)
- Présentation & restitution finale

---

## 🗂️ Organisation du dépôt

ai-ml-training-supnum/
├─ notebooks/ # Notebooks par session
│ ├─ session-01_intro/
│ │ ├─ starter.ipynb
│ │ └─ solution.ipynb
│ ├─ session-02_regression/
│ ├─ ...
│ └─ session-10_capstone/
│
├─ modules/ # Notebooks regroupés par thématique (supervised, unsupervised, NLP, etc.)
├─ data/ # Jeux de données (petits fichiers + liens externes)
│ ├─ raw/
│ ├─ processed/
│ └─ external/
├─ deployments/ # Déploiements Streamlit, FastAPI, Hugging Face
├─ scripts/ # Scripts Python (train, evaluate, download_data)
├─ tests/ # Tests unitaires
├─ resources/ # Lectures, cheat-sheets, slides templates
└─ README.md # Ce fichier



---

## ⚙️ Installation

Clonez le repo et installez les dépendances :

```bash
git clone https://github.com/[username]/ai-ml-training-supnum.git
cd ai-ml-training-supnum
pip install -r requirements.txt

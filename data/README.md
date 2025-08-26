# Dossier Data

Ce dossier contient les jeux de données utilisés dans la formation.

## Structure

- `raw/` : Données brutes, non modifiées
- `processed/` : Données nettoyées et préparées pour l'entraînement  
- `external/` : Liens vers des datasets externes

## Datasets utilisés dans la formation

### Session 2 - Régression
- Prix immobilier
- Données de ventes

### Session 3 - Classification  
- Dataset Iris
- Données de churn clients
- Détection de spam

### Session 4 - Clustering
- Données clients pour segmentation
- Données étudiants

### Session 5 - Détection d'anomalies
- Transactions financières
- Logs système

### Session 7 - Deep Learning
- MNIST (chiffres manuscrits)
- CIFAR-10 (images)

### Session 8 - NLP
- Reviews Amazon
- Tweets sentiment analysis

## Comment utiliser les datasets

```python
import pandas as pd

# Charger un dataset
df = pd.read_csv('data/processed/housing_clean.csv')

# Ou utiliser les utilitaires du projet
from src.data.loader import load_dataset
df = load_dataset('housing')
```

## Sources externes

Consultez `external/links.md` pour les liens vers les datasets volumineux stockés en externe.

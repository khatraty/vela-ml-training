# Datasets Externes

Cette page contient les liens vers les datasets volumineux hébergés en externe.

## 📊 Datasets par session

### Session 2 - Régression
- **Boston Housing** : https://www.kaggle.com/c/boston-housing
- **California Housing** : https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset
- **Automotive** : https://archive.ics.uci.edu/ml/datasets/automobile

### Session 3 - Classification
- **Titanic** : https://www.kaggle.com/c/titanic
- **Iris Dataset** : https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
- **Wine Dataset** : https://archive.ics.uci.edu/ml/datasets/wine

### Session 4 - Clustering
- **Mall Customers** : https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python
- **Wholesale Customers** : https://archive.ics.uci.edu/ml/datasets/wholesale+customers

### Session 5 - Détection d'anomalies
- **Credit Card Fraud** : https://www.kaggle.com/mlg-ulb/creditcardfraud
- **KDD Cup 99** : http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

### Session 7 - Deep Learning
- **MNIST** : http://yann.lecun.com/exdb/mnist/
- **CIFAR-10** : https://www.cs.toronto.edu/~kriz/cifar.html
- **Fashion-MNIST** : https://github.com/zalandoresearch/fashion-mnist

### Session 8 - NLP
- **IMDB Reviews** : https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
- **Amazon Reviews** : https://www.kaggle.com/bittlingmayer/amazonreviews
- **Twitter Sentiment** : https://www.kaggle.com/kazanova/sentiment140

## 🔧 Scripts de téléchargement

Utilisez les scripts dans `/scripts/` pour télécharger automatiquement les datasets :

```bash
python scripts/download_data.py --dataset housing
python scripts/download_data.py --all
```

## 📝 Notes importantes

- Certains datasets nécessitent une inscription (Kaggle)
- Respectez les licences et conditions d'utilisation
- Les datasets volumineux (>100MB) ne sont pas stockés dans le repo
- Utilisez les versions pré-traitées quand elles sont disponibles

## 🆔 Credentials requis

Pour télécharger certains datasets, vous aurez besoin de :

- **Kaggle API Token** : `~/.kaggle/kaggle.json`
- **Hugging Face Token** : pour certains datasets NLP
- **OpenML API Key** : pour les datasets OpenML

Consultez la documentation dans `/docs/setup.md` pour plus d'informations.

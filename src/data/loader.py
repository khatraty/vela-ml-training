"""
Data Loading Utilities

Ce module contient des fonctions pour charger les différents datasets
utilisés dans la formation.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Union, Tuple, Optional
import urllib.request
import os

# Chemin vers le dossier data
DATA_DIR = Path(__file__).parent.parent.parent / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


def load_dataset(name: str, processed: bool = True) -> pd.DataFrame:
    """
    Charge un dataset par son nom.
    
    Args:
        name: Nom du dataset (ex: 'housing', 'iris', 'titanic')
        processed: Si True, charge la version traitée, sinon la version brute
        
    Returns:
        DataFrame pandas avec les données
    """
    data_dir = PROCESSED_DATA_DIR if processed else RAW_DATA_DIR
    
    dataset_files = {
        'housing': 'housing.csv',
        'iris': 'iris.csv',
        'titanic': 'titanic.csv',
        'wine': 'wine.csv',
        'customers': 'customers.csv',
        'fraud': 'fraud.csv',
        'reviews': 'reviews.csv'
    }
    
    if name not in dataset_files:
        raise ValueError(f"Dataset '{name}' non reconnu. Datasets disponibles: {list(dataset_files.keys())}")
    
    file_path = data_dir / dataset_files[name]
    
    if not file_path.exists():
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas. Utilisez download_data.py pour le télécharger.")
    
    return pd.read_csv(file_path)


def load_train_test_split(name: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Charge les datasets d'entraînement et de test.
    
    Args:
        name: Nom du dataset
        
    Returns:
        Tuple (train_df, test_df)
    """
    train_path = PROCESSED_DATA_DIR / f"{name}_train.csv"
    test_path = PROCESSED_DATA_DIR / f"{name}_test.csv"
    
    if not train_path.exists() or not test_path.exists():
        raise FileNotFoundError(f"Les fichiers train/test pour '{name}' n'existent pas.")
    
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    
    return train_df, test_df


def download_sample_data():
    """
    Télécharge quelques datasets d'exemple pour commencer rapidement.
    """
    from sklearn.datasets import load_iris, load_wine, load_boston
    import seaborn as sns
    
    # Créer les dossiers si nécessaires
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Dataset Iris
    iris = load_iris()
    iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
    iris_df['target'] = iris.target
    iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    iris_df.to_csv(PROCESSED_DATA_DIR / 'iris.csv', index=False)
    
    # Dataset Wine
    wine = load_wine()
    wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
    wine_df['target'] = wine.target
    wine_df.to_csv(PROCESSED_DATA_DIR / 'wine.csv', index=False)
    
    # Dataset tips de Seaborn
    tips = sns.load_dataset('tips')
    tips.to_csv(PROCESSED_DATA_DIR / 'tips.csv', index=False)
    
    print("✅ Datasets d'exemple téléchargés avec succès!")


def get_dataset_info(name: str) -> dict:
    """
    Retourne des informations sur un dataset.
    
    Args:
        name: Nom du dataset
        
    Returns:
        Dictionnaire avec les infos du dataset
    """
    dataset_info = {
        'housing': {
            'description': 'Prix immobilier en Californie',
            'target': 'price',
            'type': 'regression',
            'size': '20640 lignes, 9 colonnes'
        },
        'iris': {
            'description': 'Classification des fleurs Iris',
            'target': 'species',
            'type': 'classification',
            'size': '150 lignes, 5 colonnes'
        },
        'titanic': {
            'description': 'Survie des passagers du Titanic',
            'target': 'survived',
            'type': 'classification',
            'size': '891 lignes, 12 colonnes'
        }
    }
    
    return dataset_info.get(name, {'description': 'Information non disponible'})


def list_available_datasets() -> list:
    """
    Liste tous les datasets disponibles.
    
    Returns:
        Liste des noms de datasets disponibles
    """
    processed_files = list(PROCESSED_DATA_DIR.glob('*.csv'))
    return [f.stem for f in processed_files if not f.stem.endswith(('_train', '_test'))]


if __name__ == "__main__":
    # Test des fonctions
    download_sample_data()
    print("Datasets disponibles:", list_available_datasets())

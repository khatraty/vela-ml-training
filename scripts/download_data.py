"""
Script pour télécharger les datasets utilisés dans la formation
"""

import argparse
import os
import urllib.request
import pandas as pd
from pathlib import Path
import sys

# Ajouter le dossier src au PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent / "src"))

from src.data.loader import download_sample_data, DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR


def download_housing_data():
    """Télécharge le dataset California Housing"""
    from sklearn.datasets import fetch_california_housing
    
    print("📊 Téléchargement du dataset California Housing...")
    housing = fetch_california_housing(as_frame=True)
    
    # Sauvegarder les données
    housing_df = housing.frame
    housing_df.to_csv(RAW_DATA_DIR / 'housing_raw.csv', index=False)
    
    # Version nettoyée
    housing_clean = housing_df.copy()
    housing_clean.columns = [col.lower().replace(' ', '_') for col in housing_clean.columns]
    housing_clean.to_csv(PROCESSED_DATA_DIR / 'housing.csv', index=False)
    
    print("✅ Dataset Housing téléchargé et traité!")


def download_titanic_data():
    """Télécharge le dataset Titanic depuis Seaborn"""
    import seaborn as sns
    
    print("🚢 Téléchargement du dataset Titanic...")
    titanic = sns.load_dataset('titanic')
    
    # Sauvegarder
    titanic.to_csv(RAW_DATA_DIR / 'titanic_raw.csv', index=False)
    
    # Version nettoyée
    titanic_clean = titanic.copy()
    # Nettoyage basique
    titanic_clean = titanic_clean.dropna(subset=['embarked'])
    titanic_clean['age'].fillna(titanic_clean['age'].median(), inplace=True)
    titanic_clean.to_csv(PROCESSED_DATA_DIR / 'titanic.csv', index=False)
    
    print("✅ Dataset Titanic téléchargé et traité!")


def download_all_datasets():
    """Télécharge tous les datasets essentiels"""
    # Créer les dossiers
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    print("🚀 Téléchargement de tous les datasets...")
    
    # Datasets de base
    download_sample_data()
    
    # Datasets spécifiques
    download_housing_data()
    download_titanic_data()
    
    print("\n✅ Tous les datasets ont été téléchargés!")
    print(f"📁 Données stockées dans: {DATA_DIR}")


def main():
    parser = argparse.ArgumentParser(description='Téléchargeur de datasets pour la formation IA/ML')
    parser.add_argument('--dataset', type=str, help='Nom du dataset à télécharger (housing, titanic, all)')
    parser.add_argument('--all', action='store_true', help='Télécharger tous les datasets')
    
    args = parser.parse_args()
    
    if args.all or args.dataset == 'all':
        download_all_datasets()
    elif args.dataset == 'housing':
        download_housing_data()
    elif args.dataset == 'titanic':
        download_titanic_data()
    elif args.dataset == 'samples':
        download_sample_data()
    else:
        print("Usage: python download_data.py --all ou --dataset [housing|titanic|samples]")
        print("\nDatasets disponibles:")
        print("  - housing: California Housing Dataset")
        print("  - titanic: Titanic Survival Dataset") 
        print("  - samples: Iris, Wine, Tips (datasets d'exemple)")
        print("  - all: Tous les datasets ci-dessus")


if __name__ == "__main__":
    main()

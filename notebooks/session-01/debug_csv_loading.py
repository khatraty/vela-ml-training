# Extraction et chargement des données BAC Mauritanie - VERSION CORRIGÉE
import os
import pandas as pd

# Chemin vers le fichier zip (dans le dossier data/ de cette session)
zip_path = "data/bac-mauritanie-2022-predictive-modeling-challeng.zip"
extract_path = "data/extracted/"

# Créer le dossier d'extraction s'il n'existe pas
os.makedirs(extract_path, exist_ok=True)

# Extraire les données
try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print("✅ Données extraites avec succès !")
    
    # Lister les fichiers extraits
    files = os.listdir(extract_path)
    print("📁 Fichiers disponibles:")
    for file in files:
        print(f"  - {file}")
        
except Exception as e:
    print(f"❌ Erreur lors de l'extraction: {e}")
    print("Vérifiez que le fichier zip existe dans data/")

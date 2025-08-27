# 🔧 CHARGEMENT ROBUSTE DES DONNÉES CSV
def load_csv_robust(file_path, encoding_attempts=['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']):
    """
    Charge un fichier CSV de manière robuste avec gestion des erreurs
    """
    for encoding in encoding_attempts:
        try:
            # Essayer différents paramètres pour gérer les erreurs de parsing
            df = pd.read_csv(file_path, 
                           encoding=encoding,
                           sep=',',
                           quotechar='"',
                           escapechar='\\',
                           on_bad_lines='skip',  # Ignorer les lignes problématiques
                           engine='python')     # Utiliser le moteur Python plus robuste
            print(f"✅ Fichier chargé avec succès - Encoding: {encoding}")
            return df
        except UnicodeDecodeError:
            print(f"❌ Échec encoding {encoding}, essai suivant...")
            continue
        except pd.errors.ParserError as e:
            print(f"❌ Erreur de parsing avec {encoding}: {e}")
            # Essayer avec des paramètres plus permissifs
            try:
                df = pd.read_csv(file_path, 
                               encoding=encoding,
                               sep=',',
                               quotechar='"',
                               on_bad_lines='skip',
                               engine='python',
                               error_bad_lines=False,    # Ancienne version pandas
                               warn_bad_lines=True)
                print(f"✅ Fichier chargé avec paramètres permissifs - Encoding: {encoding}")
                return df
            except:
                continue
    
    # Si tout échoue, essayer de charger ligne par ligne
    print("🔄 Tentative de chargement ligne par ligne...")
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        # Nettoyer les lignes problématiques
        clean_lines = []
        for i, line in enumerate(lines):
            # Compter les guillemets pour détecter les lignes mal formées
            quote_count = line.count('"')
            comma_count = line.count(',')
            
            # Si la ligne semble correcte, la garder
            if quote_count % 2 == 0 and comma_count > 0:
                clean_lines.append(line)
            else:
                print(f"⚠️ Ligne {i+1} ignorée (mal formée)")
        
        # Créer un fichier temporaire nettoyé
        temp_file = file_path.replace('.csv', '_cleaned.csv')
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.writelines(clean_lines)
        
        # Charger le fichier nettoyé
        df = pd.read_csv(temp_file, encoding='utf-8')
        print(f"✅ Fichier nettoyé et chargé: {len(df)} lignes")
        return df
        
    except Exception as e:
        print(f"❌ Impossible de charger le fichier: {e}")
        return None

# Chargement des datasets avec la fonction robuste
try:
    print("🔄 Chargement des datasets avec gestion d'erreurs...")
    
    # Chargement des données d'entraînement et de test
    train_df = load_csv_robust(f"{extract_path}/train_set.csv")
    test_df = load_csv_robust(f"{extract_path}/test_set.csv") 
    sample_submission = load_csv_robust(f"{extract_path}/submission_template.csv")
    
    if train_df is not None and test_df is not None:
        print("✅ Tous les datasets chargés avec succès !")
        print(f"📊 Données d'entraînement: {train_df.shape[0]} lignes, {train_df.shape[1]} colonnes")
        print(f"📊 Données de test: {test_df.shape[0]} lignes, {test_df.shape[1]} colonnes")
        print(f"📊 Template de soumission: {sample_submission.shape}")
        
        # Vérifier la qualité des données
        print("\n🔍 Vérification de la qualité des données:")
        print(f"  - Valeurs manquantes train: {train_df.isnull().sum().sum()}")
        print(f"  - Valeurs manquantes test: {test_df.isnull().sum().sum()}")
        
        # Afficher les premières lignes
        print("\n📋 Aperçu des données d'entraînement:")
        print(train_df.head())
        
    else:
        print("❌ Échec du chargement des datasets")
        
except Exception as e:
    print(f"❌ Erreur générale lors du chargement: {e}")
    print("💡 Suggestions:")
    print("  1. Vérifiez que les fichiers CSV sont bien extraits")
    print("  2. Essayez d'ouvrir les fichiers dans Excel pour voir s'ils sont corrompus")
    print("  3. Les noms de fichiers peuvent être différents (train.csv vs train_set.csv)")

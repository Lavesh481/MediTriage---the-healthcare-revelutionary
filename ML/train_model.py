import pandas as pd
import numpy as np
import joblib
import sys
import os

# Ensure we can import from BACKEND
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../BACKEND'))
if backend_path not in sys.path:
    sys.path.append(backend_path)

from model_loader import SymptomBasedModel

def train():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        dataset_path = os.path.join(current_dir, "dataset.csv")
        output_path = os.path.join(current_dir, "../BACKEND/disease_model.pkl")

        print(f"Loading dataset from: {dataset_path}")
        df = pd.read_csv(dataset_path)
        
        # Determine features and target
        # The dataset has 'Disease' as target and 'Symptom_1'...'Symptom_17' as features
        # We need to convert this to a binary matrix where columns are all unique symptoms
        
        # 1. Collect all unique symptoms from relevant columns
        symptom_cols = [col for col in df.columns if 'Symptom' in col]
        
        # Flatten all symptom values into a single list
        all_symptoms_raw = df[symptom_cols].values.flatten()
        
        # Clean symptoms: remove NaN and strip whitespace
        all_symptoms = [s.strip() for s in all_symptoms_raw if pd.notna(s)]
        unique_symptoms = sorted(list(set(all_symptoms)))
        
        print(f"Found {len(unique_symptoms)} unique symptoms.")
        
        # 2. Create binary feature matrix
        # Initialize DataFrame with zeros for all unique symptoms
        # Using a list of dicts is faster than creating an empty DF and filling it cell by cell
        rows_list = []
        for i, row in df.iterrows():
            row_data = {sym: 0 for sym in unique_symptoms}
            for col in symptom_cols:
                sym = row[col]
                if pd.notna(sym):
                    sym_clean = sym.strip()
                    if sym_clean in row_data:
                        row_data[sym_clean] = 1
            rows_list.append(row_data)
            
        # Convert to standard python lists/numpy arrays to avoid pandas dependency in the model
        X_train_data = [list(row.values()) for row in rows_list]
        y_train_data = df['Disease'].tolist()
        
        print(f"Training model with {len(X_train_data)} samples")
        
        # Train model
        model = SymptomBasedModel(X_train_data, y_train_data, unique_symptoms)
        
        # Save trained model
        print(f"Saving model to {output_path}...")
        joblib.dump(model, output_path)
        
        print("✅ disease_model.pkl created successfully")
        
    except Exception as e:
        print(f"❌ Error during training: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    train()

import sys
import os
import pandas as pd
import numpy as np
import joblib

# Ensure we can import from BACKEND
sys.path.append(os.path.abspath('BACKEND'))
from model_loader import SymptomBasedModel

def verify_model():
    print("Loading model...")
    try:
        model_path = "BACKEND/disease_model.pkl"
        model = joblib.load(model_path)
        print(f"✅ Model loaded from {model_path}")
    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        return

    # Test Cases (Disease, Symptoms List)
    test_cases = [
        ("Fungal infection", ["itching", "skin_rash", "nodal_skin_eruptions", "dischromic _patches"]),
        ("Allergy", ["continuous_sneezing", "shivering", "chills", "watering_from_eyes"]),
        ("GERD", ["stomach_pain", "acidity", "ulcers_on_tongue", "vomiting", "cough", "chest_pain"]),
        ("Chronic cholestasis", ["itching", "vomiting", "yellowish_skin", "nausea", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes"]),
        ("Drug Reaction", ["itching", "skin_rash", "stomach_pain", "burning_micturition", "spotting_ urination"])
    ]

    print("\nRunning Verification Tests:")
    print("-" * 60)
    print(f"{'Expected Disease':<25} | {'Predicted Disease':<25} | {'Status'}")
    print("-" * 60)

    passed = 0
    for expected_disease, symptoms in test_cases:
        # Create input vector
        # detailed mapping check isn't needed here, just checking if model predicts correctly given the raw symptoms
        # The model expects a binary vector. We need to map these symptoms to the model's feature_names_in_
        
        feature_names = model.feature_names_in_
        input_vector = [0] * len(feature_names)
        
        for symptom in symptoms:
            symptom_clean = symptom.strip()
            if symptom_clean in feature_names:
                idx = feature_names.index(symptom_clean)
                input_vector[idx] = 1
            else:
                print(f"Warning: Symptom '{symptom}' not found in model features")

        # Predict
        try:
            predicted_disease = model.predict([input_vector])[0]
        except Exception as e:
            predicted_disease = f"Error: {e}"

        status = "✅ PASS" if predicted_disease == expected_disease else "❌ FAIL"
        if status == "✅ PASS":
            passed += 1
            
        print(f"{expected_disease:<25} | {predicted_disease:<25} | {status}")

    print("-" * 60)
    print(f"Verification Results: {passed}/{len(test_cases)} Passed")

if __name__ == "__main__":
    verify_model()

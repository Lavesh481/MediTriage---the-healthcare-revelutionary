import sys
import os
import joblib
import pandas as pd
import numpy as np

# Add BACKEND to path
sys.path.append(os.path.abspath('BACKEND'))

from utils import encode_symptoms
try:
    from model_loader import model, SYMPTOM_LIST
except ImportError:
    # If model_loader tries to load relative to __file__, it might fail if we are running from root
    # let's try to mock it or fix path if needed, but model_loader uses os.path.dirname(__file__) so it should be fine
    pass

def test_prediction():
    print("Testing prediction logic...")
    
    # Test cases: Frontend input -> Expected mapped symptoms -> Expected (or valid) Disease
    test_cases = [
        (["fever", "cough", "shortness_of_breath"], ["high_fever", "cough", "breathlessness"]),
        (["headache", "chest_pain"], ["headache", "chest_pain"]),
        (["sore_throat", "runny_nose"], ["throat_irritation", "runny_nose"])
    ]
    
    for user_symptoms, expected_mapped in test_cases:
        print(f"\nInput: {user_symptoms}")
        
        # Test 1: Encoding/Mapping
        # We need to manually check mapping logic since encode_symptoms returns a vector
        # But we can check if the vector has 1s at expected indices
        vector = encode_symptoms(user_symptoms, SYMPTOM_LIST)
        
        active_features = [SYMPTOM_LIST[i] for i, val in enumerate(vector) if val == 1]
        print(f"Mapped to model features: {active_features}")
        
        missing_features = set(expected_mapped) - set(active_features)
        if missing_features:
            print(f"❌ MAPPING ERROR: Missing expected features {missing_features}")
        else:
            print(f"✅ Mapping correct")
            
        # Test 2: Prediction
        try:
            prediction = model.predict([vector])[0]
            print(f"Prediction: {prediction}")
        except Exception as e:
            print(f"❌ PREDICTION ERROR: {e}")

if __name__ == "__main__":
    test_prediction()

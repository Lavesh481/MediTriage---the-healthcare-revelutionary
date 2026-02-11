import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
data = pd.read_csv("Testing.csv")

# Split features and target
X = data.drop("prognosis", axis=1)
y = data["prognosis"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

import sys
sys.path.append('../BACKEND')
from model_loader import SymptomBasedModel

# Train model
# Using custom SymptomModel to maximize overlap
model = SymptomBasedModel(X, y, X.columns.tolist())
# No fit method needed for this simple class, or we can just pass data in __init__
# The class stores the data.


# Save trained model
joblib.dump(model, "../BACKEND/disease_model.pkl")

print("✅ disease_model.pkl created successfully")

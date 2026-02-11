# Symptoms that require urgent medical attention
SERIOUS_SYMPTOMS = [
    "chest_pain",
    "shortness_of_breath",
    "loss_of_consciousness",
    "severe_bleeding"
]

# Symptoms that should be consulted with a doctor
MODERATE_SYMPTOMS = [
    "fever",
    "cough",
    "fatigue",
    "headache",
    "vomiting"
]

def determine_severity(user_symptoms):
    """
    Determines severity level based on rule-based logic
    """
    for symptom in SERIOUS_SYMPTOMS:
        if symptom in user_symptoms:
            return "Serious"

    for symptom in MODERATE_SYMPTOMS:
        if symptom in user_symptoms:
            return "Moderate"

    return "Mild"

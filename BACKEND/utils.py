def validate_symptoms(symptoms):
    """
    Ensures symptom input is valid
    """
    if not symptoms:
        return False, "No symptoms provided"

    if not isinstance(symptoms, list):
        return False, "Symptoms must be a list"

    return True, None


def encode_symptoms(user_symptoms, symptom_list):
    """
    Converts symptom list into ML input vector
    perfroms mapping from frontend terms to dataset terms
    """
    # Mapping from frontend symtoms to dataset features
    mapping = {
        "fever": "high_fever",
        "shortness_of_breath": "breathlessness",
        "sore_throat": "throat_irritation",
        "runny_nose": "runny_nose",
        "headache": "headache",
        "cough": "cough", 
        "chest_pain": "chest_pain",
        "fatigue": "fatigue",
        "nausea": "nausea"
    }
    
    # Map symptoms
    mapped_symptoms = [mapping.get(s, s) for s in user_symptoms]

    return [
        1 if symptom in mapped_symptoms else 0
        for symptom in symptom_list
    ]

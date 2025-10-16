"""
train_model.py
Train and save a Decision Tree model for symptom -> disease prediction.

Author: Harsh Sengar
"""

import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# --- Constants / Data definitions ---
SYMPTOMS = [
    'back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze'
]

# The mapping used when replacing prognosis strings in the dataset.
# NOTE: keys intentionally match the dataset's strings (including spacing)
DISEASE_TO_CODE = {
    'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40
}

MODEL_OUTPUT_PATH = "model.pkl"
DATASET_PATH = "Prototype.csv"


# --- Functions ---
def load_and_preprocess(csv_path: str) -> pd.DataFrame:
    """Load dataset and replace disease names with integer codes."""
    data = pd.read_csv(csv_path)
    data.replace({'prognosis': DISEASE_TO_CODE}, inplace=True)
    return data


def train_decision_tree(data: pd.DataFrame, feature_columns: list, target_column: str):
    """Train a DecisionTreeClassifier and return the fitted model."""
    X = data[feature_columns]
    y = data[[target_column]]
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X, y)
    return clf


def save_model(obj, path: str):
    """Save a Python object to disk using pickle."""
    with open(path, "wb") as fout:
        pickle.dump(obj, fout)


# --- Main execution ---
if __name__ == "__main__":
    # Load and preprocess the dataset
    dataset = load_and_preprocess(DATASET_PATH)

    # Train the model
    classifier = train_decision_tree(dataset, SYMPTOMS, "prognosis")

    # Persist the trained model so other scripts can load it (keep same filename)
    save_model(classifier, MODEL_OUTPUT_PATH)

    print(f"Training complete — model saved to {MODEL_OUTPUT_PATH}")

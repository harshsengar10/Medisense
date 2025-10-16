"""
Streamlit UI for interacting with the Flask prediction API.

Author: Harsh Sengar
Behavior kept the same as original: sends selected symptoms to Flask /predict endpoint.
"""

import streamlit as st
import requests
import pickle  # kept imported to mirror original environment even if unused here

# Page config
st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🩺",
    initial_sidebar_state="expanded",
)

st.title("Disease Prediction")

# --- Symptom lists (kept identical to original for compatibility) ---
l1 = ['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
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
'yellow_crust_ooze']

l3 = ['<select>'] + l1[:]  # same options as original but created programmatically here

disease = ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

# Create a zero-filled feature vector
feature_vector = [0] * len(l1)

# Sidebar inputs (kept labels and layout same as original)
symptom1 = st.sidebar.selectbox("***Select Symptom 1*** :point_down:", l3)
symptom2 = st.sidebar.selectbox(":red[***Select Symptom 2*** :point_down:]" , l3)
symptom3 = st.sidebar.selectbox(":green[***Select Symptom 3*** :point_down:]", l3)
symptom4 = st.sidebar.selectbox(":orange[***Select Symptom 4*** :point_down:]", l3)
symptom5 = st.sidebar.selectbox(":violet[***Select Symptom 5*** :point_down:]", l3)

selected_symptoms = [symptom1, symptom2, symptom3, symptom4, symptom5]

# Build the input row expected by the Flask API
for idx, symptom_name in enumerate(l1):
    for chosen in selected_symptoms:
        if chosen == symptom_name:
            feature_vector[idx] = 1

input_test = [feature_vector]  # 2D list as required by sklearn predict

# Call the Flask API (same URL as original)
url = "http://localhost:5000/predict"
payload = {"symptoms": input_test}

# Perform request and display result (keeps original logic and messaging)
response = requests.post(url, json=payload)
prediction = None
if response.ok:
    try:
        prediction = response.json().get("prediction")
    except Exception:
        prediction = None

h = 'no'
if prediction is not None:
    for a in range(len(disease)):
        if prediction == a:
            h = 'yes'
            break

if (h == 'yes' and any(s != '<select>' for s in selected_symptoms)):
    title = st.text_input('Predicted Disease is: ', disease[a])
    st.write('The Predicted Disease is:-  ', title)
    st.error("You have the disease.")
    st.warning("Please consult a medical professional.")
else:
    title = st.text_input('Predicted Disease is: ', "Please enter symptoms to predict the disease")
    st.write('The Predicted Disease is:-  ', title)

# Footer and about (kept identical)
st.markdown("---")
st.markdown("### :blue[About]")
st.write("This app predicts diseases based on symptoms provided by the user. It is built with Flask and Streamlit, an open-source Python library for building interactive web applications.")

st.markdown("---")
st.markdown("### :blue[Note]")
st.write("The prediction provided by this app is for informational purposes only and should not be considered a medical diagnosis. Please consult a healthcare professional for a proper evaluation.")

st.sidebar.markdown("---")
st.sidebar.markdown("-----Created with ❤️ by [Harsh Sengar]-----")

st.markdown("---")
if st.button("Go Back"):
    st.markdown(
        """
        [Please Cofirm 👍🏻](http://127.0.0.1:5000/)
        
        <style>
        [class="css-1n543e5 e1ewe7hr10"] {
            text-align: center;
            margin-top: 30px;
            animation: slide-up 1s ease-in-out;
        }
        [class="css-1n543e5 e1ewe7hr10"] {
            display: inline-block;
            padding: 12px 24px;
            font-size: 16px;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 3px;
            text-decoration: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
            animation: scale-in 0.5s ease-in-out;
        }
        [class="css-1n543e5 e1ewe7hr10"]:hover {
            background-color: #0069d9;
        }
        @keyframes scale-in {
            from { transform: scale(0); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Keep the custom CSS block exactly as it was (no UI changes requested)
st.markdown(
    """
    <style>
        [data-testid="stHeader"] {
        background-color: transparent;
        box-shadow: none;
        }
        [data-testid="stAppViewContainer"]  {
        background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
        background-size: 180%;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
        }}
        .block-container {
            padding: 1rem;
            border-radius: 0.5rem;
            box-shadow: 0 0 0.5rem rgba(0, 0, 0, 0.1);
        }
        .sidebar .block-container {
            background-color: #f5f5f5;
        }
        .sidebar .block-container select {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 0.3rem;
        }
        [class="css-1nm2qww e1akgbir2"] {
            background-color: #a9a9a9;
            text-decoration: underline;
        }
        [data-testid="stSidebar"] {
            background-color: #e8f3db;
        }
        [class="row-widget stSelectbox"] {
            background-color:  #ACDDDE;
            [class="css-16idsys eqr7zpz4"] {
            text-decoration: underline;
            color: #007bff;
            }
        }
        .sidebar .block-container .stSelectbox {
            padding: 0;
            background-color: transparent;
            border: none;
        }
        .sidebar .block-container .help-button {
            font-size: 0.8rem;
            color: #888;
            transition: color 0.3s ease;
        }
        .sidebar .block-container .help-button:hover {
            color: #555;
        }
        h1 {
        text-decoration: underline;
        }
        h3 {
        text-decoration: underline;
        }
        .element-container {
            text-align: center;
            animation: slide-up 1s ease-in-out;
        }
        .prediction-message {
            font-size: 1.2rem;
            margin-top: 1rem;
            animation: fade-in 1s ease-in-out;
        }
        .prediction-message .st-error {
            color: #ff4d4d;
            text-decoration: underline;
        }
        .prediction-message .st-success {
            color: #1ebc61;
            text-decoration: underline;
        }
        .prediction-message .st-warning {
            color: #ffaa1d;
            text-decoration: underline;
        }
        .prediction-message .st-info {
            color: #1e90ff;
            text-decoration: underline;
        }
        .about-section {
            margin-top: 2rem;
        }
        .about-section h3 {
            margin-bottom: 1rem;
            text-decoration: underline;
        }
        .note-section {
            margin-top: 2rem;
        }
        .note-section h3 {
            margin-bottom: 1rem;
            text-decoration: underline;
        }
        .footer-section {
            margin-top: 3rem;
            text-align: center;
        }
        .footer-section p {
            font-size: 0.9rem;
            color: #777;
        }
        
        @keyframes fade-in {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

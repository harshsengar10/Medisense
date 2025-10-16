# 🩺 Disease Prediction using Machine Learning  

This project predicts diseases based on symptoms entered by the user.  
It combines **Machine Learning**, **Flask**, and **Streamlit** to deliver a simple, interactive web application.

---

## 📘 Project Overview

- **Model**: Decision Tree Classifier trained on symptom–disease dataset  
- **Backend**: Flask (REST API that handles prediction requests)  
- **Frontend**: Streamlit (interactive UI for users to select symptoms)  
- **Integration**: Streamlit app communicates with Flask backend via HTTP POST  

The goal is to demonstrate how AI can assist in preliminary health assessment by mapping symptoms to possible diseases.

---

## 👨‍💻 Author
**Harsh Sengar**

---

## 🧩 Folder Struct├── app.py # Flask API server
├── streamlit_app.py # Streamlit frontend
├── train_model.py # Model training script
├── model.pkl # Trained Decision Tree model (generated after training)
├── Prototype.csv # Dataset used for training
├── templates/ # HTML templates (for Flask pages)
├── static/ # CSS, JS, and image files (if any)
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 1️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate   # (Windows)
# OR
source venv/bin/activate   # (Linux/Mac)

### 2️⃣ Install required libraries
```pip install pandas scikit-learn flask streamlit requests```


### 3️⃣ Train the model

Run the training script to generate model.pkl:

```python train_model.py```

### 4️⃣ Start the Flask backend
```python app.py```


Flask will start locally at:
➡️ http://127.0.0.1:5000/

5️⃣ Launch the Streamlit frontend

Open a new terminal window (while Flask is still running):

streamlit run streamlit_app.py


Streamlit will start at:
➡️ http://localhost:8501/

🌐 How It Works

The user selects up to 5 symptoms in the Streamlit interface.

These selections are converted into a feature vector and sent as JSON to the Flask /predict API.

The Flask app loads the pre-trained Decision Tree model (model.pkl) and predicts a disease code.

The Streamlit interface maps that code to the disease name and displays it, along with a warning to consult a doctor.

🧠 Technologies Used
Component	Technology
Machine Learning	Scikit-learn (DecisionTreeClassifier)
Data Handling	Pandas
Web Framework	Flask
Frontend	Streamlit
Communication	REST API via requests library
Language	Python 3.9+

⚠️ Disclaimer

This project is for educational purposes only.
It does not provide medical advice or diagnosis.
Always consult a certified healthcare professional for medical concerns.


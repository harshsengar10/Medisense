"""
Flask API for disease prediction.

Author: Harsh Sengar
Notes:
- Keeps same routes as before.
- Loads model.pkl from the local directory and exposes /predict endpoint.
"""

from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import webbrowser

app = Flask(__name__)

# --- Load trained model from disk once at startup ---
MODEL_FILE = "model.pkl"
with open(MODEL_FILE, "rb") as f:
    model = pickle.load(f)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction endpoint - expects JSON body like {"symptoms": [[0,0,1, ...]]}
@app.route("/predict", methods=["POST"])
def predict():
    try:
        payload = request.get_json(force=True)
        symptoms = payload["symptoms"]  # expecting a 2D list
        predictions = model.predict(symptoms)
        result = {"prediction": int(predictions[0])}
        return jsonify(result)
    except Exception as exc:
        # Provide a simple error response for debugging in development
        return jsonify({"error": str(exc)}), 400


# Open Streamlit in a new browser tab (route preserved)
@app.route("/streamlit/<name>")
def open_streamlit(name):
    webbrowser.open_new_tab("http://localhost:8501")  # Change the URL if needed
    return jsonify({"message": "Streamlit page opened"})


# Test form that redirects to the streamlit opener (route preserved)
@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        return redirect(url_for("open_streamlit", name=request.form["name"]))
    return render_template("predict.html")


# Other informational routes (kept unchanged)
@app.route("/about.html")
def open_about():
    return render_template("about.html")


@app.route("/know_more.html")
def know_more():
    return render_template("know_more.html")


if __name__ == "__main__":
    # Start Flask app in debug mode for development (same behavior as original)
    app.run(debug=True)

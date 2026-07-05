from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# Project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model and label encoder
model = joblib.load(os.path.join(BASE_DIR, "models", "intrusion_model.pkl"))
label_encoder = joblib.load(os.path.join(BASE_DIR, "models", "label_encoder.pkl"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return render_template("index.html", result="No file selected.")

    file = request.files["file"]

    if file.filename == "":
        return render_template("index.html", result="No file selected.")

    try:
        df = pd.read_csv(file)

        df.columns = df.columns.str.strip()

        if "Label" in df.columns:
            df = df.drop("Label", axis=1)

        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)

        df = df.apply(pd.to_numeric, errors="coerce")
        df.dropna(inplace=True)

        predictions = model.predict(df)

        labels = label_encoder.inverse_transform(predictions)

        benign = sum(labels == "BENIGN")
        attack = len(labels) - benign

        result = f"Total Records: {len(labels)} | BENIGN: {benign} | ATTACK: {attack}"

        return render_template("index.html", result=result)

    except Exception as e:
        return render_template("index.html", result=str(e))

if __name__ == "__main__":
    app.run(debug=True)
import pandas as pd
import numpy as np
import joblib


model = joblib.load("C:/Users/Dell/OneDrive/Desktop/AI-Intrusion-Detection-System Project/AI-Intrusion-Detection-System/models/intrusion_model.pkl")
label_encoder = joblib.load("C:/Users/Dell/OneDrive/Desktop/AI-Intrusion-Detection-System Project/AI-Intrusion-Detection-System/models/label_encoder.pkl")


df = pd.read_csv("C:/Users/Dell/OneDrive/Desktop/AI-Intrusion-Detection-System Project/AI-Intrusion-Detection-System/dataset/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")


df.columns = df.columns.str.strip()
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)


X = df.drop("Label", axis=1)


X = X.apply(pd.to_numeric, errors="coerce")
X.replace([np.inf, -np.inf], np.nan, inplace=True)
X.dropna(inplace=True)


sample = X.head(10)


predictions = model.predict(sample)
labels = label_encoder.inverse_transform(predictions)

print("Predictions:")
for i, label in enumerate(labels, 1):
    print(f"Row {i}: {label}")
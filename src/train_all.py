import os
import glob
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Get project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Dataset folder
folder_path = os.path.join(project_root, "dataset", "MachineLearningCSV", "MachineLearningCVE")

# Find all CSV files
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

print(f"Found {len(csv_files)} CSV files")

# Load all files
dfs = []
for file in csv_files:
    print("Loading:", os.path.basename(file))
    df = pd.read_csv(file, low_memory=False)
    dfs.append(df)

# Combine all files
df = pd.concat(dfs, ignore_index=True)

print("Dataset Shape:", df.shape)

# Clean column names
df.columns = df.columns.str.strip()

# Replace infinity values
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Remove missing values
df.dropna(inplace=True)

# Features and target
X = df.drop("Label", axis=1)
y = df["Label"]

# Convert all columns to numeric
X = X.apply(pd.to_numeric, errors="coerce")

# Remove invalid rows
X.replace([np.inf, -np.inf], np.nan, inplace=True)

valid_rows = X.notna().all(axis=1)
X = X[valid_rows]
y = y[valid_rows]

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
print("Training model...")
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Results
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save model
joblib.dump(model, os.path.join(project_root, "intrusion_model.pkl"))
joblib.dump(encoder, os.path.join(project_root, "label_encoder.pkl"))

print("\nModel saved successfully!")
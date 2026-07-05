System Architecture

AI-Powered Intrusion Detection System Architecture

The system follows a machine learning pipeline for detecting network intrusions.

Workflow

1. Dataset Collection
   
   - CIC-IDS-2017 dataset is collected and stored in the "dataset" folder.

2. Data Preprocessing
   
   - Multiple CSV files are combined.
   - Missing values and invalid data are removed.
   - Data is converted into a format suitable for machine learning.

3. Model Training
   
   - A Random Forest classifier is trained using the cleaned dataset.
   - The trained model and label encoder are saved in the "models" folder.

4. Flask Web Application
   
   - Users access the web application through a browser.
   - Users upload a CSV file containing network traffic data.

5. Prediction
   
   - The uploaded file is processed.
   - The trained model predicts whether each record is BENIGN or ATTACK.

6. Result Display
   
   - The application displays the total number of records, BENIGN records, and ATTACK records on the webpage.

Components

- User Interface (Flask)
- Data Processing Module
- Machine Learning Model (Random Forest)
- Prediction Engine
- Result Display Module
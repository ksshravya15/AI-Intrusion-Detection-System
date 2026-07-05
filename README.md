AI-Powered Intrusion Detection System

Project Overview

This project is an AI-based Intrusion Detection System (IDS) that detects malicious network traffic using Machine Learning. It is built using Python and Flask and trained on the CIC-IDS-2017 dataset.
 
 Features

- Upload a network traffic CSV file.
- Detect normal (BENIGN) and malicious (ATTACK) traffic.
- Machine Learning model trained using Random Forest.
- Simple Flask-based web interface.
- Displays prediction results after processing the uploaded file.

Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib

Dataset

- CIC-IDS-2017

Project Structure

- "dataset/" – Dataset files
- "models/" – Trained model and label encoder
- "src/" – Python source code
- "templates/" – HTML templates
- "static/" – Static files (CSS, images, etc.)
- "requirements.txt" – Python dependencies
- "README.md" – Project documentation

How to Run

1. Install the required packages:
   pip install -r requirements.txt
2. Start the Flask application:
   python src/app.py
3. Open your browser and go to:
   http://127.0.0.1:5000
4. Upload a CSV file and click Predict to view the intrusion detection results.

Future Enhancements

- Display graphs and charts for prediction results.
- Support real-time network traffic monitoring.
- Improve the web interface.
- Deploy the application to a cloud platform.

Author

K. S. Shravya
Bachelor of Engineering
In
Information Science and Engineering
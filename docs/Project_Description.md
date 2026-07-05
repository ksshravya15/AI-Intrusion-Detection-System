Project Description

Project Title

AI-Powered Intrusion Detection System

Objective

The objective of this project is to develop a machine learning-based Intrusion Detection System (IDS) capable of identifying malicious network traffic and distinguishing it from normal network traffic. The system aims to improve cybersecurity by providing accurate and automated intrusion detection.

Problem Statement

Traditional intrusion detection methods often rely on predefined rules and signatures, making them less effective against new or unknown cyberattacks. This project addresses this issue by using machine learning to analyze network traffic patterns and classify them as either BENIGN or ATTACK.

Methodology

1. Download the CIC-IDS-2017 dataset.
2. Preprocess and combine multiple CSV files.
3. Clean the dataset by removing missing and invalid values.
4. Train a Random Forest classifier.
5. Save the trained model and label encoder.
6. Develop a Flask web application for user interaction.
7. Allow users to upload CSV files and display prediction results.

Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Git and GitHub

Dataset

The project uses the CIC-IDS-2017 dataset, which contains both normal network traffic and multiple categories of cyberattacks for training and testing intrusion detection models.

Outcome

The developed system successfully predicts whether uploaded network traffic records are BENIGN or ATTACK using a trained Random Forest machine learning model through a user-friendly web interface.
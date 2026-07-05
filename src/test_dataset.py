import pandas as pd

df=pd.read_csv("C:/Users/Dell/OneDrive/Desktop/AI-Intrusion-Detection-System Project/AI-Intrusion-Detection-System/dataset/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

print("Dataset loaded successfully!")
print(df.head())
print(df.shape)
print(df.columns)
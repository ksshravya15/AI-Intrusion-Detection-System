import pandas as pd

df = pd.read_csv("C:/Users/Dell/OneDrive/Desktop/AI-Intrusion-Detection-System Project/AI-Intrusion-Detection-System/dataset/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

df.columns = df.columns.str.strip()

print("Missing values:")
print(df.isnull().sum())

df = df.dropna()

print("\nDataset shape after cleaning:", df.shape)

print("\nTraffic labels:")
print(df["Label"].value_counts())
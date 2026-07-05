import os
import glob
import pandas as pd

# 1. Automatically find the correct 'MachineLearningCVE' folder
script_dir = os.path.dirname(os.path.abspath(__file__))  # points to 'src'
project_root = os.path.dirname(script_dir)              # points to the project root

# This sets the folder path perfectly to: dataset/MachineLearningCVE
folder_path = os.path.join(project_root, "dataset", "MachineLearningCVE")

print("--- PATH CHECK ---")
print(f"Looking for CSV files inside:\n--> {folder_path}\n")

# 2. Find all CSV files inside that folder
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

print(f"Number of CSV files found: {len(csv_files)}")
print("CSV files list:")
for file in csv_files:
    print(f"- {os.path.basename(file)}")

# 3. SAFETY NET: Stop the script nicely if no files were found (instead of crashing)
if len(csv_files) == 0:
    print("\n[STOP] No CSV files were found! Please check:")
    print("1. Are the files completely downloaded from OneDrive?")
    print("2. Are the CSV files physically inside the 'dataset/MachineLearningCVE' folder?")
    exit()

# 4. Read and combine all CSV files safely
dataframes = []
for file in csv_files:
    print(f"Loading {os.path.basename(file)}...")
    df = pd.read_csv(file, low_memory=False)
    dataframes.append(df)

# 5. Combine into one DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

print("\nAll files loaded successfully!")
print("Dataset Shape:", combined_df.shape)
print(combined_df.head())
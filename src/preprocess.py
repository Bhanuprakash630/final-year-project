import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

def preprocess_data(input_path, output_path):
    # Load the dataset
    df = pd.read_csv(input_path)
    
    # 1. Drop User_ID as it's just a label, not a feature for prediction
    df = df.drop(columns=['user_id'])
    
    # 2. Convert 'role' (text) into numbers (0, 1, 2, etc.)
    le = LabelEncoder()
    df['role'] = le.fit_transform(df['role'])
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 3. Save the processed data
    df.to_csv(output_path, index=False)
    print(f"✅ Data processed and saved to: {output_path}")

if __name__ == "__main__":
    preprocess_data('data/raw/insider_threat_dataset_10000.csv', 
                    'data/processed/processed_insider_threat.csv')
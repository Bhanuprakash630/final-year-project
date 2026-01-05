import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import os

def evaluate_performance(model_path, model_name, X, y):
    if not os.path.exists(model_path):
        print(f"⚠️ {model_name} not found at {model_path}. Skipping...")
        return None

    # Load and Predict
    model = joblib.load(model_path)
    predictions = model.predict(X)
    acc = accuracy_score(y, predictions)

    print(f"\n{'='*20} {model_name} Report {'='*20}")
    print(f"Overall Accuracy: {acc:.2%}")
    print("\nDetailed Classification Report:")
    print(classification_report(y, predictions))
    
    print("Confusion Matrix:")
    print(confusion_matrix(y, predictions))
    return acc

def run_comparison():
    # 1. Load data
    data_path = 'data/processed/processed_insider_threat.csv'
    if not os.path.exists(data_path):
        print("❌ Processed data not found. Please run preprocess.py first.")
        return
        
    df = pd.read_csv(data_path)
    X = df.drop(columns=['insider_threat'])
    y = df['insider_threat']

    # 2. Evaluate Random Forest
    rf_acc = evaluate_performance('models/random_forest_model.pkl', "Random Forest", X, y)

    # 3. Evaluate XGBoost
    xgb_acc = evaluate_performance('models/xgboost_model.pkl', "XGBoost", X, y)

    # 4. Summary Table
    print("\n" + "#"*50)
    print("📊 FINAL COMPARISON SUMMARY")
    print("#"*50)
    if rf_acc: print(f"Random Forest Accuracy: {rf_acc:.2%}")
    if xgb_acc: print(f"XGBoost Accuracy:       {xgb_acc:.2%}")
    print("#"*50)

if __name__ == "__main__":
    run_comparison()
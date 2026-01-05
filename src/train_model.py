import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier # New Model
import os

def train_models():
    # Load processed data
    df = pd.read_csv('data/processed/processed_insider_threat.csv')
    
    X = df.drop(columns=['insider_threat'])
    y = df['insider_threat']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # --- Model 1: Random Forest ---
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    joblib.dump(rf_model, 'models/random_forest_model.pkl')
    print("✅ Random Forest trained.")

    # --- Model 2: XGBoost ---
    xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    xgb_model.fit(X_train, y_train)
    joblib.dump(xgb_model, 'models/xgboost_model.pkl')
    print("✅ XGBoost trained.")

if __name__ == "__main__":
    train_models()
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

from src.data_loader import load_and_clean_data

def train_and_save_model(data_path=r"D:\Work_USA\Projects\lab-report-automation\data\kidney_disease.csv", model_path=r"D:\Work_USA\Projects\lab-report-automation\src\ckd_model.pkl"):
    df, _ = load_and_clean_data(data_path)

    # Drop non-feature columns
    if 'id' in df.columns:
        df = df.drop(columns=['id'])

    X = df.drop('classification', axis=1)
    y = df['classification']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

    # Save model
    joblib.dump(model, model_path)
    print(f"✅ Model saved to: {model_path}")

if __name__ == "__main__":
    train_and_save_model()
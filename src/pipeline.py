import joblib
import pandas as pd

# Load preprocessing and model
scaler = joblib.load("models/scaler.pkl")
model = joblib.load("models/house_price_model.pkl")

def predict_price(input_dict):
    df = pd.DataFrame([input_dict])   # convert to DataFrame
    df_scaled = scaler.transform(df)  # preprocess
    prediction = model.predict(df_scaled)
    return prediction[0]

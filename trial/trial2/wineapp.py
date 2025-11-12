from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import uvicorn
import os


load_dotenv()

try:
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    print(" Model and scaler loaded successfully.")
except Exception as e:
    print(f"Error loading model or scaler: {e}")


app = FastAPI(title="Wine Quality Prediction API",
              description="An API to predict wine quality based on its features.",
              version="1.0.0")

class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


@app.get("/")
def root():
    return {"message": "Welcome to the Wine Quality Prediction API!"}

# ===== 5. Prediction Endpoint =====
@app.post("/predict")
def predict_quality(features: WineFeatures):
    # Convert input to NumPy array
    data = np.array([[features.fixed_acidity,
                      features.volatile_acidity,
                      features.citric_acid,
                      features.residual_sugar,
                      features.chlorides,
                      features.free_sulfur_dioxide,
                      features.total_sulfur_dioxide,
                      features.density,
                      features.pH,
                      features.sulphates,
                      features.alcohol]])
    
    # Scale input
    data_scaled = scaler.transform(data)

    # Predict
    prediction = model.predict(data_scaled)[0]
    probability = model.predict_proba(data_scaled)[0][1]

    # Output
    result = "Good Quality" if prediction == 1 else "Bad Quality"

    return {
        "prediction": int(prediction),
        "quality_label": result,
        "probability_good": round(probability, 3)
    }




if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))
   
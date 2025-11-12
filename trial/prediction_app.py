# Imports for FastAPI and data handling
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# 8 # lets load our saved model
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# 13 # lets initialize our application
app = FastAPI()

# 17 # lets create our pydantic model
class WineFeatures(BaseModel):
    # Features required for the prediction model
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

# 34 # home endpoints - home
@app.get("/")
def home():
    return {"message": "Welcome To Wine Quality Predictor"}

# 43 # prediction endpoint
@app.post("/predict")
def predict(wine: WineFeatures):
    # 46 # convert the features to 2D numpy array using [[...]]
    features = np.array([[
        wine.fixed_acidity,
        wine.volatile_acidity,
        wine.citric_acid,
        wine.residual_sugar,
        wine.chlorides,
        wine.free_sulfur_dioxide,
        wine.total_sulfur_dioxide,
        wine.density,
        wine.pH,
        wine.sulphates,
        wine.alcohol
    ]])

# 62 # lets scale our input features using the loaded scaler (to normalize the input features)
    scaled_features = scaler.transform(features)

    # 65 # lets make prediction with the loaded model
    prediction = model.predict(scaled_features)

    # 68 # Return the prediction and the prediction converted to string for serialization
    return {"predicted_quality": str(prediction[0])}

# 71 # run app with --- uvicorn wine_app:app --reload
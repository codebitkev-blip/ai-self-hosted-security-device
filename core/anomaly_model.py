from sklearn.ensemble import IsolationForest
import joblib
import os

MODEL_PATH = "storage/model.pkl"

def train(data):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(data)
    os.makedirs("storage", exist_ok=True)
    joblib.dump(model, MODEL_PATH)

def load():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model not trained yet")
    return joblib.load(MODEL_PATH)

def predict(model, features):
    return model.predict([features])[0]

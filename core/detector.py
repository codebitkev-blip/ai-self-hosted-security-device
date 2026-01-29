from core.feature_extractor import extract_features
from core.anomaly_model import load, predict
from storage.db import log_event

model = None

def handle_packet(packet):
    global model

    if model is None:
        model = load()

    features = extract_features(packet)
    result = predict(model, features)

    if result == -1:
        print("⚠️ Anomaly detected:", packet)
        log_event(packet)

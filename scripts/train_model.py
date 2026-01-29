from core.anomaly_model import train

# Simulated normal traffic
training_data = [
    [60, 6],
    [64, 6],
    [70, 17],
    [90, 6],
    [110, 17],
    [120, 6],
]

train(training_data)
print("Model trained successfully")

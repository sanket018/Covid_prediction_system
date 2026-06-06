import joblib
import numpy as np

# Load Model
model = joblib.load(
    "model/covid_model.pkl"
)

# Sample Input
sample_data = np.array([
    [
        0,          # Active
        10637,      # Discharged
        129,        # Deaths
        0.0,        # Active Ratio
        98.80,      # Discharge Ratio
        1.20,       # Death Ratio
        100896618   # Population
    ]
])

prediction = model.predict(sample_data)

print("Predicted Total Cases:")
print(round(prediction[0]))
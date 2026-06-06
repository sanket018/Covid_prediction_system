import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load Dataset
df = pd.read_csv("data/Latest Covid-19 India Status.csv")

# Features
X = df.drop(
    columns=["State/UTs", "Total Cases"]
)

# Target
y = df["Total Cases"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

score = r2_score(y_test, y_pred)

print(f"R2 Score: {score:.4f}")

# Save Model
joblib.dump(
    model,
    "model/covid_model.pkl"
)

print("Model saved successfully.")
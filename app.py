from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/covid_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    values = [
        float(request.form["Active"]),
        float(request.form["Discharged"]),
        float(request.form["Deaths"]),
        float(request.form["ActiveRatio"]),
        float(request.form["DischargeRatio"]),
        float(request.form["DeathRatio"]),
        float(request.form["Population"])
    ]

    prediction = model.predict([values])[0]

    return render_template(
        "result.html",
        prediction=round(prediction)
    )


if __name__ == "__main__":
    app.run(debug=True)
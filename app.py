from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
saved_data = joblib.load("model.pkl")

model = saved_data["model"]
scaler = saved_data["scaler"]
feature_names = saved_data["feature_names"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict_page")
def predict_page():
    return render_template(
        "index.html",
        feature_names=feature_names,
        prediction=None,
        confidence=None
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        values = []

        for feature in feature_names:
            values.append(float(request.form[feature]))

        values = np.array(values).reshape(1, -1)

        values_scaled = scaler.transform(values)

        prediction = model.predict(values_scaled)[0]

        probability = model.predict_proba(values_scaled)[0]

        confidence = round(max(probability) * 100, 2)

        if prediction == 1:
            result = "🟢 BENIGN"
        else:
            result = "🔴 MALIGNANT"

        return render_template(
            "index.html",
            feature_names=feature_names,
            prediction=result,
            confidence=confidence
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)
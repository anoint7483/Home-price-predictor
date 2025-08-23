from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

# Load trained model
model_path = os.path.join("models", "house_price_model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # create templates/index.html

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from form
        features = [float(x) for x in request.form.values()]
        features = np.array(features).reshape(1, -1)

        # Predict using model
        prediction = model.predict(features)[0]

        return render_template("index.html", prediction_text=f"Predicted House Price: ₹ {prediction:,.2f}")
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

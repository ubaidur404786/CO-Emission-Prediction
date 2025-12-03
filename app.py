from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app=Flask(__name__)

#load model
# load model
try:
    import os
    model_path = os.path.join(os.path.dirname(__file__), "rf_pipeline_model.pkl")
    model = joblib.load(model_path)
    print("Model loaded successfully!")
    print("Loaded model type:", type(model))
    print("Model steps:", model.named_steps)


    @app.route("/")

    def home():
        return render_template("index.html")
    @app.route("/predict", methods=["POST"])
    def predict():
        try:
            print("RAW FORM:", request.form)

            engine_size = float(request.form["engine_size"])
            cylinders = int(request.form["cylinders"])
            fuel_consumption = float(request.form["fuel_consumption"])
            make = request.form["make"]
            transmission = request.form["transmission"]
            fuel = request.form["fuel"]

            print("Parsed values:", engine_size, cylinders, fuel_consumption, make, transmission, fuel)

            new_data = pd.DataFrame({
                "ENGINE SIZE": [engine_size],
                "CYLINDERS": [cylinders],
                "FUEL CONSUMPTION": [fuel_consumption],
                "MAKE": [make],
                "TRANSMISSION": [transmission],
                "FUEL": [fuel]
            })

            print("New DataFrame:\n", new_data)

            prediction = model.predict(new_data)
            result = np.round(prediction[0])

            return render_template("index.html", prediction_text=f"Predicted CO₂ Emission: {result}")

        except Exception as e:
            print("ERROR:", e)  # very important
            return render_template("index.html", prediction_text=f"Error is : {str(e)}")


except Exception as e:
    print("Error ! Reason",str(e))
    model = None

if __name__=="__main__":
    app.run(debug=False)
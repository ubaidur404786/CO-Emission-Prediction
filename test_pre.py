import joblib
import pandas as pd
import numpy as np

try:

    rf_pileline_model=joblib.load("rf_pipeline_model.pkl")

    print("Model loaded!")
    new_data = pd.DataFrame({
        "ENGINE SIZE": [3.5],
        "CYLINDERS": [6],
        "FUEL CONSUMPTION": [10.5],
        "MAKE": ["ACURA"],
        "TRANSMISSION": ["A4"],
        "FUEL": ["X"]
    })


    prediction=rf_pileline_model.predict(new_data)

    print("Predicted CO2 Emmison is = ",np.round(prediction[0]))

except Exception as e:
    print("Error loading model! Reason",str(e))






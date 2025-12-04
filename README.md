
# CO₂ Emission Prediction Web App

This project is a Flask-based machine learning web application that predicts **vehicle CO₂ emissions (g/km)** using a trained **Random Forest Regression** model. Users input engine size, cylinders, fuel consumption, make, transmission, and fuel type, and the app instantly returns a CO₂ emission prediction. The full preprocessing pipeline and model are saved in `rf_pipeline_model.pkl`, making the app fully portable and ready for deployment.

---

##  Features
- End-to-end ML pipeline (preprocessing → training → prediction)  
- Random Forest Regression model  
- User-friendly Flask web interface  
- Dockerized for easy deployment  
- Clean model loading with error handling  
- Supports both categorical and numerical features  

---

##  How It Works
1. User enters vehicle details in the web form.  
2. Flask converts the inputs into a pandas DataFrame.  
3. The trained pipeline processes the data (encoding + scaling).  
4. The Random Forest model predicts CO₂ emissions.  
5. Prediction is shown on the UI.  

## Docker Quick Start 
Follws these steps if you want to run this web for testing 
This guide provides the minimal steps required to run the `ubaidur404786/co2_emmision_app` Docker image on your machine.
## Prerequisites
- Docker: Ensure you have Docker Engine or Docker Desktop installed on your system.
## Run the Application
Execute the following command in your terminal. This command downloads the image (if not already present), runs it in the background, and maps the container's internal port to a port on your host machine.
1. `docker pull ubaidur404786/co2_emmision_app`
2. `docker run -p 5000:5000 ubaidur404786/co2_emmision_app` or you can change your port if it busy with other task "5000:5000"
## Access the Application
Once the container is running, open your web browser and navigate to:

`http://localhost:5000`

<img width="1557" height="957" alt="image" src="https://github.com/user-attachments/assets/611d84f0-0c51-478a-b49e-40ae77b5949f" />

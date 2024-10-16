import streamlit as st
import pickle
import numpy as np

# Load the saved model and encoders
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    
    st.write("""### We need some information to predict the salary""")
    
    countries = (
        "United States of America",
        "Other",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "Canada",
        "India",
        "France",
        "Brazil",
        "Netherlands",
        "Australia",
        "Spain",
        "Poland",
        "Sweden",
        "Italy",
        "Switzerland",
        "Denmark",
        "Norway",
        "Israel",
        "Portugal",
        "Austria"
    )
    
    education_levels = (
        "Less than Bachelor's",
        "Bachelor's degree",
        "Master's degree",
        "Post grad"
    )
    
    # Get user input
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)
    experience = st.slider("Years of Experience", 0, 50, 3)

    # Button to trigger the prediction
    calc_salary = st.button("Calculate Salary")
    
    if calc_salary:
        # Transform the inputs using the label encoders
        country_enc = le_country.transform([country])[0]
        education_enc = le_education.transform([education])[0]
        
        # Prepare the feature array for the model
        X = np.array([[country_enc, education_enc, experience]])
        
        # Make the salary prediction
        salary = regressor.predict(X)
        
        # Display the predicted salary
        st.subheader(f"The estimated salary is ${salary[0]:,.2f}")

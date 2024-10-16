# DevSalaryInsights


A Streamlit app that predicts software developer salaries based on education, experience, and location. Explore salary data from the Stack Overflow Developer Survey with interactive visualizations.

## Project Overview

This project allows users to predict software developer salaries using machine learning models. Additionally, the app provides insights into the distribution of salaries across different countries and experience levels, derived from the Stack Overflow Developer Survey.

## Features

- **Salary Prediction**: Predict software developer salaries based on user inputs (education, experience, country).
- **Salary Exploration**: Visualize salary data across different countries and levels of experience.
- **Interactive Charts**: Explore salary distribution using pie charts, bar charts, and line charts.

## Project Structure

- `app.py`: Main script to run the Streamlit app.
- `explore_page.py`: Code for exploring salary data through visualizations.
- `predict_page.py`: Contains the logic for predicting salaries.
- `survey_results_public.csv`: Stack Overflow Developer Survey 2023 dataset used for predictions and insights.
- `saved_steps.pkl`: Pickled model file used for salary prediction.


## Setup and Installation

### 1. Clone the repository

      git clone https://github.com/rahul-vinay/DevSalaryInsights.git
      cd rahul-vinay

### 2. Set up a virtual environment (If on Windows, use):

     py -3 -m venv venv
     venv\Scripts\activate

### 3. Install the required dependancies (ensure streamlit, pandas and matplotlib are installed)

     pip install -r requirements.txt

### 4. Run the Streamlit app

    streamlit run app.py


## Usage

- **Salary Prediction**: Navigate to the "Predict" page and enter details such as education level, years of experience, and country. The app will predict your estimated salary.
- **Salary Exploration**: Navigate to the "Explore" page to view charts and insights based on global software developer salary data.

## Data Source

The data used in this project is sourced from the [Stack Overflow Developer Survey 2023](https://survey.stackoverflow.co/2023/).



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to categorize countries based on cutoff
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

# Function to clean experience years
def clean_exp(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

# Function to clean education levels
def clean_ed(x):
    x = x.replace("’", "'").strip()

    if "bachelor" in x.lower():
        return "Bachelor's degree"
    if "master" in x.lower():
        return "Master's degree"
    if "professional" in x.lower():
        return "Post grad"
    
    return "Less than Bachelor's"

@st.cache_data
def load_data():
    # Load the data only once
    df = pd.read_csv("survey_results_public.csv")
    
    # Only keep relevant columns
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]

    # Filter rows where salary is non-null
    df = df[df["ConvertedCompYearly"].notnull()]
    
    # Filter rows for full-time employed respondents
    df = df[df["Employment"].str.contains("Employed, full-time", na=False)]

    # Drop any remaining NaN values
    df = df.dropna()

    # Shorten categories for country to group smaller ones into "Other"
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)

    # Apply salary limits
    df = df[df["ConvertedCompYearly"] <= 250000]
    df = df[df["ConvertedCompYearly"] >= 10000]
    df = df[df["Country"] != "Other"]

    # Clean YearsCodePro and EdLevel columns
    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_exp)
    df["EdLevel"] = df["EdLevel"].apply(clean_ed)
    
    # Rename salary column for clarity
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")
    
    st.write(
        """
        ### Stack Overflow Developer Survey 2023
        """
    )   
    
    # Pie chart of countries
    data = df["Country"].value_counts()
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle
    
    st.write("""#### Number of Data from different countries""")
    st.pyplot(fig1)
    plt.close(fig1)
    
    # Bar chart for mean salary based on country
    st.write(
        """
        #### Mean Salary based on Country
        """
    )
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    
    # Line chart for salary based on years of experience
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

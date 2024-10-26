# importing all the different modules needed
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# loading the dataset
titanic_data = pd.read_csv('/Desktop/BETA/DATA_SCIENCE/Files/titanic.csv')

# changing it to a framework
df = pd.DataFrame(titanic_data)

# dropping the cabin to clean up data 
df.drop('Cabin', inplace=True, axis=1)

# dropping remaining empty columns
df.dropna(inplace=True, axis=0)

# counting the genders on the titanic
gender_counts = df['Sex'].value_counts()

# Display bar graph for number of males vs. females
st.subheader("Gender Distribution Onboard")
fig, ax = plt.subplots(figsize=(4, 2))
gender_counts.plot(kind='bar', color=['skyblue', 'salmon'], ax=ax, width=0.5)
plt.ylabel("Number of Passengers")
plt.title("Number of Males vs. Females Onboard")
st.pyplot(fig)


# Create a summary table
summary_table = df.groupby(['Pclass', 'Sex']).agg(
    avg_fare=('Fare', 'mean'),
    survival_rate=('Survived', 'mean')
).reset_index()

# Streamlit app layout
st.title("Titanic Data Analysis")

# Display the summary table
st.subheader("Summary Table: Average Fare and Survival Rate by Class and Gender")
st.dataframe(summary_table)





import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

sns.set()

DATA_URL = ("IBM.csv")

st.title("IBM HR Analytics v2")

st.sidebar.title("Select Univariate/Bivariate")

st.markdown("Employee Attrition & Performance Dashboard")

@st.cache(persist=True)
def load_data():
    df = pd.read_csv(DATA_URL)
    
    return df

df = load_data()

#st.sidebar.markdown('Univariate Analysis')
a = st.sidebar.selectbox('Univariate Analysis', ['Chart 1', 'Chart 2'], key='2')

fig, ax = plt.subplots()
if not st.sidebar.checkbox("Hide", True ,key='4'):
    if a == 'Chart 1':
        st.write('What is the distribution of the Age column in the data set?')
        sns.distplot(df['Age'])
        st.pyplot(fig)
        st.header('Observation:')
        st.subheader('We have Employees mostly between the age of 30 to 45')

    if a == 'Chart 2':
        st.write('What is the distribution of the MothlyIncome column in the data set?')
        sns.distplot(df['MonthlyIncome']) 
        st.pyplot(fig)
        st.header('Observation:')
        st.subheader('Most of the Employees in the company earn between 2000 and 7000 monthly')
        st.subheader('Very few Employees command a higher salary')



a = st.sidebar.selectbox('Bi-variate Analysis', ['Chart 1', 'Chart 2', 'Chart 3'], key='3')

if not st.sidebar.checkbox("Hide", True, key='5'):
    if a == 'Chart 1':
        st.write('Which gender is more likely to leave?')
        #f,ax = plt.subplots()
        new_df = df["Gender"].groupby(df["Attrition"]).value_counts(normalize = True).rename("Percentage of group").reset_index()

        sns.barplot(x = "Attrition", y = "Percentage of group", hue = "Gender", data = new_df)

        vals = ax.get_yticks()
        ax.set_yticklabels(['{:,.0%}'.format(x) for x in vals])

        ax.set(title = "Distribution of gender")
        st.pyplot(fig)
        st.header('Observation:')
        st.subheader('The company has more men than women, and so this plot tells us that men tend to leave the company more but only because they are in a larger number. This also indicates that gender might not be a key factor for employee attrition')

    if a == 'Chart 2':
        st.write('Does distance from home affect attrition rate in employees?')
        sns.barplot(df['Gender'],df['DistanceFromHome'],hue = df['Attrition'])
        st.pyplot(fig)
        st.header('Observation:')
        st.subheader('Distance from home matters more to women employees than men\n Employee are more likely to quit, when DistanceFromHome is above 8 km')

    if a == 'Chart 3':
        st.write('Scatter plot - Monthly Income vs Years at the company')
        sns.scatterplot(x=df['MonthlyIncome'], y=df['YearsAtCompany'], hue=df['Attrition']) 
        st.pyplot(fig)
        st.header('Observation:')
        st.subheader('Most of the Employees in the company earn between 2000 and 7000 monthly')
        st.subheader('Very few Employees command a higher salary')
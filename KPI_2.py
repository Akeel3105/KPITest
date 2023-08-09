# import package
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#from sklearn.linear_model import LinearRegression
#from  sklearn.metrics import mean_squared_error, r2_score
#import time

#Import data

data= pd.read_csv("Amkpi.csv")
#image = Image.open("ui.png")
st.title("AM KPI APP")
#st.image(image, use_column_width = False)

#checking the data
st.write("This is an App to track your KPI Scores")
#check_data= st.checkbox("View Data")
#if check_data:
#   st.write(data.head(3))
#st.write("Lets Check Your KPI Scores")

#sample = input('Enter Your Emp Code: ')
#data.loc[(data['AM Code'] == sample)]

AM_Code=st.text_input('Enter Your Employee Code With WF/WFCH')
Password=st.number_input('Enter Your Password',value=0)
# data1 = data.loc[(data['AM Code'] == AM_Code)]
data1 = data[(data['AM Code'] == AM_Code) & (data['Password'] == Password )]
st.table(data1)

check_data= st.button("View Full FY23 Data")
if check_data:
   st.write(data1.head(3))
# st.dataframe(data1, 100, 200)
# st.dataframe(data1.style.highlight_max(axis=0))
# st.bar_chart(data=data1)
# df[(df['AM Code'] == AM_Code) & (df['Password'] == int(Password) )]


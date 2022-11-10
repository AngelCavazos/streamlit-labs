import streamlit as st
import pandas as pd
#
##LECTURAS DE UN DATAFRAME
#
data = pd.read_csv('dataset.csv')


st.title("Streamlit y Pandas")

st.dataframe(data)
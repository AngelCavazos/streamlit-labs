import streamlit as st
import pandas as pd
import numpy as np
st.title('Streamlit con sidebar')
sidebar= st.sidebar

sidebar.title('Titulo de barra lateral')
sidebar.write('Información de mi sidebar')
st.write('Header de mi app')
st.write('Información de mi app')

if sidebar.checkbox('Show dataframe'):
    chart_data= pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
    st.dataframe(chart_data)
import streamlit as st
import pandas as pd
 
st.title('Streamlit con cache')

data_url='dataset.csv'

@st.cache
def load_data(rows):
    df = pd.read_csv(data_url,nrows=rows)
    return df

data_load_state = st.text('Cargando...')

data= load_data(500)

data_load_state.text('Carga completa')

st.dataframe(data)
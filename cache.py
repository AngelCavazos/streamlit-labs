import streamlit as st
import pandas as pd
# Existencia del manejo de memorias cache


st.title('Streamlit con cache')

#data_url="https://raw.githubusercontent.com/AngelCavazos/streamlit-labs/master/dataset.csv?token=GHSAT0AAAAAAB2XYZDND5XUDKWWE7N2S7M6Y3NF74A"
data_url='https://raw.githubusercontent.com/adsoftsito/streamlit-labs/master/dataset.csv?token=GHSAT0AAAAAAB2NR7KYLAP4VXUGLOVWKVL6Y3NHLEQ'

@st.cache
def load_data(rows):
    df = pd.read_csv(data_url,nrows=rows)
    return df

data_load_state = st.text('Cargando...')

data= load_data(500)

data_load_state.text('Carga completa')

st.dataframe(data)
import streamlit as st
import pandas as pd

st.title('Busqueda de nombres en data frame')

data_url = 'dataset.csv'

@st.cache
def dataload_name(name):
    data = pd.read_csv(data_url)
    filtered_df = data[data.name.str.contains(name)]
    return filtered_df

name= st.text_input('Nombre a buscar: ')
if(name):
    df = dataload_name(name)
    count_row = df.shape[0]
    st.write(f'Total names {count_row}')
    st.dataframe(df)

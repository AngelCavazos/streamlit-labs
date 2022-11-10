import streamlit as st
import pandas as pd

st.title('Busqueda de caja de selección')

data_url = 'dataset.csv'

#load para llenado de lista de caja de selección
@st.cache
def load_data():
    df = pd.read_csv(data_url)
    return df

#Esta es la que filtra
@st.cache
def filtro_sex(sex):
    df = pd.read_csv(data_url)
    filtered = df[df.sex == sex]
    return filtered

data = load_data()

selected_sex = st.selectbox('Sex',data.sex.unique())
btn_filter = st.button('Filter')

if(btn_filter):
    df = filtro_sex(selected_sex)
    count_row = df.shape[0]
    st.write(f'Filas totales {count_row}')
    st.dataframe(df)
    


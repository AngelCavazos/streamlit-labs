import streamlit as st
import pandas as pd

st.title('Busqueda de rangos en indice')

data_url = 'dataset.csv'

@st.cache
def filtro_rango(startid, endid):
    df = pd.read_csv(data_url)
    filtered = df.iloc[startid:endid+1]
    return filtered

start = st.text_input('Id inicial: ')
end = st.text_input('Id final: ')

if st.button('Buscar'):
    df = filtro_rango(int(start),int(end))
    count_row = df.shape[0]
    st.write(f'Filas totales {count_row}')
    st.dataframe(df)



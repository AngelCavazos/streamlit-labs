# Interaccion con usuario
import streamlit as st

st.title('Bienvenida a usuario')
def bienvenida(nombre):
    msj = 'bienvenid@ '+nombre
    return msj

myname= st.text_input('Nombre: ')
#revisa si existe valor
if (myname):
    mensaje = bienvenida(myname)
    st.write(f"mensaje: {mensaje}")
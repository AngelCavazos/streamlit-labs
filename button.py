import streamlit as st

myname = st.text_input('Name: ')

if st.button('Search'):
    st.write(f'Searching {myname}')


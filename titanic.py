import pandas as pd
import streamlit as st
import datetime
titanic_link ='https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
titanic_data = pd.read_csv(titanic_link)

st.title("My Titanic App")
st.subheader('Creado por Angel Cavazos')
#creamos barra lateral
sidebar = st.sidebar
sidebar.title("This is the sidebar.")
sidebar.write("You can add any elements to the sidebar.")


#Calendario para obtener la fecha actual
today = datetime.date.today()
today_date = sidebar.date_input('Current date', today)
st.success('Current date: `%s`' % (today_date))

st.header("Dataset")
agree = sidebar.checkbox("show DataSet Overview ? ")
if agree:
    st.dataframe(titanic_data)

st.header("Data Description")
selected_class = sidebar.radio("Select Class",titanic_data['class'].unique())

st.write("Selected Class:", selected_class)
st.markdown("___")

selected_sex = sidebar.selectbox("Select Sex", titanic_data['sex'].unique())
st.write(f"Selected Option: {selected_sex!r}")

st.markdown("___")

optionals = sidebar.expander("Optional Configurations", True)
fare_select = optionals.slider("Select the Fare",
min_value=float(titanic_data['fare'].min()),
max_value=float(titanic_data['fare'].max()))

subset_fare = titanic_data[(titanic_data['fare'] >= fare_select)]
st.write(f"Number of Records With this Fare {fare_select}: {subset_fare.shape[0]}")
st.markdown("___")
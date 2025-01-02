import streamlit as st
import pandas as pd
import plotly.express as px

        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Header
st.header('Panel de Control de Anuncios de Venta de vehiculos')

# Create a Checkbox for the Histogram
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Histograma de Odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig)

# Create a Checkbox for the Scatter Plot
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Gráfico de Dispersión de Precio vs Odómetro')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig)

import streamlit as st
import pandas as pd
import plotly.express as px

        
car_data = pd.read_csv(r'C:\Users\crist\Documents\Documentos\ds_my_projects\web_aplication\vehicles_us.csv') # leer los datos

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
          
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
# prompt: leer archivo DATOS.csv

import pandas as pd

try:
  df = pd.read_csv('DATOS.csv')
  print(df.head()) # Print the first few rows to verify
except FileNotFoundError:
  print("Error: DATOS.csv not found.")
except Exception as e:
  print(f"An error occurred: {e}")
# prompt: mostrar columnas del archivo DATOS.csv

df.columns
# prompt: mostrar tabla de resultados

df
# prompt: crea una grafica de pastel usando streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Análisis de Datos')
st.header('Inasistencias de los estudiantes de FCA')

# Assuming your DATOS.csv is in the same directory as your Streamlit script
try:
    df = pd.read_csv('DATOS.csv')
    st.write("Data loaded successfully:")
    st.dataframe(df.head())
except FileNotFoundError:
    st.error("Error: DATOS.csv not found.")
    st.stop() # Stop the script if the file is not found
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop() # Stop the script if an error occurs

# Dropdown to select a column
column_name = st.selectbox(
    'Selecciona una columna para graficar:',
    df.columns.tolist()
)

# Create the pie chart
if column_name:
    st.subheader(f'Distribución de {column_name}')

    # Count the occurrences of each unique value in the selected column
    column_counts = df[column_name].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(column_counts, labels=column_counts.index, autopct='%1.1f%%', startangle=140)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

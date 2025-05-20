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
# prompt: crear una grafica de pastel con DATOS.csv usando streamlit

!pip install streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación Streamlit
st.title('Análisis de Datos de Inasistencias')
st.header('Inasistencias de los estudiantes de FCA')

# Cargar los datos
try:
    df = pd.read_csv('DATOS.csv')
    st.write("Datos cargados exitosamente:")
    st.dataframe(df.head()) # Mostrar las primeras filas del DataFrame
except FileNotFoundError:
    st.error("Error: DATOS.csv no encontrado. Por favor, asegúrese de que el archivo está en el directorio correcto.")
except Exception as e:
    st.error(f"Ocurrió un error al cargar el archivo: {e}")

# Verificar si el DataFrame no está vacío para proceder
if 'df' in locals() and not df.empty:
    st.subheader("Gráfica de Pastel")

    # Permitir al usuario seleccionar la columna para la gráfica de pastel
    # Asegurarse de que las columnas son de un tipo adecuado para contar valores (generalmente strings o categorías)
    # Filtramos columnas que podrían no ser adecuadas (ej. IDs únicos, fechas si no se agrupan)
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    # También podemos incluir columnas numéricas si tienen un número limitado de valores únicos (tratarlas como categorías)
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64'] and df[col].nunique() < 50: # Umbral ajustable
             if col not in categorical_cols:
                 categorical_cols.append(col)


    if not categorical_cols:
        st.warning("No se encontraron columnas categóricas o con un número limitado de valores únicos para crear la gráfica de pastel.")
    else:
        column_to_plot = st.selectbox(
            "Seleccione la columna para la gráfica de pastel:",
            categorical_cols
        )

        # Contar las ocurrencias de cada categoría en la columna seleccionada
        counts = df[column_to_plot].value_counts()

        if counts.empty:
            st.warning(f"La columna '{column_to_plot}' no contiene datos para visualizar.")
        else:
            # Crear la gráfica de pastel usando matplotlib
            fig, ax = plt.subplots(figsize=(8, 8))
            ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
            ax.set_title(f'Distribución de {column_to_plot}')
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Mostrar la gráfica en Streamlit
            st.pyplot(fig)
else:
    if 'df' in locals(): # Si df existe pero está vacío
         st.warning("El DataFrame está vacío. No se puede crear una gráfica de pastel.")

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
# prompt: crea un filtro con las columnas 'Edad', 'Licenciatura', 'Promedio', '¿Cuántos dias vas a la escuela?',
#        'Consideras que eres una persona que falta con regularidad',
#        '¿Tus faltas suelen estar justificadas por la escuela?',
#        'Cuantos dias has llegado a faltar por decision propia (sin justificacion o situacion adversa)',
#        'Cual es la razón por la que consideras que faltas',
#        'Hay algun tipo de materia a la que suelas faltar mas' usando streamlit

filter_columns = [
    'Edad',
    'Licenciatura',
    'Promedio',
    '¿Cuántos dias vas a la escuela?',
    'Consideras que eres una persona que falta con regularidad',
    '¿Tus faltas suelen estar justificadas por la escuela?',
    'Cuantos dias has llegado a faltar por decision propia (sin justificacion o situacion adversa)',
    'Cual es la razón por la que consideras que faltas',
    'Hay algun tipo de materia a la que sueles faltar mas'
]

st.header('Filtrar Datos')

# Create filters for each specified column
filtered_df = df.copy()

for col in filter_columns:
    if col in df.columns:
        unique_values = df[col].unique().tolist()
        # Add 'Todos' option to see all values
        unique_values = ['Todos'] + unique_values
        selected_value = st.selectbox(f'Selecciona valor para "{col}":', unique_values)

        if selected_value != 'Todos':
            filtered_df = filtered_df[filtered_df[col] == selected_value]
    else:
        st.warning(f"La columna '{col}' no se encontró en el DataFrame.")

st.subheader('Datos Filtrados')
st.dataframe(filtered_df)

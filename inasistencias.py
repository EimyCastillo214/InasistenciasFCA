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
# prompt: Crear una grafica de pastel la columna Licenciatura de DATOS.csv

# Count the occurrences of each category in the 'Licenciatura' column
if not df.empty:
    if 'Licenciatura' in df.columns:
        counts_licenciatura = df['Licenciatura'].value_counts()

        if not counts_licenciatura.empty:
            # Create the pie chart for Licenciatura
            plt.figure(figsize=(8, 8)) # Optional: Adjust figure size
            plt.pie(counts_licenciatura, labels=counts_licenciatura.index, autopct='%1.1f%%', startangle=140)
            plt.title('Distribución de Licenciatura') # Set the title of the chart
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()
        else:
            print("La columna 'Licenciatura' está vacía.")
    else:
        print("La columna 'Licenciatura' no se encuentra en el DataFrame.")
else:
  print("DataFrame is empty. Cannot create a pie chart.")

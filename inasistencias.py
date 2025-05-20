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

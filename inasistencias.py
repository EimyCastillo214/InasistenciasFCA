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
#        'Hay algun tipo de materia a la que suelas faltar mas'

filtro_columnas = ['Edad', 'Licenciatura', 'Promedio', '¿Cuántos dias vas a la escuela?',
                    'Consideras que eres una persona que falta con regularidad',
                    '¿Tus faltas suelen estar justificadas por la escuela?',
                    'Cuantos dias has llegado a faltar por decision propia (sin justificacion o situacion adversa)',
                    'Cual es la razón por la que consideras que faltas',
                    'Hay algun tipo de materia a la que suelas faltar mas']

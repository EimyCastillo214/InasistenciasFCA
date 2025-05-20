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
# prompt: crea un filtro en donde aparezcan los nombres de las columnas y crea una grafica de pastel con los resultados de la columna seleccionada

import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt

# Dropdown to select a column
column_selector = widgets.Dropdown(
    options=df.columns.tolist(),
    description='Select Column:',
    disabled=False,
)

# Output widget for the plot
output = widgets.Output()

def display_pie_chart(column_name):
    with output:
        output.clear_output(wait=True) # Clear previous plot
        if column_name in df.columns:
            # Count the occurrences of each unique value in the selected column
            column_counts = df[column_name].value_counts()

            plt.figure(figsize=(8, 8))
            plt.pie(column_counts, labels=column_counts.index, autopct='%1.1f%%', startangle=140)
            plt.title(f'Distribution of {column_name}')
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()
        else:
            print(f"Column '{column_name}' not found.")

# Link the dropdown value to the display function
widgets.interactive(display_pie_chart, column_name=column_selector)

# Display the widgets
display(column_selector, output)

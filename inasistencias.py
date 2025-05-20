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
# prompt: crear una grafica de pastel con DATOS.csv

import matplotlib.pyplot as plt

# Count the occurrences of each category in a relevant column
# Replace 'your_column_name' with the actual column you want to visualize
# For a pie chart, this column should contain categorical data
# Example: If you have a column named 'attendance_status' with values like 'Present', 'Absent', 'Late'
# counts = df['attendance_status'].value_counts()

# Assuming you want to visualize the counts of values in the 'df' DataFrame
# You'll need to choose a specific column to create the pie chart from.
# Let's assume, for the sake of example, that you want to visualize the counts of
# different values in the first column of your DataFrame.
# You should replace 'df.columns[0]' with the actual column name you want to use.
if not df.empty:
  column_to_plot = df.columns[0] # Replace with the actual column name
  counts = df[column_to_plot].value_counts()

  # Create the pie chart
  plt.figure(figsize=(8, 8)) # Optional: Adjust figure size
  plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
  plt.title(f'Distribución de {column_to_plot}') # Set the title of the chart
  plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.show()
else:
  print("DataFrame is empty. Cannot create a pie chart.")

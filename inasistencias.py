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
# prompt: hAZME UNA GRAFICA circulares PARA CADA COLUMNA En un solo documento

import matplotlib.pyplot as plt

# Create a figure and a set of subplots
fig, axes = plt.subplots(nrows=(len(df_csv_filtered.columns) + 1) // 2, ncols=2, figsize=(15, 5 * ((len(df_csv_filtered.columns) + 1) // 2)))
axes = axes.flatten() # Flatten the 2D array of axes for easier iteration

# Generate a pie chart for each column
for i, column in enumerate(df_csv_filtered.columns):
    value_counts = df_csv_filtered[column].value_counts()
    labels = value_counts.index
    sizes = value_counts.values

    axes[i].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    axes[i].set_title(f'Distribución de {column}')

# Hide any unused subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout() # Adjust layout to prevent titles overlapping
plt.show()

# prompt: Agregame el numero de valores que representa cada porcentaje A LAS GRAFICAS

# Create a figure and a set of subplots
fig, axes = plt.subplots(nrows=(len(df_csv_filtered.columns) + 1) // 2, ncols=2, figsize=(15, 5 * ((len(df_csv_filtered.columns) + 1) // 2)))
axes = axes.flatten() # Flatten the 2D array of axes for easier iteration

# Generate a pie chart for each column
for i, column in enumerate(df_csv_filtered.columns):
    value_counts = df_csv_filtered[column].value_counts()
    labels = value_counts.index
    sizes = value_counts.values

    # Combine labels with counts
    labels_with_counts = [f'{label} ({count})' for label, count in zip(labels, sizes)]

    axes[i].pie(sizes, labels=labels_with_counts, autopct='%1.1f%%', startangle=140)
    axes[i].set_title(f'Distribución de {column}')

# Hide any unused subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout() # Adjust layout to prevent titles overlapping
plt.show()

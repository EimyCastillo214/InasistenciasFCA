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
# prompt: Crear una grafica de pastel la columna Licenciatura de DATOS.csv usando streamlit

# Mostrar la gráfica de pastel para la columna 'Licenciatura' en Streamlit
if 'df' in locals() and not df.empty and 'Licenciatura' in df.columns and not df['Licenciatura'].empty:
    st.subheader("Gráfica de Pastel por Licenciatura")
    counts_licenciatura = df['Licenciatura'].value_counts()

    if not counts_licenciatura.empty:
        fig_licenciatura, ax_licenciatura = plt.subplots(figsize=(8, 8))
        ax_licenciatura.pie(counts_licenciatura, labels=counts_licenciatura.index, autopct='%1.1f%%', startangle=140)
        ax_licenciatura.set_title('Distribución de Licenciatura')
        ax_licenciatura.axis('equal')
        st.pyplot(fig_licenciatura)
    else:
        st.warning("La columna 'Licenciatura' no contiene datos para visualizar.")
elif 'df' in locals() and not df.empty and 'Licenciatura' not in df.columns:
     st.warning("La columna 'Licenciatura' no se encuentra en el archivo DATOS.csv.")
elif 'df' in locals() and df.empty:
     st.warning("El DataFrame está vacío. No se puede crear la gráfica de pastel para Licenciatura.")

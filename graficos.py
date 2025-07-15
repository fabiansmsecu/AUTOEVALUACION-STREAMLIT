import pandas as pd
import plotly.express as px
import streamlit as st

def generar_grafico(promedios):
    """
    Genera un gráfico de barras con los promedios de cumplimiento por dominio.
    """
    # Convertir diccionario a DataFrame
    df = pd.DataFrame(list(promedios.items()), columns=["Dominio", "Promedio"])
    
    # Crear gráfico de barras
    fig = px.bar(
        df,
        x="Dominio",
        y="Promedio",
        color="Promedio",
        color_continuous_scale=["red", "yellow", "green"],
        title="Nivel de Cumplimiento por Dominio",
        text_auto=True
    )
    
    fig.update_layout(
        xaxis_title="Dominio",
        yaxis_title="Promedio / 20",
        coloraxis_colorbar=dict(title="Promedio"),
    )
    
    st.plotly_chart(fig, use_container_width=True)

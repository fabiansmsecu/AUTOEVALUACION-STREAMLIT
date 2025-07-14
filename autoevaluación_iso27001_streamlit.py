# autoevaluacion_iso27001_streamlit.py

import streamlit as st
import pandas as pd
from docx import Document
from io import BytesIO
from datetime import datetime
import plotly.express as px
import openai
import os

# -------------------------------
# CONFIGURAR DEEPSEEK
# -------------------------------
openai.api_key = os.getenv("DEEPSEEK_API_KEY")
openai.api_base = "https://api.deepseek.com"

if not openai.api_key:
    st.error("No se encontró la clave API de DeepSeek en los secrets de Streamlit.")
    st.stop()

# -------------------------------
# DATOS DE LA RÚBRICA
# -------------------------------
rubricas = {
    'Gestión de Acceso': {
        '¿Existen políticas y procedimientos documentados para la gestión de accesos?': {
            1: 'No se tienen políticas ni procedimientos documentados.',
            2: 'Existen políticas y procedimientos, pero no están completamente documentados.',
            3: 'Políticas y procedimientos documentados y regularmente revisados.',
            4: 'Cumplen con todos los requisitos establecidos por ISO 27001.',
            5: 'Implementación avanzada que supera los requisitos estándar.'
        }
    },
    'Seguridad Física y Ambiental': {
        '¿Existen medidas de seguridad física para proteger los equipos críticos?': {
            1: 'No hay medidas de seguridad física implementadas.',
            2: 'Medidas físicas parciales o insuficientes.',
            3: 'Medidas físicas implementadas regularmente.',
            4: 'Cumple totalmente con ISO 27001.',
            5: 'Implementación avanzada que supera los requisitos estándar.'
        }
    }
}

# -------------------------------
# FUNCIONES
# -------------------------------

def procesar_calificaciones(calificaciones):
    promedios = {
        aspecto: sum(calificacion for pregunta, calificacion in lista) / len(lista)
        for aspecto, lista in calificaciones.items()
    }
    return promedios

def generar_texto_ia(promedios):
    # Armar prompt dinámico
    prompt = f"""
Eres un auditor experto en ISO 27001. Con base en estos resultados de autoevaluación:
{promedios}

Genera un texto profesional que incluya:
- Fortalezas encontradas
- Debilidades
- Recomendaciones técnicas específicas según ISO 27001
- Riesgos asociados a las debilidades
- Plan de acción priorizado

Responde en lenguaje técnico y profesional.
"""

    response = openai.ChatCompletion.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Eres un auditor experto en ISO 27001."},
            {"role": "user", "content": prompt}
        ]
    )

    texto_ia = response.choices[0].message.content
    return texto_ia

def generar_informe_word(calificaciones, promedios, texto_ia,
                         nombre_compania, nombre_evaluador, fecha_evaluacion):
    buffer = BytesIO()
    doc = Document()

    # Portada
    doc.add_heading('Informe de Autoevaluación ISO 27001', 0)
    doc.add_paragraph(f'Compañía: {nombre_compania}')
    doc.add_paragraph(f'Evaluador: {nombre_evaluador}')
    doc.add_paragraph(f'Fecha: {fecha_evaluacion}')
    doc.add_page_break()

    # Resultados Detallados
    doc.add_heading('Detalles de la Evaluación', level=1)
    for aspecto, preguntas in calificaciones.items():
        doc.add_heading(aspecto, level=2)
        for pregunta, calificacion in preguntas:
            descripcion = rubricas[aspecto][pregunta][calificacion]
            p = doc.add_paragraph()
            p.add_run(f'{pregunta}: ').bold = True
            p.add_run(f'{calificacion} - {descripcion}')
    
    doc.add_page_break()

    # Promedios
    doc.add_heading('Promedios por Dominio', level=1)
    for aspecto, promedio in promedios.items():
        doc.add_paragraph(f"{aspecto}: {promedio:.2f} / 5")

    doc.add_page_break()

    # Análisis de IA
    doc.add_heading('Análisis y Recomendaciones IA', level=1)
    doc.add_paragraph(texto_ia)

    doc.save(buffer)
    buffer.seek(0)
    return buffer

def generar_grafico(promedios):
    df = pd.DataFrame(list(promedios.items()), columns=["Dominio", "Promedio"])
    fig = px.bar(
        df,
        x="Dominio",
        y="Promedio",
        color="Promedio",
        color_continuous_scale=["red", "yellow", "green"],
        range_y=[0, 5],
        title="Resultados por Dominio"
    )
    st.plotly_chart(fig)

# -------------------------------
# MAIN APP
# -------------------------------

def main():
    st.title("Autoevaluación ISO 27001 - Con Recomendaciones IA (DeepSeek)")

    nombre_compania = st.text_input("Nombre de la Compañía Evaluada", "")
    nombre_evaluador = st.text_input("Nombre del Evaluador", "")
    fecha_evaluacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    calificaciones = {key: [] for key in rubricas.keys()}

    for aspecto, preguntas in rubricas.items():
        st.subheader(aspecto)
        for pregunta, opciones in preguntas.items():
            seleccion = st.selectbox(
                pregunta,
                [f"{k}: {v}" for k, v in opciones.items()],
                key=f"{aspecto}_{pregunta}"
            )
            calificacion = int(seleccion.split(":")[0])
            calificaciones[aspecto].append((pregunta, calificacion))

    if st.button("Generar Informe"):
        if not nombre_compania or not nombre_evaluador:
            st.error("Completa todos los campos antes de continuar.")
        else:
            promedios = procesar_calificaciones(calificaciones)
            generar_grafico(promedios)
            
            # Llamar a DeepSeek para generar texto IA
            texto_ia = generar_texto_ia(promedios)

            # Generar informe Word
            buffer = generar_informe_word(
                calificaciones,
                promedios,
                texto_ia,
                nombre_compania,
                nombre_evaluador,
                fecha_evaluacion
            )
            
            st.success("¡Informe generado exitosamente!")
            st.download_button(
                label="Descargar Informe en Word",
                data=buffer,
                file_name=f"Informe_ISO27001_{nombre_compania}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

if __name__ == "__main__":
    main()

# autoevaluacion_iso27001_streamlit.py

import streamlit as st
import pandas as pd
import openai
import os
from datetime import datetime
from docx import Document
from io import BytesIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import plotly.express as px

# Configurar DeepSeek
openai.api_key = os.getenv("DEEPSEEK_API_KEY")
openai.api_base = "https://api.deepseek.com"

if not openai.api_key:
    st.error("No se encontró la clave API de DeepSeek en las variables de entorno.")
    st.stop()

# Definir las descripciones de las rúbricas específicas para cada pregunta
rubricas = {
    'Gestión de Acceso': {
        '¿Existen políticas y procedimientos documentados para la gestión de accesos?': {
            1: 'No se tienen políticas ni procedimientos documentados.',
            2: 'Existen políticas y procedimientos, pero no están completamente documentados.',
            3: 'Políticas y procedimientos documentados y regularmente revisados.',
            4: 'Cumplen con todos los requisitos establecidos por ISO 27001.',
            5: 'Implementación avanzada que supera los requisitos estándar.'
        },
        '¿Se implementan controles de autenticación fuertes para acceder a sistemas críticos?': {
            1: 'No se implementan controles de autenticación.',
            2: 'Se implementan controles de autenticación de manera limitada o inconsistente.',
            3: 'Controles de autenticación fuertes implementados de manera regular.',
            4: 'Cumple totalmente con los requisitos de autenticación de ISO 27001.',
            5: 'Implementación avanzada de controles de autenticación que supera los requisitos estándar.'
        }
    },
    'Seguridad Física y Ambiental': {
        '¿Existen medidas de seguridad física para proteger los equipos críticos del departamento de sistemas?': {
            1: 'No hay medidas de seguridad física implementadas.',
            2: 'Medidas de seguridad física parciales o insuficientes.',
            3: 'Medidas de seguridad física implementadas regularmente.',
            4: 'Cumple totalmente con los requisitos de seguridad física de ISO 27001.',
            5: 'Implementación avanzada que supera los requisitos estándar.'
        },
        '¿Se realizan controles ambientales para proteger la infraestructura tecnológica (temperatura, humedad, etc.)?': {
            1: 'No se realizan controles ambientales.',
            2: 'Controles ambientales realizados de manera irregular o insuficiente.',
            3: 'Controles ambientales implementados regularmente.',
            4: 'Cumple totalmente con los requisitos de controles ambientales de ISO 27001.',
            5: 'Implementación avanzada que supera los requisitos estándar.'
        }
    }
}

def procesar_calificaciones(calificaciones):
    promedios = {
        aspecto: sum(calificacion for pregunta, calificacion in lista) / len(lista)
        for aspecto, lista in calificaciones.items()
    }
    promedios_ponderados = {
        aspecto: (promedio / 5) * 20 
        for aspecto, promedio in promedios.items()
    }
    calificacion_final = sum(promedios_ponderados.values()) / len(promedios_ponderados) * 5
    return promedios, promedios_ponderados, calificacion_final

def generar_informe_word(calificaciones, promedios_ponderados, calificacion_final,
                         nombre_compania, nombre_evaluador, destinatario, fecha_evaluacion):
    buffer = BytesIO()
    document = Document()
    document.add_heading('Informe de Autoevaluación ISO 27001', 0)
    document.add_paragraph(f'Compañía Evaluada: {nombre_compania}')
    document.add_paragraph(f'Evaluador: {nombre_evaluador}')
    document.add_paragraph(f'Fecha de Evaluación: {fecha_evaluacion}')
    document.add_page_break()

    document.add_heading('Detalles de la Evaluación', level=1)
    for aspecto, preguntas in calificaciones.items():
        document.add_heading(aspecto, level=2)
        for pregunta, calificacion in preguntas:
            descripcion = rubricas[aspecto][pregunta][calificacion]
            p = document.add_paragraph()
            p.add_run(f'{pregunta}: ').bold = True
            p.add_run(f'{calificacion} - {descripcion}')

    document.add_page_break()
    document.add_heading('Resultados', level=1)
    for aspecto, calificacion in promedios_ponderados.items():
        document.add_paragraph(f"{aspecto}: {calificacion:.2f} puntos sobre 20")

    document.add_paragraph(f"Calificación Final: {calificacion_final:.2f} / 100")

    document.save(buffer)
    buffer.seek(0)

    st.success(f"Informe generado correctamente. Descárgalo abajo:")
    st.download_button(
        label="Descargar Informe en Word",
        data=buffer,
        file_name=f"Informe_ISO27001_{nombre_compania}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

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

def main():
    st.title("Autoevaluación ISO 27001 con DeepSeek AI")

    # Formulario de datos generales
    nombre_compania = st.text_input("Nombre de la Compañía Evaluada", "")
    nombre_evaluador = st.text_input("Nombre del Evaluador", "")
    destinatario = st.text_input("Correo Electrónico del Destinatario", "")
    fecha_evaluacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Evaluación
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
        if not nombre_compania or not nombre_evaluador or not destinatario:
            st.error("Por favor, completa todos los campos antes de continuar.")
        else:
            promedios, promedios_ponderados, calificacion_final = procesar_calificaciones(calificaciones)
            generar_grafico(promedios)
            generar_informe_word(
                calificaciones,
                promedios_ponderados,
                calificacion_final,
                nombre_compania,
                nombre_evaluador,
                destinatario,
                fecha_evaluacion
            )
            
    # Opcional: integración con DeepSeek para generar preguntas dinámicas
    if st.button("Generar Preguntas con IA (DeepSeek)"):
        prompt = "Genera 3 preguntas en escala Likert sobre Seguridad Física en la norma ISO 27001."
        response = openai.ChatCompletion.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Eres un auditor experto en ISO 27001."},
                {"role": "user", "content": prompt}
            ]
        )
        st.subheader("Preguntas sugeridas por IA:")
        st.write(response.choices[0].message.content)

if __name__ == "__main__":
    main()

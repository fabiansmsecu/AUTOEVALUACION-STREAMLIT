import streamlit as st
from datetime import datetime
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import matplotlib.pyplot as plt
import numpy as np
import openai
import os

# Leer la clave API desde una variable de entorno
openai.api_key = os.getenv('OPENAI_API_KEY')

# Verificar si la clave API fue obtenida correctamente
if not openai.api_key:
    st.error("No se encontró la clave API de OpenAI en las variables de entorno.")
    st.stop()

# Definir las descripciones de las rúbricas específicas para cada pregunta
rubricas = {
    'Gestión de Acceso': {
        '¿Existen políticas y procedimientos documentados para la gestión de accesos?': {
            1: 'No se tienen políticas ni procedimientos documentados...',
            2: 'Existen políticas y procedimientos, pero no están completamente documentados...',
            3: 'Políticas y procedimientos documentados y regularmente revisados...',
            4: 'Cumplen con todos los requisitos establecidos por ISO 27001...',
            5: 'Implementación avanzada que supera los requisitos estándar...'
        },
        '¿Se implementan controles de autenticación fuertes para acceder a sistemas críticos?': {
            1: 'No se implementan controles de autenticación...',
            2: 'Se implementan controles de autenticación de manera limitada o inconsistente...',
            3: 'Controles de autenticación fuertes implementados de manera regular...',
            4: 'Cumple totalmente con los requisitos de autenticación de ISO 27001...',
            5: 'Implementación avanzada de controles de autenticación que supera los requisitos estándar...'
        }
    },
    'Seguridad Física y Ambiental': {
        '¿Existen medidas de seguridad física para proteger los equipos críticos del departamento de sistemas?': {
            1: 'No hay medidas de seguridad física implementadas...',
            2: 'Medidas de seguridad física parciales o insuficientes...',
            3: 'Medidas de seguridad física implementadas regularmente...',
            4: 'Cumple totalmente con los requisitos de seguridad física de ISO 27001...',
            5: 'Implementación avanzada que supera los requisitos estándar...'
        },
        '¿Se realizan controles ambientales para proteger la infraestructura tecnológica (temperatura, humedad, etc.)?': {
            1: 'No se realizan controles ambientales...',
            2: 'Controles ambientales realizados de manera irregular o insuficiente...',
            3: 'Controles ambientales implementados regularmente...',
            4: 'Cumple totalmente con los requisitos de controles ambientales de ISO 27001...',
            5: 'Implementación avanzada que supera los requisitos estándar...'
        }
    },
    'Gestión de Comunicaciones y Operaciones': {
        '¿Se utilizan procedimientos seguros para la transmisión de datos sensibles dentro y fuera de la organización?': {
            1: 'No se utilizan procedimientos seguros para la transmisión de datos...',
            2: 'Procedimientos seguros utilizados de manera parcial o inconsistente...',
            3: 'Procedimientos seguros utilizados regularmente...',
            4: 'Cumple totalmente con los requisitos de seguridad de transmisión de datos de ISO 27001...',
            5: 'Implementación avanzada que supera los requisitos estándar...'
        },
        '¿Se realizan pruebas periódicas de vulnerabilidades y evaluaciones de riesgos en la infraestructura de redes?': {
            1: 'No se realizan pruebas de vulnerabilidades ni evaluaciones de riesgos...',
            2: 'Pruebas de vulnerabilidades realizadas de manera limitada o irregular...',
            3: 'Pruebas de vulnerabilidades y evaluaciones de riesgos realizadas regularmente...',
            4: 'Cumple totalmente con los requisitos de pruebas y evaluaciones de ISO 27001...',
            5: 'Implementación avanzada que supera los requisitos estándar...'
        }
    },
    'Control de Acceso a la Información': {
        '¿Se implementan controles para limitar el acceso a la información confidencial y crítica dentro del departamento de sistemas?': {
            1: 'No se implementan controles de acceso a la información...',
            2: 'Controles de acceso implementados de manera limitada o inconsistente...',
            3: 'Controles de acceso implementados regularmente...',
            4: 'Cumple totalmente con los requisitos de control de acceso de ISO 27001...',
            5: 'Implementación avanzada que supera los requisitos estándar...'
        },
        '¿Se establecen y mantienen políticas para la clasificación y etiquetado de la información dentro del departamento de sistemas?': {
            1: 'No se establecen ni mantienen políticas para clasificación y etiquetado...',
            2: 'Políticas de clasificación y etiquetado establecidas pero no mantenidas adecuadamente...',
            3: 'Políticas de clasificación y etiquetado mantenidas regularmente...',
            4: 'Cumple totalmente con los requisitos de clasificación y etiquetado de ISO 27001...',
            5: 'Implementación avanzada que supera los requisitos estándar...'
        }
    },
    'Gestión de Incidentes de Seguridad de la Información': {
        '¿Existe un procedimiento documentado para la gestión de incidentes de seguridad de la información?': {
            1: 'No hay procedimiento documentado para la gestión de incidentes...',
            2: 'Procedimiento documentado pero no actualizado o implementado de manera limitada...',
            3: 'Procedimiento documentado y regularmente revisado e implementado...',
            4: 'Cumple totalmente con los requisitos de gestión de incidentes de ISO 27001...',
            5: 'Implementación avanzada que supera los requisitos estándar...'
        },
        '¿Se realiza capacitación y simulacros periódicos para el personal sobre cómo responder a incidentes de seguridad de la información?': {
            1: 'No se realizan capacitaciones ni simulacros sobre incidentes de seguridad...',
            2: 'Capacitaciones y simulacros realizados de manera irregular o insuficiente...',
            3: 'Capacitaciones y simulacros realizados regularmente...',
            4: 'Cumple totalmente con los requisitos de capacitación y simulacros de ISO 27001...',
            5: 'Implementación avanzada que supera los requisitos estándar...'
        }
    }
}

def generar_informe_word(calificaciones, promedios_ponderados, calificacion_final, nombre_compania, nombre_evaluador, destinatario, fecha_evaluacion):
    document = Document()
    document.add_heading('Informe de Autoevaluación de Cumplimiento de la Norma ISO 27001', 0)
    document.add_paragraph(f'Compañía Evaluada: {nombre_compania}', style='Title')
    document.add_paragraph(f'Evaluador: {nombre_evaluador}', style='Heading 3')
    document.add_paragraph(f'Fecha de Evaluación: {fecha_evaluacion}', style='Heading 3')
    document.add_page_break()

    document.add_heading('Anexo I: Detalles de la Evaluación', level=1)
    for aspecto, preguntas in calificaciones.items():
        document.add_heading(aspecto, level=2)
        for pregunta, calificacion in preguntas:
            descripcion = rubricas[aspecto][pregunta][calificacion]
            p = document.add_paragraph()
            p.add_run(f'{pregunta}: ').bold = True
            p.add_run(f'{calificacion} - {descripcion}')

    document.add_paragraph(f'Calificación final del departamento de sistemas: {calificacion_final:.2f} / 100')
    document.save('Autoevaluacion_Norma_ISO_27001.docx')
    st.success("El informe se ha generado correctamente en Autoevaluacion_Norma_ISO_27001.docx")

def procesar_calificaciones(calificaciones):
    promedios = {aspecto: sum(valores[1] for valores in lista) / len(lista) for aspecto, lista in calificaciones.items()}
    promedios_ponderados = {aspecto: (promedio / 5) * 20 for aspecto, promedio in promedios.items()}
    calificacion_final = sum(promedios_ponderados.values()) / len(promedios_ponderados) * 5
    return promedios_ponderados, calificacion_final


def main():
    st.title("Evaluación de Cumplimiento ISO 27001")
    calificaciones = {key: [] for key in rubricas.keys()}

    for aspecto, preguntas in rubricas.items():
        st.subheader(aspecto)
        for pregunta, opciones in preguntas.items():
            seleccion = st.selectbox(pregunta, [f"{k}: {v}" for k, v in opciones.items()])
            calificacion = int(seleccion.split(":")[0])
            calificaciones[aspecto].append((pregunta, calificacion))

    if st.button("Generar Informe"):
        nombre_compania = st.text_input("Nombre de la Compañía Evaluada", "")
        nombre_evaluador = st.text_input("Nombre y Apellido del Evaluador", "")
        destinatario = st.text_input("Nombre y Apellido del Destinatario", "")
        fecha_evaluacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if not nombre_compania or not nombre_evaluador or not destinatario:
            st.error("Debe completar todos los campos para generar el informe.")
        else:
            promedios_ponderados, calificacion_final = procesar_calificaciones(calificaciones)
            generar_informe_word(calificaciones, promedios_ponderados, calificacion_final, nombre_compania, nombre_evaluador, destinatario, fecha_evaluacion)

if __name__ == "__main__":
    main()

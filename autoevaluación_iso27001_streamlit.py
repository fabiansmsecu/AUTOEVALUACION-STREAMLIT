import streamlit as st
from datetime import datetime
from rubricas import rubricas
from informe import generar_informe_word
from graficos import generar_grafico

def procesar_calificaciones(calificaciones):
    """
    Calcula promedios por dominio y la calificación final.
    """
    promedios = {
        aspecto: sum(calificacion for _, calificacion in preguntas) / len(preguntas)
        for aspecto, preguntas in calificaciones.items()
    }
    promedios_ponderados = {
        aspecto: (promedio / 5) * 20
        for aspecto, promedio in promedios.items()
    }
    calificacion_final = sum(promedios_ponderados.values()) / len(promedios_ponderados) * 5
    return promedios_ponderados, calificacion_final

def main():
    st.set_page_config(page_title="Autoevaluación ISO 27001", layout="wide")
    st.title("Autoevaluación ISO 27001 - Seguridad de la Información")

    calificaciones = {key: [] for key in rubricas.keys()}

    nombre_compania = st.text_input("Nombre de la Compañía Evaluada", "")
    nombre_evaluador = st.text_input("Nombre y Apellido del Evaluador", "")
    destinatario = st.text_input("Destinatario del Informe", "")
    fecha_evaluacion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    st.markdown("---")

    for aspecto, preguntas in rubricas.items():
        st.subheader(aspecto)

        for pregunta, opciones in preguntas.items():
            opciones_list = [f"{k}: {v['descripcion']}" for k, v in opciones.items()]
            
            seleccion = st.selectbox(
                pregunta,
                ["Seleccione una opción"] + opciones_list,
                key=f"{aspecto}_{pregunta}"
            )

            if seleccion != "Seleccione una opción":
                calificacion = int(seleccion.split(":")[0])
                calificaciones[aspecto].append((pregunta, calificacion))
            else:
                calificaciones[aspecto].append((pregunta, None))

    if st.button("Generar Informe"):
        # Validar que no haya preguntas sin responder
        for aspecto, preguntas in calificaciones.items():
            for pregunta, calificacion in preguntas:
                if calificacion is None:
                    st.error(f"Falta contestar la pregunta: {pregunta} en el aspecto {aspecto}.")
                    return

        promedios_ponderados, calificacion_final = procesar_calificaciones(calificaciones)
        
        # Mostrar gráfico
        generar_grafico(promedios_ponderados)

        # Generar informe Word
        buffer = generar_informe_word(
            calificaciones,
            promedios_ponderados,
            calificacion_final,
            nombre_compania,
            nombre_evaluador,
            destinatario,
            fecha_evaluacion
        )

        st.success("✅ Informe generado correctamente. ¡Descárgalo aquí!")

        st.download_button(
            label="📥 Descargar Informe Word",
            data=buffer,
            file_name=f"Informe_ISO27001_{nombre_compania}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

if __name__ == "__main__":
    main()

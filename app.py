import streamlit as st
import requests
from datetime import datetime
from googletrans import Translator
import time

#* Inicializar el traductor
translator = Translator()

#* Función para obtener el versículo del día desde una API
def obtener_versiculo():
    response = requests.get("https://beta.ourmanna.com/api/v1/get/?format=text&order=random")
    if response.status_code == 200:
        versiculo = response.text.strip()
        try:
            traduccion = translator.translate(versiculo, src='en', dest='es')
            return traduccion.text
        except Exception as e:
            return f"No se pudo traducir el versículo de hoy. Error: {str(e)}"
    else:
        return "No se pudo obtener el versículo de hoy."

#* Función para obtener una frase motivacional desde ZenQuotes API
def obtener_frase_motivacional():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        frase = data[0]["q"]
        try:
            traduccion = translator.translate(frase, src='en', dest='es')
            return traduccion.text
        except Exception as e:
            return f"No se pudo traducir la frase motivacional de hoy. Error: {str(e)}"
    else:
        return "No se pudo obtener la frase motivacional de hoy."

#* CSS personalizado para estilizar componentes de Streamlit con fondo oscuro
def agregar_estilos():
    st.markdown(
        """
        <style>
        .main {
            background-color: #121212;
            color: #e0e0e0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .header {
            text-align: center;
            font-size: 36px;
            color: #76c7c0;
        }
        .title {
            text-align: center;
            font-size: 46px;
            color: #fff;
        }
        .subheader {
            text-align: center;
            font-size: 28px;
            color: #f8c3c3;
        }
        .content {
            font-size: 18px;
            margin: 20px;
            padding: 20px;
            border-radius: 10px;
            background-color: #1e1e1e;
            color: #e0e0e0;
            box-shadow: 0 0 10px rgba(0,0,0,0.3);
        }
        hr {
            border: 0;
            height: 1px;
            background: #333;
            margin: 20px 0;
        }
        a {
            color: #76c7c0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
#* Configurar la aplicación de Streamlit
st.markdown("<h1 class='title'>📖 Frase y Versículo del Día</h1><hr>", unsafe_allow_html=True)

#* Agregar estilos personalizados
agregar_estilos()

#* Mostrar el versículo del día
st.markdown("<div class='header'>Versículo del Día</div>", unsafe_allow_html=True)
versiculo = obtener_versiculo()
st.markdown(f"<div class='content'>{versiculo}</div>", unsafe_allow_html=True)

#* Mostrar la frase motivacional del día
st.markdown("<div class='subheader'>Frase Motivacional del Día</div>", unsafe_allow_html=True)
frase = obtener_frase_motivacional()
st.markdown(f"<div class='content'>{frase}</div>", unsafe_allow_html=True)

#* Agregar un pie de página
st.markdown(
    """
    <hr>
    <div style='text-align: center; color: #e0e0e0;'>
        <p>Powered by <a href='https://www.streamlit.io' target='_blank'>Streamlit</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

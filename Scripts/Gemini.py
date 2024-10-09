import streamlit as st
import google.generativeai as genai

# Configuramos el lugar de la API
genai.configure(api_key="AIzaSyA2DyBAOkP7xjp8TcHrHI1Xvv4QKShUkSw")

# Cargamos el modelo
gemini_model = genai.GenerativeModel('gemini-1.5-flash')

# Función de respuesta de "texto"
def generate_response(qtn):
    try:
        res = gemini_model.generate_content(qtn)
        return res.text
    except Exception as e:
        return f"Ocurrió un error: {e}"

# Función para limpiar el campo de texto
def clear_text_input():
    st.session_state.input_text = ""

# Nombramos la pestaña web
st.set_page_config(page_title="Ecosystem Tech Bot", page_icon="🤖", layout="centered")

# Aplicamos estilo CSS personalizado para el fondo degradado y botones
st.markdown(
    """
    <style>
    /* Fondo degradado */
    body {
        background-color: #291947;
    }
    div.stApp {
        background-color: #291947;
        color: #FFFFFF;
    }

    /* Títulos y textos */
    h1, h2, h3, p {
        color: #FFFFFF;
    }

    /* Botones */
    .stButton button {
        background-color: #49DDC0;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px;
        width: 100%;  /* Esto asegura que el botón ocupe el 100% de su contenedor */
    }

    .stButton button:hover {
        background-color: #3cc0a7;
        color: white;
    }

    /* Entrada de texto */
    .css-1y4p8pa input {
        background-color: #283593;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Agregamos el logo o imagen en lugar del título
st.image("imagenes\logos editables_LOGO 1-2.png", caption="Ecosystem Tech Bot", use_column_width=True)

# Definimos el layout de la aplicación
st.markdown("<h4 style='text-align: center;color: #49DDC0;'>¡Hazme una pregunta y te responderé! 🤖</h4>", unsafe_allow_html=True)

# Definimos la entrada/pregunta con un valor por defecto en el estado de la sesión
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""

# Entrada de usuario con un campo de texto personalizado
input_text = st.text_input(
    "¿En qué puedo ayudarte?", 
    value=st.session_state.input_text, 
    placeholder="Escribe tu pregunta aquí...", 
    key="user_input",
    label_visibility="collapsed"
)

# Creamos un contenedor con columnas para los botones, centrados y alineados
col1, col2, col3 = st.columns([1, 1, 1])

with col2:  # Centramos las columnas para los botones
    with st.container():
        button_preg = st.button("Generar Respuesta", help="Haz clic para obtener la respuesta")

with col3:
    with st.container():
        nuev_preg = st.button("Nueva Pregunta", help="Haz clic para limpiar la entrada", on_click=clear_text_input)

# Mostramos la respuesta en una caja diferenciada
if button_preg:
    if input_text:
        output = generate_response(input_text)
        st.markdown("<h3 style='text-align: center; color: #49DDC0;'>...</h3>", unsafe_allow_html=True)
        st.markdown(f"<div style='border: 1px solid #ddd; padding: 10px; border-radius: 5px;'>{output}</div>", unsafe_allow_html=True)
    else:
        st.write("<div style='color: red;'>Por favor ingresa una pregunta.</div>", unsafe_allow_html=True)

# Pie de página
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FFFFFF;'>Desarrollado con 💻 por Ecosystem Tech</p>", unsafe_allow_html=True)

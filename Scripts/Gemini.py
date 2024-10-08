import streamlit as st
import google.generativeai as g_gen

# Configuramos el lugar de la API
g_gen.configure(api_key="AIzaSyA2DyBAOkP7xjp8TcHrHI1Xvv4QKShUkSw")

# Cargamos el modelo
gemini_model = g_gen.get_model('models/gemini-pro')

# Función de respuesta de "texto"
def generate_response(qtn):
    try:
        res = gemini_model.generate_content(qtn)
        return res.text
    except Exception as e:
        return f"Ocurrió un error: {e}"

# Nombramos la pestaña web
st.set_page_config(page_title="QnA")

# Agregamos el título
st.title("Ecosystem Application")

# Definimos entrada/preguntas
input_text = st.text_input("Ingresa tus preguntas:")

# Agregamos botón
submit = st.button("Generar respuesta")

if submit:
    if input_text:
        output = generate_response(input_text)
        st.write(output)
    else:
        st.write("Por favor ingresa una pregunta.")


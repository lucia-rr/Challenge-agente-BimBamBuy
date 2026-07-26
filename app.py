import streamlit as st
from src.consulta import obtener_respuesta

st.set_page_config(page_title="BimBam Buy - Soporte", page_icon="", layout="centered")

st.markdown("""
<style>
/* Fondo blanco global */
.stApp {
    background-color: #ffffff !important;
}

/* Ocultar footer */
footer {visibility: hidden !important;}

/* Texto unificado en negro */
.stMarkdown, .stMarkdown p, .stMarkdown li, .stChatMessageContent p, label, div {
    color: #1a1a1a !important;
    font-size: 16px !important;
}

/* Encabezados en negro */
h1 { color: #000000 !important; }

/* Chat input con fondo blanco y borde sutil */
div[data-testid="stChatInput"] {
    background-color: #ffffff !important;
    border: 1px solid #cccccc !important;
    border-radius: 8px !important;
}

div[data-testid="stChatInput"] textarea {
    background-color: transparent !important;
    color: #1a1a1a !important;
}

/* Mensajes sin bordes */
.stChatMessage {
    background-color: transparent !important;
    border: none !important;
}

/* Línea separadora sutil */
hr {
    border-color: #cccccc !important;
}

/* Ocultar header */
header {visibility: hidden !important;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>BimBam Buy</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1em; color: #1a1a1a;'>Asistente virtual de soporte para pagos, garantías y postventa.</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; border-top: 1px solid #cccccc; margin: 20px 0;'>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
    
    bienvenida = """¡Hola! Soy tu asistente de BimBam Buy.

Puedo apoyarte con información sobre:
- Métodos de pago disponibles
- Problemas con pagos rechazados o pendientes
- Proceso de garantías, devoluciones y reembolsos

¿En qué puedo ayudarte hoy?"""
    
    st.session_state.messages.append({"role": "assistant", "content": bienvenida})

for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=None):
        st.markdown(message["content"])

if pregunta := st.chat_input("¿En qué duda puedo ayudarte en BimBam Buy?"):
    st.session_state.messages.append({"role": "user", "content": pregunta})
    with st.chat_message("user", avatar=None):
        st.markdown(pregunta)
    
    with st.chat_message("assistant", avatar=None):
        with st.spinner("Buscando información..."):
            respuesta = obtener_respuesta(pregunta)
            st.markdown(respuesta)
    
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
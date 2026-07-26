import streamlit as st
from src.consulta import obtener_respuesta

st.set_page_config(page_title="BimBam Buy - Soporte", page_icon="", layout="centered")


st.markdown("""
<style>
/* Fondo oscuro en TODOS los contenedores posibles */
.stApp, 
.stApp > div,
[data-testid="stAppViewContainer"],
[data-testid="stMainBlockContainer"],
[data-testid="stBottomBlockContainer"],
.stChatInputContainer,
[data-testid="stChatInputContainer"],
[data-testid="stChatInputContainer"] > div,
[data-testid="stBottomBlock"],
[data-testid="stBottomBlock"] > div,
[data-testid="stChatInput"] {
    background-color: #0e1117 !important;
}

/* Eliminar avatares completamente */
[data-testid="stChatMessageAvatar"] {
    display: none !important;
    visibility: hidden !important;
    width: 0 !important;
    height: 0 !important;
}

/* Mensajes sin avatar */
[data-testid="stChatMessage"] {
    padding-left: 1rem !important;
}

/* Chat input sin fondo blanco */
[data-testid="stChatInput"] textarea {
    background-color: #1a1d23 !important;
    color: #E0E0E0 !important;
}

[data-testid="stChatInput"] {
    background-color: #1a1d23 !important;
    border: 1px solid #333 !important;
    border-radius: 8px !important;
}

/* Texto en gris claro */
.stMarkdown, .stMarkdown p, .stMarkdown li, .stChatMessageContent p, label, div {
    color: #E0E0E0 !important;
}

/* Ocultar footer y header */
footer, header {
    visibility: hidden !important;
    display: none !important;
}

/* Línea separadora */
hr {
    border-color: #333 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>BimBam Buy</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1em; color: #E0E0E0;'>Asistente virtual de soporte para pagos, garantías y postventa.</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; border-top: 1px solid #333; margin: 20px 0;'>", unsafe_allow_html=True)

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
    with st.chat_message(message["role"], avatar=""):
        st.markdown(message["content"])

if pregunta := st.chat_input("¿En qué duda puedo ayudarte en BimBam Buy?"):
    st.session_state.messages.append({"role": "user", "content": pregunta})
    with st.chat_message("user", avatar=""):
        st.markdown(pregunta)
    
    with st.chat_message("assistant", avatar=""):
        with st.spinner("Buscando información..."):
            respuesta = obtener_respuesta(pregunta)
            st.markdown(respuesta)
    
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
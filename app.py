import streamlit as st
from src.consulta import obtener_respuesta

st.set_page_config(page_title="BimBam Buy - Soporte", page_icon="🛒", layout="centered")

st.markdown("""
<style>
/* FONDO OSCURO EN ABSOLUTAMENTE TODOS LOS CONTENEDORES */
.stApp, 
.stApp > div,
[data-testid="stAppViewContainer"],
[data-testid="stMainBlockContainer"],
[data-testid="stBottomBlockContainer"],
[data-testid="stBottomBlock"],
[data-testid="stChatInputContainer"],
[data-testid="stChatInputContainer"] > div,
[data-testid="stChatInput"],
[data-testid="stChatInput"] > div,
[data-testid="stChatInput"] textarea,
[data-testid="stChatMessage"],
[data-testid="stChatMessage"] > div,
section.main > div,
div.element-container,
div.stChatMessage,
div[data-testid="stVerticalBlock"] {
    background-color: #0e1117 !important;
}

/* ELIMINAR AVATARES */
[data-testid="stChatMessageAvatar"] {
    display: none !important;
}

/* CHAT INPUT SIN BORDES BLANCOS */
[data-testid="stChatInput"] {
    background-color: #1a1d23 !important;
    border: 1px solid #333 !important;
    border-radius: 8px !important;
}

[data-testid="stChatInput"] textarea {
    background-color: #1a1d23 !important;
    color: #E0E0E0 !important;
    border: none !important;
}

/* TEXTO GRIS CLARO */
.stMarkdown, .stMarkdown p, .stMarkdown li, .stChatMessageContent p, label, div {
    color: #E0E0E0 !important;
}

/* OCULTAR FOOTER Y HEADER */
footer, header, .st-emotion-cache-1y4h80 {
    display: none !important;
    visibility: hidden !important;
}

/* SIN BORDES */
hr, .stDivider {
    border-color: #333 !important;
}

/* ELIMINAR SOMBRAS Y BORDES BLANCOS */
div[data-testid="stChatInput"] {
    box-shadow: none !important;
}

/* CONTENEDOR PRINCIPAL SIN PADDING BLANCO */
.main .block-container {
    padding-top: 1rem !important;
    background-color: #0e1117 !important;
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
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if pregunta := st.chat_input("¿En qué duda puedo ayudarte en BimBam Buy?"):
    st.session_state.messages.append({"role": "user", "content": pregunta})
    with st.chat_message("user"):
        st.markdown(pregunta)
    
    with st.chat_message("assistant"):
        with st.spinner("Buscando información..."):
            respuesta = obtener_respuesta(pregunta)
            st.markdown(respuesta)
    
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
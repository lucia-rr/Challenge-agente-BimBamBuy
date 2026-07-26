import streamlit as st
from src.consulta import obtener_respuesta


st.set_page_config(page_title="BimBam Buy - Soporte", page_icon="🛒", layout="centered")


st.markdown("""
<style>

.stApp {
    background-color: #0e1117;
}


footer {visibility: hidden;}

.stMarkdown, .stMarkdown p, .stMarkdown li {
    color: #E0E0E0 !important;
    font-size: 16px !important;
}


h1 { color: #FFFFFF !important; }


[data-testid="stChatAvatar"] {
    display: none !important;
}


div[data-testid="stChatInput"] {
    background-color: #1a1d23 !important;
    border: 1px solid #333 !important;
    border-radius: 8px !important;
}

div[data-testid="stChatInput"] textarea {
    background-color: transparent !important;
    color: #E0E0E0 !important;
}


.stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
    background-color: #1a1d23 !important;
    border-radius: 8px !important;
    padding: 10px !important;
}


.stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
    background-color: #0e1117 !important;
}


.stChatMessage {
    border: none !important;
}


hr {
    border-color: #333 !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center;'>BimBam Buy</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1em;'>Asistente virtual de soporte para pagos, garantías y postventa.</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0; border-top: 1px solid #333; margin: 20px 0;'>", unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state.messages = []


bienvenida = """¡Hola! Soy tu asistente de BimBam Buy 🛒. ¡Estoy listo para ayudarte!

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
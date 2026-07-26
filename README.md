Agente de Soporte BimBam Buy.-

Asistente virtual de atención al cliente basado en Inteligencia Artificial, especializado en resolver dudas sobre métodos de pago, garantías, reembolsos y postventa para **BimBam Buy**. 

El sistema utiliza una arquitectura **RAG (Retrieval-Augmented Generation)** para garantizar que las respuestas sean precisas, basadas estrictamente en la documentación oficial de la empresa, evitando alucinaciones del modelo.

Características Principales.-

- **Respuestas basadas en contexto:** Utiliza documentos PDF oficiales (Métodos de pago y Garantías) como fuente de la verdad.
- **Multilingüe:** Detecta y responde en el mismo idioma en el que el usuario realiza la consulta.
- **Seguridad y Control:** Prompting estructurado para mantener al agente enfocado exclusivamente en su rol de soporte.
- **Interfaz Conversacional:** Interfaz web limpia y minimalista construida con Streamlit.

Stack Tecnológico.-

- **Lenguaje:** Python 3.11+
- **Framework Web:** Streamlit
- **Orquestación de LLM:** LangChain (Classic & Community)
- **Modelo de Lenguaje (LLM):** Cohere (`command-a-03-2025`)
- **Embeddings:** Cohere (`embed-multilingual-v3.0`)
- **Base de Datos Vectorial:** FAISS (CPU)
- **Extracción de texto:** PyPDF

Estructura del Proyecto.-

── app.py                  # Interfaz de usuario en Streamlit
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno locales (NO subir a GitHub)
├── .gitignore              # Archivos ignorados por Git
├── data/                   # Documentos PDF fuente
│   ├── pf_metodo_pago.pdf
│   └── manual_garantia.pdf
├── db/                     # Base de datos vectorial FAISS (indexada)
│   └── faiss_index/
└── src/                    # Lógica del agente
    ├── ingestion.py        # Script para procesar PDFs y crear la DB vectorial
    ├── consulta.py         # Lógica de LangChain, RAG y conexión con Cohere
    └── vector_store.py     # Utilidades para la base de datos

Enlace de interes: https://challenge-agente-bimbambuy-hhhy5wu4tr9fqeuqv3hsoc.streamlit.app/
Fotos de evidencia de funcionamiento: 
<img width="817" height="516" alt="prueba3" src="https://github.com/user-attachments/assets/0e63f8d0-c4e7-4a47-a53a-4c719a9f15b8" />
<img width="869" height="418" alt="prueba2" src="https://github.com/user-attachments/assets/c6d40468-1153-485c-9760-a1ab22fac352" />
<img width="1110" height="552" alt="Prueba1" src="https://github.com/user-attachments/assets/fb1a0c7e-3658-427b-a495-4fb614c3d499" />


NOTA.- Este repositorio conforma parte del challenge para pasar a la siguietne parte del programa de Alura y ONE

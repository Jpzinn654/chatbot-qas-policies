import streamlit as st
from utils.extract_pdf import *
from utils.extract_word import *
from models.load_model import *

def process_uploaded_file(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        return extract_text_pdf(uploaded_file)
    elif file_extension == 'docx':
        return extract_text_word(uploaded_file)
    else:
        return "Formato de arquivo não suportado. Por favor, envie um PDF ou DOCX."

model, tokenizer, nlp = load_model()

st.title("Question Answering sobre Documentos")
st.sidebar.header("Faça o upload de um documento")

uploaded_file = st.sidebar.file_uploader("Escolha um arquivo PDF ou DOCX", type=["pdf", "docx"])

if "messages" not in st.session_state:
    st.session_state.messages = []

if uploaded_file:
    text = process_uploaded_file(uploaded_file)
    
    question = st.text_input("Digite sua pergunta")

    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        
        result = nlp(question=question, context=text)
        answer = result['answer']
        
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"**Você:** {message['content']}")
            else:
                st.markdown(f"**Assistente:** {message['content']}")

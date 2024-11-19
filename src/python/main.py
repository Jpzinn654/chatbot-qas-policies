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

if uploaded_file:
    text = process_uploaded_file(uploaded_file)

    st.header("Pergunte sobre o documento")
    question = st.text_input("Digite sua pergunta")

    if question:
        result = nlp(question=question, context=text)
        st.write(f"Resposta: {result['answer']}")
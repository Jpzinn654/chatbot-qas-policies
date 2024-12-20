# Projeto: ChatBot Perguntas e Respostas Baseada em Documentos com LLM

Este projeto é uma aplicação que utiliza Modelos de Linguagem de Grande Escala (LLM) para ler documentos em formato PDF ou DOCX e responder perguntas baseadas no conteúdo desses documentos. O objetivo principal é permitir que o usuário envie documentos e obtenha respostas precisas relacionadas às informações contidas neles, utilizando as capacidades avançadas de entendimento e processamento de linguagem natural (PNL) dos LLMs.

## Video do Projeto

https://github.com/user-attachments/assets/7f770d91-96bf-47c0-9fe8-52b059536925

## Sobre o Projeto

O objetivo deste projeto é permitir a interação inteligente com documentos em formato PDF e DOCX por meio de uma interface simples. A aplicação carrega o documento enviado, extrai o texto e utiliza um modelo de linguagem (como o GPT-3 ou GPT-4) para fornecer respostas às perguntas feitas pelo usuário, com base no conteúdo do documento carregado.

### Funcionalidades:
- Carregar arquivos PDF ou DOCX para leitura.
- Análise de conteúdo e extração de texto.
- Perguntas e respostas baseadas nas informações extraídas do documento.
- Interface simples e intuitiva para interação.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento da aplicação.
- **Streamlit**: Framework para criação da interface de usuário web.
- **PyPDF2 / pdfplumber**: Bibliotecas para extrair texto de arquivos PDF.
- **python-docx**: Biblioteca para extrair texto de arquivos DOCX.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- **Python 3.x** ou superior
- **pip** (gerenciador de pacotes do Python)

## Instalação

### 1. Clonar o Repositório

Primeiro, clone este repositório em sua máquina:

```bash
git clone https://github.com/Jpzinn654/chatbot-qas-policies.git
```

### 2. Criar e Ativar o Ambiente Virtual

Recomenda-se usar um ambiente virtual para gerenciar as dependências do projeto:
```bash
python3 -m venv env
source env/bin/activate  # Para sistemas Linux/macOS
env\Scripts\activate  # Para sistemas Windows
```

### 3. Instalar as Dependências

Instale todas as dependências necessárias:

```bash
pip install -r requirements.txt
```
**Nota:** O arquivo requirements.txt deve conter todas as bibliotecas que o projeto depende, como openai, streamlit, pypdf2, python-docx, etc.

## Como Rodar

Para rodar a aplicação, basta executar o seguinte comando:

```bash
cd src\python
streamlit run app.py
```
Isso irá iniciar a aplicação no seu navegador padrão, normalmente acessível em http://localhost:8501.

## Como Usar

### Passo 1: Enviar o Documento
1. Abra a aplicação no navegador.
2. Na interface, clique no botão para carregar o arquivo.
3. Selecione o arquivo em formato PDF ou DOCX de sua escolha.

### Passo 2: Fazer Perguntas
Após o documento ser carregado e processado:
1. Digite a pergunta que você deseja fazer sobre o conteúdo do documento.
2. O modelo de linguagem (LLM) irá buscar informações no texto extraído e fornecer uma resposta baseada nas informações contidas no documento.

### Exemplos de Perguntas
- "Qual é a data de validade do contrato?"
- "Quais são as condições para o reembolso?"
- "Quem são os responsáveis pela assinatura do documento?

## Contribuindo
Contribuições são bem-vindas! Caso deseje contribuir para o projeto, siga estas etapas:

1. Faça o fork deste repositório.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Faça o commit das suas alterações (git commit -m 'Adicionando nova funcionalidade').
4. Envie para o repositório remoto (git push origin feature/nova-feature).
5. Crie um Pull Request explicando suas alterações.

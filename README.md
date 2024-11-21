# Projeto TP2 - Parte 1: FastAPI
### **Descrição**
Este projeto utiliza o framework FastAPI para construir duas aplicações simples que integram modelos da biblioteca HuggingFace para as seguintes funcionalidades:

* Geração de texto: Utilizando o modelo GPT-2.
* Tradução de texto: Utilizando o modelo Helsinki-NLP/opus-mt-en-fr para traduzir textos do inglês para o francês.

### **Requisitos**
* Python 3.8 ou superior
* Dependências listadas em requirements.txt

### **Dependências**
* FastAPI: Framework
* Transformers: Biblioteca da HuggingFace para uso de modelos de NLP.

# Como Executar
Passo 1: Clone o repositório
~~~
  git clone https://github.com/seu-repositorio.git
  cd tp2_datadriven_parte1
~~~
Passo 2: Crie e ative o ambiente virtual
~~~
python -m venv .venv
.venv/Scripts/activate  # Windows
source .venv/bin/activate  # Linux/Mac
~~~
Passo 3: Instale as dependências
~~~
pip install -r requirements.txt
~~~

Passo 4: Execute a aplicação
~~~
cd parte_1_fast_api
python main.py
~~~

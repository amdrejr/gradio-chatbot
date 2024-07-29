# gradio-chatbot
 Front-end de chatbot com Gradio


## Passos para rodar o projeto
Primeiro, crie uma venv:

```bash
python -m venv venv
```
Ative a venv:

```bash
.\venv\Scripts\activate
```

Depois, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Para funcionar no local, também é necessário criar um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```bash
AZURE_OPENAI_API_KEY="codigo_chave"
AZURE_OPENAI_ENDPOINT="url_do_endpoint"
```

Por fim, rode o projeto:

```bash
python .\main.py
```

## Editar para seu contexto
Para enquadrar ao contexto do que fizeram, é só alterar o arquivo `utils/openai_connect.py` adicionando suas funções na onde está comentado.

Podem clonar o projeto e fazer as alterações necessárias a vontade.

## Deploy da aplicação
Antes, é necessário subir o projeto para o GitHub.

Costumo utilizar a plataforma [Render](https://render.com/). Uma vez conectado e com sua conta do Github vinculada, basta seguir os passos:
- Em dashboard, clicar no botão `+ New`
- Selecione a opção `Web Service`
- Selecione o repositório do projeto
- Em **Build Command**, colocar `pip install -r requirements.txt`
- Em **Start Command**, colocar `uvicorn main:app --host 0.0.0.0 --port 8000`
- em **Instance Type**, selecione `Free`
- Na parte de **Environment Variables**, adicionar as variáveis de ambiente, igual você fez no arquivo .env explicado a cima. Os valores não precisam estar entre aspas `"`
- Clique em **Deploy Web Service**


Pronto! Seu chatbot está no ar! 🚀
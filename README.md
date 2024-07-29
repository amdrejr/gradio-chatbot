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
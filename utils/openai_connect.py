import os

from langchain_openai import AzureOpenAIEmbeddings
from openai import AzureOpenAI

# Iniciando variáveis que serão usadas durante o processo de RAG e Chat
# Nome dos modelos no endpoint
embedding_model_name = 'embeddings-start'
openai_model_name = 'projeto-start'

# Iniciando o client de embeddings
encoder = AzureOpenAIEmbeddings(
    azure_deployment=embedding_model_name,
    openai_api_version="2023-05-15",
)


# Lendo a base de conhecimento


# Criando base usando Embeddings


# Salvando base de conhecimento com RAG



# Iniciando client de resposta da Azure OpenAI
client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = "2024-02-01",
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT") 
)

def message_openai(message: str):
    # Criando prompt com as informações da base de conhecimento
    prompt = f"""
    Responda a seguinte pergunta: {message}
    """
    
    completion = client.chat.completions.create(
        model=openai_model_name,  # e.g. gpt-35-instant
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    
    return completion.choices[0].message.content
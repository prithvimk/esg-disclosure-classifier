import ollama
from ollama import AsyncClient
import os

from config.schemas import ESGQuantData, ESGQuantResponse
from config.llm_prompts import USER_PROMPT_QUALITATIVE, USER_PROMPT_QUANTITATIVE, SYSTEM_PROMPT

LLM_HOST = os.getenv('LLM_HOST', "http://localhost:11434")
LLM_PORT = os.getenv('LLM_PORT', '11434')
LLM_MODEL = os.getenv('LLM_MODEL', 'deepseek-r1:7b')
EMBEDDING_MODELS = os.getenv('EMBEDDING_MODELS', 'nomic-embed-text:v1.5')






async def generate_response() -> dict:
    '''
    Function to use the apt prompt and generate response from selected model.
    '''
    async with AsyncClient(host=LLM_HOST) as client:
        response = await client.chat(
            model=LLM_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT_QUANTITATIVE},
            ],
            format=ESGResponse.model_json_schema()
        )

        return response.message.content



def generate_response() -> dict:
    '''
    Function to use the apt prompt and generate response from selected model.
    '''
    response = ollama.chat(
    model="deepseek-r1:7b",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT_QUANTITATIVE},
    ],
    format=ESGResponse.model_json_schema()
)
    return response.message.content
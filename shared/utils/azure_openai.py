from openai import AzureOpenAI
from shared.configs.azure_config import (
    api_key, end_point, api_version
)

client = AzureOpenAI(
    api_key = api_key,
    api_version = api_version,
    azure_endpoint = end_point
)

def run_llm(prompt: str):
    response = client.chat.completions.create(
        model = 'gpt-4o',
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
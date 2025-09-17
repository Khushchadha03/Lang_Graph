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


def run_llm_with_system(system_prompt: str, user_prompt: str) -> str:
    """Send prompts with system context to Azure OpenAI."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content or ""
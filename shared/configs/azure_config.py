import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

api_key: Optional[str] = os.getenv("AZURE_OPENAI_GPT_4O_API_KEY")
end_point: Optional[str] = os.getenv("AZURE_OPENAI_GPT_4O_ENDPOINT")
api_version: Optional[str] = os.getenv("AZURE_OPENAI_GPT_4O_API_VERSION")
import os
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "openai").lower()

if PROVIDER == "groq":
    API_KEY = os.getenv("GROQ_API_KEY")
    API_BASE = "https://api.groq.com/openai/v1"
    MODEL_NAME = "mixtral-8x7b-32768"
else:
    API_KEY = os.getenv("OPENAI_API_KEY")
    API_BASE = "https://api.openai.com/v1"
    MODEL_NAME = "gpt-3.5-turbo"

from configparser import ConfigParser, ExtendedInterpolation
import os

# Lê o arquivo config.ini (deve estar no mesmo diretório)
parser = ConfigParser(interpolation=ExtendedInterpolation())
parser.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# Provider: "groq" ou "openai"
PROVIDER = parser.get('DEFAULT', 'provider').lower()

if PROVIDER == 'groq':
    API_KEY = parser.get('DEFAULT', 'groq_api_key')
    API_BASE = 'https://api.groq.com/openai/v1'
    MODEL_NAME = 'llama3-8b-8192'
else:
    API_KEY = parser.get('DEFAULT', 'openai_api_key')
    API_BASE = 'https://api.openai.com/v1'
    MODEL_NAME = 'gpt-3.5-turbo'

# Optional: exibir para debug
print(f"⚙️ Provider: {PROVIDER}")
print(f"⚙️ Model:    {MODEL_NAME}")
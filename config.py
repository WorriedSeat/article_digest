from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # OpenRouter
    openrouter_api_key:str
    openrouter_base_url:str = "https://openrouter.ai/api/v1"
    openrouter_model_name:str = "google/gemma-4-31b-it:free"
    
    # Telegram
    # tg_bot_token:str
    
    # LangSmith
    langsmith_api_key:str
    langsmith_project:str = "article_digest"
    
    # Agent
    # arxiv_tags:dict[str, str] = {}
    
    # .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
        
settings = Settings()
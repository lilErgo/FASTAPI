import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


# Класс для управления настройками приложения через Pydantic
@lru_cache
class Settings(BaseSettings):
    REDIS_PORT: int               # Порт для подключения к Redis
    REDIS_PASSWORD: str           # Пароль для подключения к Redis
    BASE_URL: str                 # Базовый URL приложения
    REDIS_HOST: str               # Хост Redis-сервера
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Корневая директория проекта

    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: int


    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", "redis://cool_pass@172.28.182.219:6388/0") # NEW
    CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", "redis://cool_pass@172.28.182.219:6388/0") # NEW


    model_config = SettingsConfigDict(env_file=f"{BASE_DIR}/.env")# Указание файла с переменными окружения

    @property
    def DATABASE_URL_asyncpg(self):

        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    @property
    def DATABASE_URL_psycopg(self):
        
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def REDIS_URL(self):
        # Формирование URL для подключения к Redis
        return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/0"





# Создание экземпляра настроек
settings = Settings()
# print(settings.BASE_DIR) # отладка параметра




# ssl_options = {"ssl_cert_reqs": ssl.CERT_NONE} # у меня не https

# celery_app = Celery(
#                         "celery_worker",
#                         broker=settings.REDIS_URL, 
#                         backend=settings.REDIS_URL
#                     )
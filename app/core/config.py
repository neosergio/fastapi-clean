from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    REGION_NAME: str
    DYNAMODB_TABLE: str
    ENDPOINT_URL: str

    class Config:
        env_file = ".env"


settings = Settings()

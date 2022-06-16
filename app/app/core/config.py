from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    PROJECT_NAME: str
    VPIC_API_URL: AnyHttpUrl

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()

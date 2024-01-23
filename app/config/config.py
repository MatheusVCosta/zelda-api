# from functools import lru_cache, lru

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Teste"
    version: str = "1.0.0"
    app_env: str = "development"
    zelda_api: str = "https://zelda.fanapis.com/api/"
    firebase_uri: str = "https://zelda-guide.firebaseio.com"
    # database_url: str
    # certifix_url: str
    # certifix_token: str = "xxxxxxxxxxxxxxxx"
    # username_docs: str = "bm-integration"
    # password_docs: str = "bm-integration-pass"

    class Config:
        env_file = ".env"


# class TestSettings(Settings):
#     app_name: str = "Balance Manager Integration"
#     api_key: str
#     version: str = "1.0.0"
#     app_env: str = "test"
#     database_url: str
#     certifix_url: str
#     certifix_token: str = "xxxxxxxxxxxxxxxx"
#     username_docs: str = "bm-integration"
#     password_docs: str = "bm-integration-pass"

#     class Config:
#         env_file = ".env.test"


uses_test_env = False


# @lru_cach
def get_settings():
    # if uses_test_env:
        # return TestSettings()
    return Settings()

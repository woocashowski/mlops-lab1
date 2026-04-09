from settings import Settings
from main import export_envs


def test_settings():
    export_envs("test")
    settings = Settings()
    assert settings.APP_NAME == "mlops-lab1"
    assert settings.ENVIRONMENT == "test"
    assert settings.API_KEY == "fake-api-key-test"


# ENVIRONMENT=test
# APP_NAME=mlops-lab1
# API_KEY=fake-api-key-test

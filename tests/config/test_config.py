import os

import pytest
from config import get_settings


@pytest.mark.usefixtures("load_env_variables")
def test_config_values():
    settings = get_settings()
    assert settings.secret == os.getenv("SECRET")
    assert settings.default_expiration_time == int(os.getenv("DEFAULT_EXPIRATION_TIME"))
    assert settings.algorithm == os.getenv("ALGORITHM")

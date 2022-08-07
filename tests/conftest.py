import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient

from src.entrypoints.main import app


@pytest.fixture(scope="session")
def load_env_variables():
    load_dotenv()

@pytest.fixture(scope="session")
def client():
    return TestClient(app)

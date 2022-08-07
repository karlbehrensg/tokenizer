import pytest
from pydantic.error_wrappers import ValidationError

from src.domain.schemas import TokenCreate, TokenResponse
from config import get_settings

settings = get_settings()


class TestToken:
    payload = {"data": "test"}
    expire=False
    expireTime=15

    def test_valid_token_create_default(self):
        token_create = TokenCreate(payload=self.payload)
        assert token_create.payload == self.payload
        assert token_create.expire == True
        assert token_create.expireTime == settings.default_expiration_time

    def test_valid_token_create(self):
        token_create = TokenCreate(payload=self.payload, expire=self.expire, expireTime=self.expireTime)
        assert token_create.payload == self.payload
        assert token_create.expire == self.expire
        assert token_create.expireTime == self.expireTime

    def test_not_valid_expire_type(self):
        with pytest.raises(ValidationError):
            TokenCreate(payload=self.payload, expire="invalid type")

    def test_not_valid_expire_time_type(self):
        with pytest.raises(ValidationError):
            TokenCreate(payload=self.payload, expireTime="invalid type")

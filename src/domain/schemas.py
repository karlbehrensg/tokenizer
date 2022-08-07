from pydantic import BaseModel
from typing import Optional
from config import get_settings

settings = get_settings()


class TokenCreate(BaseModel):
    payload: dict
    expireTime: Optional[int] = settings.default_expiration_time
    expire: Optional[bool] = True


class TokenResponse(BaseModel):
    token: str

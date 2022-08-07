from datetime import datetime, timedelta
from jose import JWTError, jwt
from config import get_settings

settings = get_settings()


class Tokenizer:
    SECRET_KEY = settings.secret
    ALGORITHM = settings.algorithm

    def create_token(self, payload: dict, expires_delta: int, expire: bool):
        to_encode = payload.copy()
        expire_at = datetime.utcnow() + timedelta(minutes=expires_delta)
        if expire:
            to_encode.update({"exp": expire_at})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

from fastapi import HTTPException, status
from datetime import datetime, timedelta
from jose import JWTError, ExpiredSignatureError, jwt
from config import get_settings

settings = get_settings()


class Tokenizer:
    SECRET_KEY = settings.secret
    ALGORITHM = settings.algorithm
    expired_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token has expired",
    )
    signature_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Signature verification failed"
    )

    def create_token(self, payload: dict, expires_delta: int, expire: bool):
        to_encode = payload.copy()
        expire_at = datetime.utcnow() + timedelta(minutes=expires_delta)
        if expire:
            to_encode.update({"exp": expire_at})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def verify(self, token: str):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            payload.pop("exp", None)
            return payload
        except ExpiredSignatureError:
            raise self.expired_exception
        except JWTError:
            raise self.signature_exception

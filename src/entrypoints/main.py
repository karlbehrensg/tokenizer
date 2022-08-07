from fastapi import FastAPI, Depends

from src.domain import schemas
from src.utils.tokenizer import Tokenizer

app = FastAPI()


@app.post("/api/create", status_code=201, response_model=schemas.Token)
async def create_token(
    data: schemas.TokenCreate, tokenizer: Tokenizer = Depends(Tokenizer)
):
    token = tokenizer.create_token(data.payload, data.expireTime, data.expire)
    response = schemas.Token(token=token)
    return response


@app.get("/api/verify", status_code=200, response_model=schemas.VerifiedToken)
async def verify_token(
    token: schemas.Token, tokenizer: Tokenizer = Depends(Tokenizer)
):
    payload = tokenizer.verify(token=token.token)
    response = schemas.VerifiedToken(payload=payload)
    return response

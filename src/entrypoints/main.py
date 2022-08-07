from fastapi import FastAPI, Depends

from src.domain import schemas
from src.utils.tokenizer import Tokenizer

app = FastAPI()


@app.post("/create", status_code=201, response_model=schemas.TokenResponse)
async def register_user(
    data: schemas.TokenCreate, tokenizer: Tokenizer = Depends(Tokenizer)
):
    token = tokenizer.create_token(data.payload, data.expireTime, data.expire)
    return {"token": token}

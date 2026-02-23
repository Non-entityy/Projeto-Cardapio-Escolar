from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "SUPER_SECRET_KEY"
ALGORITHM = "HS256"

router = APIRouter(prefix="/api/auth")

class LoginData(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginData):
    if data.username == "admin" and data.password == "admin123":
        role = "admin"
    elif data.username == "user" and data.password == "user123":
        role = "viewer"
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = jwt.encode({
        "sub": data.username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(hours=4)
    }, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token, "role": role}

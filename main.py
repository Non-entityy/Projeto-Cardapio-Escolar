
from fastapi import FastAPI
from .database import engine
from . import models
from .routers import meals

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cardápio Escolar API")

app.include_router(meals.router)

@app.get("/")
def root():
    return {"message": "API Cardápio Escolar rodando"}

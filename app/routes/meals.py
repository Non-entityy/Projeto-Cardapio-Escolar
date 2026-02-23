from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models

router = APIRouter(prefix="/api/meals")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_meals(db: Session = Depends(get_db)):
    return db.query(models.Meal).all()

@router.post("/")
def create_meal(meal: dict, db: Session = Depends(get_db)):
    if not meal.get("name") or meal.get("calories") is None:
        raise HTTPException(status_code=400, detail="Dados inválidos")
    new_meal = models.Meal(name=meal["name"], calories=meal["calories"])
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal

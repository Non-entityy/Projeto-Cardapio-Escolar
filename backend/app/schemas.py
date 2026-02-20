
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date

class MealBase(BaseModel):
    name: str
    calories: int
    food_group: Optional[str] = None
    substitutes: Optional[str] = None
    allergens: Optional[str] = None

class MealCreate(MealBase):
    pass

class MealResponse(MealBase):
    id: UUID

    class Config:
        orm_mode = True

class WeekCreate(BaseModel):
    start_date: date

class WeekResponse(BaseModel):
    id: UUID
    start_date: date

    class Config:
        orm_mode = True

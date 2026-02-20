
import uuid
from sqlalchemy import Column, String, Integer, Text, Date, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .database import Base
import enum

class MealType(str, enum.Enum):
    cafe = "cafe"
    almoco = "almoco"
    lanche = "lanche"

class Meal(Base):
    __tablename__ = "meals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(150), nullable=False)
    calories = Column(Integer, nullable=False)
    food_group = Column(String(100))
    substitutes = Column(Text)
    allergens = Column(Text)

class Week(Base):
    __tablename__ = "weeks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    start_date = Column(Date, nullable=False, unique=True)
    days = relationship("WeekDay", back_populates="week", cascade="all, delete")

class WeekDay(Base):
    __tablename__ = "week_days"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    week_id = Column(UUID(as_uuid=True), ForeignKey("weeks.id"))
    day_index = Column(Integer, nullable=False)

    week = relationship("Week", back_populates="days")
    meals = relationship("DayMeal", back_populates="week_day", cascade="all, delete")

class DayMeal(Base):
    __tablename__ = "day_meals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    week_day_id = Column(UUID(as_uuid=True), ForeignKey("week_days.id"))
    meal_id = Column(UUID(as_uuid=True), ForeignKey("meals.id"))
    type = Column(Enum(MealType), nullable=False)

    week_day = relationship("WeekDay", back_populates="meals")
    meal = relationship("Meal")

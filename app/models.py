from sqlalchemy import Column, String, Integer
import uuid
from .database import Base

class Meal(Base):
    __tablename__ = "meals"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    calories = Column(Integer, nullable=False)

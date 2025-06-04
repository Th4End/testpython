from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Discount(Base):
    __tablename__ = "discount"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import validates
from . import Base, Session

class Vehicle(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    battery_range = Column(Integer, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    
    # [Add all your Vehicle class methods here]
from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from sqlalchemy.orm import validates
from . import Base, Session

class Vehicle(Base):
    __tablename__ = 'vehicles'
    __table_args__ = (
        CheckConstraint('price > 0', name='check_price_positive'),
        CheckConstraint('battery_range > 0', name='check_range_positive'),
        CheckConstraint('stock_quantity >= 0', name='check_stock_non_negative')
    )

    id = Column(Integer, primary_key=True)
    model = Column(String(100), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    battery_range = Column(Integer, nullable=False)
    stock_quantity = Column(Integer, nullable=False, default=0)

    @validates('model')
    def validate_model(self, key, model):
        if not model or not model.strip():
            raise ValueError("Model name cannot be empty")
        return model.strip()

    # ... [Keep all your CRUD methods but add proper error handling] ...

    def to_dict(self):
        return {
            'id': self.id,
            'model': self.model,
            'price': self.price,
            'battery_range': self.battery_range,
            'stock_quantity': self.stock_quantity
        }
from sqlalchemy import Column, Integer, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from . import Base, Session
from datetime import datetime

class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = (
        CheckConstraint('quantity > 0', name='check_quantity_positive'),
    )

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id', ondelete="CASCADE"))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id', ondelete="RESTRICT"))
    quantity = Column(Integer, nullable=False)
    order_date = Column(DateTime, default=func.now())
    
    customer = relationship("Customer", back_populates="orders")
    vehicle = relationship("Vehicle")

    @validates('quantity')
    def validate_quantity(self, key, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.vehicle and quantity > self.vehicle.stock_quantity:
            raise ValueError("Insufficient stock")
        return quantity

    # ... [Add transaction-safe methods] ...

    def calculate_total(self):
        return self.vehicle.price * self.quantity
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates, relationship
from sqlalchemy.sql import func
from . import Base, Session
import re

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(String, default=func.now())
    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")

    @validates('email')
    def validate_email(self, key, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")
        return email.lower()

    # ... [Add comprehensive CRUD methods] ...

    def get_order_history(self):
        return {
            'customer': self.name,
            'total_orders': len(self.orders),
            'total_spent': sum(order.vehicle.price * order.quantity for order in self.orders)
        }
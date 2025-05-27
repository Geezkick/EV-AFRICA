cat << EOF > lib/models/order.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from . import Base, Session
from datetime import datetime

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    order_date = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    customer = relationship("Customer", back_populates="orders")
    vehicle = relationship("Vehicle")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Quantity must be a positive integer")
        self._quantity = value

    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    def order_date(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Order date must be a non-empty string")
        self._order_date = value

    @classmethod
    def create(cls, customer_id, vehicle_id, quantity):
        session = Session()
        try:
            customer = session.query(Customer).get(customer_id)
            vehicle = session.query(Vehicle).get(vehicle_id)
            if not customer or not vehicle:
                raise ValueError("Invalid customer or vehicle ID")
            if vehicle.stock_quantity < quantity:
                raise ValueError(f"Insufficient stock: only {vehicle.stock_quantity} available")
            order = cls(customer_id=customer_id, vehicle_id=vehicle_id, order_date=datetime.now().strftime("%Y-%m-%d"), quantity=quantity)
            vehicle.stock_quantity -= quantity  # Update stock
            session.add(order)
            session.commit()
            return order
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete(cls, id):
        session = Session()
        try:
            order = session.query(cls).get(id)
            if order:
                vehicle = session.query(Vehicle).get(order.vehicle_id)
                vehicle.stock_quantity += order.quantity  # Restore stock
                session.delete(order)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def get_all(cls):
        session = Session()
        try:
            return session.query(cls).all()  # Returns a list of orders
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, id):
        session = Session()
        try:
            return session.query(cls).get(id)
        finally:
            session.close()

    @classmethod
    def get_by_customer(cls, customer_id):
        session = Session()
        try:
            return session.query(cls).filter_by(customer_id=customer_id).all()  # Returns a list
        finally:
            session.close()

    def __repr__(self):
        return f"<Order(id={self.id}, customer_id={self.customer_id}, vehicle_id={self.vehicle_id}, order_date={self.order_date}, quantity={self.quantity})>"

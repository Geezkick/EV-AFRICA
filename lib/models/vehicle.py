cat << EOF > lib/models/vehicle.py
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

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Model must be a non-empty string")
        self._model = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be a positive number")
        self._price = float(value)

    @property
    def battery_range(self):
        return self._battery_range

    @battery_range.setter
    def battery_range(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Battery range must be a positive integer")
        self._battery_range = value

    @property
    def stock_quantity(self):
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Stock quantity must be a non-negative integer")
        self._stock_quantity = value

    @classmethod
    def create(cls, model, price, battery_range, stock_quantity):
        session = Session()
        try:
            vehicle = cls(model=model, price=price, battery_range=battery_range, stock_quantity=stock_quantity)
            session.add(vehicle)
            session.commit()
            return vehicle
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete(cls, id):
        session = Session()
        try:
            vehicle = session.query(cls).get(id)
            if vehicle:
                session.delete(vehicle)
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
            return session.query(cls).all()  # Returns a list of vehicles
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
    def find_by_model(cls, model):
        session = Session()
        try:
            return session.query(cls).filter_by(model=model).first()
        finally:
            session.close()

    @classmethod
    def filter_by_price(cls, min_price, max_price):
        session = Session()
        try:
            return session.query(cls).filter(cls.price.between(min_price, max_price)).all()  # Returns a list
        finally:
            session.close()

    def __repr__(self):
        return f"<Vehicle(id={self.id}, model={self.model}, price={self.price}, battery_range={self.battery_range}, stock_quantity={self.stock_quantity})>"

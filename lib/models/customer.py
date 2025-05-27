from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates, relationship
from . import Base, Session

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or '@' not in value or not value.strip():
            raise ValueError("Email must be a valid non-empty string containing '@'")
        self._email = value

    @classmethod
    def create(cls, name, email):
        session = Session()
        try:
            customer = cls(name=name, email=email)
            session.add(customer)
            session.commit()
            return customer
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete(cls, id):
        session = Session()
        try:
            customer = session.query(cls).get(id)
            if customer:
                session.delete(customer)  # Cascade deletes related orders
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
            return session.query(cls).all()  # Returns a list of customers
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
    def find_by_email(cls, email):
        session = Session()
        try:
            return session.query(cls).filter_by(email=email).first()
        finally:
            session.close()

    def __repr__(self):
        return f"<Customer(id={self.id}, name={self.name}, email={self.email})>"
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Database configuration
engine = create_engine('sqlite:///ev_market.db', echo=True)
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))

# Import models after Base is created
from .vehicle import Vehicle
from .customer import Customer
from .order import Order

def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)
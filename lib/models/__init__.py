cat << EOF > lib/models/__init__.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///ev_market.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

from .vehicle import Vehicle
from .customer import Customer
from .order import Order


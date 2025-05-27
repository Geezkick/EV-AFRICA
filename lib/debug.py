cat << EOF > lib/debug.py
from models import Base, engine

Base.metadata.create_all(engine)

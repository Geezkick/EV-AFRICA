cat > lib/debug.py << 'PYTHON_EOF'
from models import Base, engine

def initialize_database():
    Base.metadata.create_all(engine)
    print("Database tables created successfully!")

if __name__ == '__main__':
    initialize_database()
PYTHON_EOF
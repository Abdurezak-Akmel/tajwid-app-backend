from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings  # Import the settings class we created earlier

# 1. Create the Database Engine
# The engine manages the network connections (connection pool) to MySQL.
# 'pool_pre_ping=True' checks if the connection is alive before using it, preventing "MySQL server has gone away" errors.
engine = create_engine(
    settings.database_url, 
    pool_pre_ping=True,
    echo=False  # Set to True if you want to see the raw SQL queries printed in your terminal
)

# 2. Create the Session Factory
# This is a factory that generates new Session objects for interacting with the database.
# 'autocommit=False' and 'autoflush=False' ensure transactions are explicitly committed.
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# 3. Create a Dependency/Helper for Database Sessions
# This ensures that database connections are properly opened when a request starts and closed when it finishes.
def get_db():
    """
    Context manager / dependency provider for database sessions.
    Yields a session instance and guarantees it closes after use.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
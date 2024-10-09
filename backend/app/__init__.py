# backend/app/__init__.py

# Import Base and DATABASE_URL for easy access
from .database import Base, DATABASE_URL

# Import models to ensure they are registered with SQLAlchemy
from . import models
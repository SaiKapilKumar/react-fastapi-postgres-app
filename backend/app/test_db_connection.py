# backend/app/test_db_connection.py

import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# For debugging: Print the path to the .env file
print(f"Loading .env file from: {os.path.join(os.path.dirname(__file__), '..', '.env')}")

# For debugging: Print all environment variables
#print(os.environ)

# Fetch the DATABASE_URL environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# For debugging: Print the value of DATABASE_URL
print(f"DATABASE_URL: {DATABASE_URL}")

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Database connection successful!")
    connection.close()
except OperationalError as e:
    print(f"Database connection failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
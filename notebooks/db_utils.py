#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# --- CONFIGURATION ---
# In a real production environment, use environment variables (os.environ)
# for sensitive data like passwords. For this local portfolio, we keep it simple.
DB_CONFIG = {
    'dbname': 'olist',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def get_engine():
    """
    Creates and returns a SQLAlchemy engine connection.
    Constructs the connection string safely using the URL helper.
    """
    connection_url = URL.create(
        drivername="postgresql+psycopg2",
        username=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        database=DB_CONFIG['dbname']
    )
    return create_engine(connection_url)

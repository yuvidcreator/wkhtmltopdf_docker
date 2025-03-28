import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv(f".env.{os.getenv('ENVIRONMENT', 'development')}")

dev_mode = os.getenv("DEV_MODE")

# Desired maximum connections
max_connections = 10000

# Compute pool_size and max_overflow based on max_connections
pool_size = 10  # You can adjust this as needed
max_overflow = max_connections - pool_size

# Database Setup
if dev_mode == "docker":
    MYSQL_DATABASE=os.getenv("MYSQL_DATABASE")
    MYSQL_USER=os.getenv("MYSQL_USER")
    MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD")
    DATABASE_URL = f"mysql+mysqlconnector://${MYSQL_USER}:${MYSQL_PASSWORD}@mysql-db:3306/${MYSQL_DATABASE}"
else:
    DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_size=pool_size, 
    max_overflow=max_overflow,
    pool_timeout=30,
    pool_recycle=3600,
    pool_pre_ping=True,
    connect_args={
        "init_command": "SET SESSION wait_timeout=2592000"
    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


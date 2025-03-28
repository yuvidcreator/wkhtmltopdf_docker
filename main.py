import os
from app.db import Base, SessionLocal, engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
# import logging
# import logging.config

# Load environment variables
from dotenv import load_dotenv

from app.routes.pdf import route as pdf_router


# load_dotenv(f".env.{os.getenv('ENV', 'development')}")
load_dotenv(f".env.{os.getenv('ENVIRONMENT', 'development')}")
# print("Printing env file ---- ",load_dotenv(f".env.{os.getenv('ENVIRONMENT', 'development')}"))


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

Base.metadata.create_all(bind=engine)

# FastAPI Initialization
# app = FastAPI(lifespan=lifespan)
app = FastAPI()

# Configuration
TEMPLATE_DIR = "templates"
STATIC_DIR = "static"
CHARTS_DIR = "charts"
OUTPUT_DIR = "output"

os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(TEMPLATE_DIR, exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(pdf_router)

# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger(__name__)

# logger.info("Application started.")

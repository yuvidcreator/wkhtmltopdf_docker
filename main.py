import os
from fastapi import FastAPI, Depends
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
# from contextlib import asynccontextmanager
# import logging
# import logging.config

# from __future__ import annotations
# from typing import TYPE_CHECKING

# import celery.states
# from celery.result import AsyncResult

# Load environment variables
from dotenv import load_dotenv
from app import models
from app.db import Base, SessionLocal, engine
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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# models.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]


# if TYPE_CHECKING:
#     from celery import Task
#     long_task: Task


# FastAPI Initialization
# app = FastAPI(lifespan=lifespan)
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

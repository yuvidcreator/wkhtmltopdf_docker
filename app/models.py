from sqlalchemy import Column, String, Integer, Enum

from app.db import Base, metadata



class ProcessTable(Base):
    __tablename__ = "process_table"
    metadata
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String(50), unique=True, index=True)
    status = Column(Enum("pending", "processing", "completed", "failed", name="status"), default="pending")
    file_path = Column(String(255), nullable=True)


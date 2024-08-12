from sqlalchemy import Column, Integer, String, DateTime, JSON
from db import Base

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    job_name = Column(String, index=True)
    last_run_timestamp = Column(DateTime)
    next_run_timestamp = Column(DateTime)
    interval = Column(String)
    details = Column(JSON)

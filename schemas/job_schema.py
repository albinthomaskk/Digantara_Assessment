from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class JobCreate(BaseModel):
    job_name: str
    interval: str
    details: Optional[Dict] = None

class JobResponse(BaseModel):
    id: int
    job_name: str
    last_run_timestamp: datetime
    next_run_timestamp: datetime
    interval: str
    details: Optional[Dict] = None

    class Config:
        orm_mode = True

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Job
from schemas.job_schema import JobCreate, JobResponse
from db import get_db
from services.job_scheduler import schedule_job
from utils import calculate_next_run
from datetime import datetime

job_router = APIRouter(prefix="/jobs", tags=["Jobs"])

@job_router.get("/", response_model=list[JobResponse])
def list_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()

@job_router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@job_router.post("/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    last_run = datetime.now()
    next_run = calculate_next_run(last_run, job.interval)
    new_job = Job(
        job_name=job.job_name,
        last_run_timestamp=last_run,
        next_run_timestamp=next_run,
        interval=job.interval,
        details=job.details
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    # Schedule the job
    schedule_job(new_job.id, job.interval, new_job.details)

    return new_job

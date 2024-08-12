from fastapi import FastAPI
from routes.jobs import job_router
from db import Base, engine

# Initialize the database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scheduler Microservice")

# Include the job management routes
app.include_router(job_router)

@app.get("/")
def read_root():
    return {"message": "Scheduler Microservice is running"}

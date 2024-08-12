from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
from typing import Dict

scheduler = BackgroundScheduler()
scheduler.start()

def dummy_job(job_id: int, details: Dict):
    print(f"Executing job {job_id} at {datetime.now()} with details: {details}")

def schedule_job(job_id: int, interval: str, details: Dict):
    if interval == "daily":
        trigger = IntervalTrigger(days=1)
    elif interval == "weekly":
        trigger = IntervalTrigger(weeks=1)
    else:
        return

    scheduler.add_job(dummy_job, trigger, args=[job_id, details])

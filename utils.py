from datetime import datetime, timedelta

def calculate_next_run(last_run: datetime, interval: str) -> datetime:
    if interval == "daily":
        return last_run + timedelta(days=1)
    elif interval == "weekly":
        return last_run + timedelta(weeks=1)
    # Add more interval cases as needed
    return last_run

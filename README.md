# Scheduler Microservice

## Overview
This is a microservice for scheduling jobs. It allows the creation, listing, and retrieval of job details with scheduling intervals like daily or weekly.

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/albinthomaskk/Digantara_Assessment
    cd scheduler_service
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    uvicorn app:app --reload
    ```

4. **Access API Documentation**:
   Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser to view the automatically generated API documentation.

## API Endpoints

- **GET /jobs**: List all jobs.
- **GET /jobs/{id}**: Retrieve job details by ID.
- **POST /jobs**: Create a new job with scheduling.

## Scaling Strategy
To scale this application:
1. **Horizontal Scaling**: Use containerization (e.g., Docker) and orchestration (e.g., Kubernetes) to deploy multiple instances of the service.
2. **Load Balancing**: Implement load balancers to distribute incoming traffic across instances.
3. **Database Scaling**: Use techniques like database sharding, replication, and partitioning to handle larger datasets.
4. **Caching**: Implement caching for frequently accessed data to reduce load on the database.
5. **Rate Limiting**: Protect the service from abuse by implementing rate limiting for API requests.

## Notes
- This project is set up for local development with SQLite. For production, replace SQLite with a more robust database like PostgreSQL or MySQL.

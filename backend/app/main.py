from fastapi import FastAPI
from app.api import health
from app.api import projects

app = FastAPI(
    title="DevPilot API",
    description="Self Service Deployment Platform",
    version="1.0.0"
)


app.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)

app.include_router(
    projects.router,
    prefix="/projects",
    tags=["Projects"]
)
from typing import Optional
from pydantic import BaseModel


class ProjectCreate(BaseModel):

    name: str
    github_url: str
    branch: str
    jenkins_url: str
    deployment_server: str


class ProjectUpdate(BaseModel):

    name: Optional[str] = None
    github_url: Optional[str] = None
    branch: Optional[str] = None
    jenkins_url: Optional[str] = None
    deployment_server: Optional[str] = None


class ProjectResponse(ProjectCreate):

    id: int

    class Config:
        from_attributes = True
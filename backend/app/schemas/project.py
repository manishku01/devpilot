from pydantic import BaseModel


class ProjectCreate(BaseModel):

    name: str
    github_url: str
    branch: str
    jenkins_url: str
    deployment_server: str


class ProjectUpdate(BaseModel):

    name: str
    github_url: str
    branch: str
    jenkins_url: str
    deployment_server: str


class ProjectResponse(ProjectCreate):

    id: int

    class Config:
        from_attributes = True
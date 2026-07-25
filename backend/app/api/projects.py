from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.project import Project
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate
)


router = APIRouter()


@router.post(
    "/",
    response_model=ProjectResponse
)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):

    new_project = Project(
        name=project.name,
        github_url=project.github_url,
        branch=project.branch,
        jenkins_url=project.jenkins_url,
        deployment_server=project.deployment_server
    )

    db.add(new_project)

    db.commit()

    db.refresh(new_project)

    return new_project

@router.get(
    "/",
    response_model=list[ProjectResponse]
)
def get_projects(
    db: Session = Depends(get_db)
):

    projects = db.query(Project).all()

    return projects

@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    return project

@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        return {
            "message": "Project not found"
        }

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }

@router.put(
    "/{project_id}",
    response_model=ProjectResponse
)
def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    db: Session = Depends(get_db)
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    project.name = project_data.name
    project.github_url = project_data.github_url
    project.branch = project_data.branch
    project.jenkins_url = project_data.jenkins_url
    project.deployment_server = project_data.deployment_server

    db.commit()
    db.refresh(project)

    return project

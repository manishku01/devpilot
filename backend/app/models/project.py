from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.database import Base


class Project(Base):

    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    github_url = Column(
        String,
        nullable=False
    )

    branch = Column(
        String,
        default="main"
    )

    jenkins_url = Column(
        String,
        nullable=False
    )

    deployment_server = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
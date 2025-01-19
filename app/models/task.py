from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="tasks")


if __name__ == "__main__":
    from sqlalchemy.schema import CreateTable

    print(CreateTable(Task.__table__))
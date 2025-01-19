from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.backend.db import Base


class User(Base):
    __tablename__ = "users"
    __table_args_ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")


if __name__ == "__main__":
    from sqlalchemy.schema import CreateTable

    print(CreateTable(User.__table__))
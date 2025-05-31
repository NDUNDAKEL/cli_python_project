from sqlalchemy import Column, Integer, String
from lib.models import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # One-to-Many: One user can write many reviews
    reviews = relationship("Review", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"

from sqlalchemy import Column, Integer, String
from lib.models import Base
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

    # One-to-Many: One book can have many reviews
    reviews = relationship("Review", back_populates="book")

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title})>"

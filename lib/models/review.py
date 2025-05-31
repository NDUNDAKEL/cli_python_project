from sqlalchemy import Column, Integer, String, ForeignKey
from lib.models import Base
from sqlalchemy.orm import relationship

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    # Many-to-One: Each review belongs to one user and one book
    user = relationship("User", back_populates="reviews")
    book = relationship("Book", back_populates="reviews")

    def __repr__(self):
        return f"<Review(id={self.id}, rating={self.rating}, user_id={self.user_id}, book_id={self.book_id})>"

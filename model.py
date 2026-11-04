from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped ,  mapped_column, relationship
from database import Base

class User(Base):
    __tablename__ = "user"
    id: Mapped[int]= mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    posts:Mapped[list["Post"]]=relationship(back_populates="owner") # Lets you write user.posts and post.owner

class Post(Base):
    __tablename__="posts"
    id: Mapped[int]= mapped_column(primary_key=True)
    post:Mapped[str]=mapped_column(String(100))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"] = relationship(back_populates="posts") # Lets you write user.posts and post.owner
    

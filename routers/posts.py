from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from model import User, Post
from schema import   PostRead, PostCreate
from sqlalchemy.orm import Session

router= APIRouter(tags=["Posts"])
@router.get("/posts", response_model= list[PostRead])
def get_all_posts(db: Session= Depends(get_db)):
    return db.query(Post).all()

@router.get("/users/{id}/posts", response_model=list[PostRead])
def get_all_posts_ofUser(id:int, db:Session=Depends(get_db)):
    user= db.query(User).filter(User.id==id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.posts

@router.post("/users/{id}/posts", response_model=PostRead)
def create_post_for_user(id:int, name:PostCreate, db: Session=Depends(get_db)):
    user= db.query(User).filter(User.id==id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    post= Post(title=name.title, user_id=id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

    
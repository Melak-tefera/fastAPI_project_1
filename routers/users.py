from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from model import User
from schema import  UserRead
from sqlalchemy.orm import Session

router= APIRouter(prefix="/users", tags=["Users"])
@router.get("", response_model= list[UserRead])
def get_all_users(db:Session=Depends(get_db)):
    return db.query(User).all()
@router.get("/{id}", response_model=UserRead)
def get_user_by_id(id:int, db: Session=Depends(get_db)):
    user= db.query(User).filter(User.id==id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user
@router.post("",response_model=UserRead)
def create_user(name: UserRead, db: Session=Depends(get_db)):
    user=User(name=name.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
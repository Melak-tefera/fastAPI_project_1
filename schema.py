from pydantic import BaseModel, ConfigDict

class UserRead(BaseModel):
    id:int
    name:str
    model_config= ConfigDict(from_attributes=True)

class PostCreate(BaseModel):
    title: str

class PostRead(BaseModel):
    id: int
    title: str
    user_id: int
    model_config = ConfigDict(from_attributes=True)
    
class UserWithPosts(UserRead):
    posts: list[PostRead] = []
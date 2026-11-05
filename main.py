from fastapi import FastAPI # importing fastAPI
import model # importing model.py a model for the database
from routers import users, posts # importing  the endpints that are  at router/user.py


app= FastAPI() # creating the backend app
app.include_router(users.router) # the routers importing 
app.include_router(posts.router)


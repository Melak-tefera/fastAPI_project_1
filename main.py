from fastapi import FastAPI # importing fastAPI
from database import engine, Base # importing engine and Base class from database.py
import model # importing model.py a model for the database
from routers import users # importing  the endpints that are  at router/user.py

Base.metadata.create_all(bind=engine) # creating the tables for the first time
app= FastAPI() # creating the backend app
app.include_router(users.router) # the routers importing 


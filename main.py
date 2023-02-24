# main.py
#import FastAPI
from fastapi import FastAPI
import api
from pydantic import BaseModel
import uvicorn


# Initialize the app
app = FastAPI()

app.include_router(api.router)


# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to my Todo list App."}

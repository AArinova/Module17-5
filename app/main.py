from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message': 'Welcome to TaskManager'}

app.include_router(task.router)
app.include_router(user.router)
from fastapi import FastAPI
from app.api import api_router
from app.config.database import Connect

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    session = Connect()
    await session.start_connection()

@app.get("/")
async def index():
    return {"message":"Welcome To Pokedex"}

app.include_router(api_router, prefix="/api/v1")
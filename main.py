"""Pokedex Service Core"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api import api_router
from app.config.database import Connect
from app.utils.customException import PokeException
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """
    Trigger Any Tasks Before Starting The Backend Server
    """
    session = Connect()
    await session.start_connection()


@app.exception_handler(PokeException)
async def exception_handler(_: Request, exc: PokeException):
    """
    Exception Handler For Pokedex Service
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.message,
            "detail": None,
            "success": False
        }
    )


@app.get("/")
async def index():
    """Root Of All APIs"""
    return {"message": "Welcome To Pokedex"}

app.include_router(api_router, prefix="/api/v1")

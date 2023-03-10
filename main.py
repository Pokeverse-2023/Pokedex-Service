from fastapi import FastAPI, Request
from app.api import api_router
from app.config.database import Connect
from app.utils.CustomException import CustomException
from app.viewModels.responseModel import Response
from fastapi.responses import JSONResponse
app = FastAPI()


@app.on_event("startup")
async def startup_event():
    session = Connect()
    await session.start_connection()


@app.exception_handler(CustomException)
async def unicorn_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=418,
        content={
            "message": exc.message,
            "detail": None,
            "success": False
        }
    )


@app.get("/")
async def index():
    return {"message": "Welcome To Pokedex"}

app.include_router(api_router, prefix="/api/v1")

from fastapi import APIRouter

from app.api.pokemon import pokemon_router

api_router = APIRouter()

api_router.include_router(pokemon_router, prefix="/pokemon", tags=["Pokemon"])

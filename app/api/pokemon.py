from fastapi import APIRouter, Query
from app.core.pokemon import PokemonCore
from app.utils.CustomException import CustomException
from app.viewModels import CreatePokemonRequest, UpdatePokemonRequest, Response

pokemon_router = APIRouter()
core = PokemonCore()


@pokemon_router.get("/", response_model=Response)
async def get_pokemon(search: str = ""):
    res = await core.get_pokemon(search)
    return Response(detail=res, message="Pokemon Fetched Successfully", success=True)


@pokemon_router.post("/")
async def add_pokemon(data: CreatePokemonRequest):
    await core.create_pokemon(data)
    return Response(detail=None, message="Pokemon Added Successfully", success=True)


@pokemon_router.put("/{id}")
async def modify_pokemon(id: int, data: UpdatePokemonRequest):
    await core.update_pokemon(id, data)
    return Response(detail=None, message="Pokemon Updated Successfully", success=True)

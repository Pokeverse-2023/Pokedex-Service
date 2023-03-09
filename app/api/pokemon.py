from fastapi import APIRouter, Query
from app.core.pokemon import PokemonCore
from app.viewModels import CreatePokemonRequest, UpdatePokemonRequest, Response

pokemon_router = APIRouter()
core = PokemonCore()


@pokemon_router.get("/", response_model=Response)
async def get_pokemon(
        id: int = Query(..., gt=0),
        name: str = ""
):
    try:
        res = await core.get_pokemon(id, name)
        return Response(detail=res, message="Pokemon Fetched Successfully", success=True)
    except Exception as exc:
        return Response(detail=None, message=str(exc), success=False)


@pokemon_router.post("/")
async def add_pokemon(data: CreatePokemonRequest):
    await core.create_pokemon(data)


@pokemon_router.put("/{id}")
async def modify_pokemon(id: int, data: UpdatePokemonRequest):
    await core.update_pokemon(id, data)

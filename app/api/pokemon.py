"""Pokemon Core API"""
from typing import Optional
from fastapi import APIRouter
from app.core.pokemon import PokemonCore
from app.utils.common import OrderBy
from app.utils.constants import PokemonSortField
from app.viewModels import CreatePokemonRequest, UpdatePokemonRequest, Response

pokemon_router = APIRouter()
core = PokemonCore()


@pokemon_router.get("/", response_model=Response)
async def get_pokemon(
        search: Optional[str],
        sort_by: PokemonSortField = PokemonSortField.NAME,
        order_by: OrderBy = OrderBy.ASC):
    """
    Get Pokemon API
    """
    if search == "" or search is None:
        res = await core.get_pokemon(sort_by, order_by)
    else:
        res = await core.get_pokemon_by_search(search, sort_by, order_by)
    return Response(detail=res, message="Pokemon Fetched Successfully", success=True)


@pokemon_router.post("/")
async def add_pokemon(data: CreatePokemonRequest):
    """
    Add Pokemon API
    """
    await core.create_pokemon(data)
    return Response(detail=None, message="Pokemon Added Successfully", success=True)


@pokemon_router.put("/{id}")
async def modify_pokemon(pid: int, data: UpdatePokemonRequest):
    """
    Update Pokemon API
    """
    await core.update_pokemon(pid, data)
    return Response(detail=None, message="Pokemon Updated Successfully", success=True)

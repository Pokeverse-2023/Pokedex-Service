"""Core Pokemon Services"""
from pydantic import BaseModel
from app.models import Pokemon
from app.utils.customException import PokeException
from app.utils.constants import PokemonType
from app.viewModels.pokemon import CreatePokemonRequest, UpdatePokemonRequest


class ProjectionModel(BaseModel):
    """Projection Model For Pokemon Layer"""
    pokemon_id: int
    name: str
    base_experience: int
    weight: int
    height: int
    type: PokemonType


class PokemonCore:
    """Core Pokemon Layer"""
    async def create_pokemon(self, request: CreatePokemonRequest):
        """
        Create A New Pokemon
        """
        exists = await Pokemon.find_one({"$or": [{"name": request.id}, {"name": request.name}]})
        if exists:
            raise PokeException(
                message="Pokemon already exists", status_code=409)
        new_model = Pokemon.from_pydantic(request)
        await new_model.create()

    async def get_pokemon(self, sort_field, order_by):
        """
        Fetch All Pokemons With Field Sorting And Order By Filters
        """
        return await Pokemon.find()\
            .sort(f"{order_by}{sort_field}")\
            .limit(20)\
            .to_list()

    async def get_pokemon_by_search(self, search, sort_field, order_by):
        """
        Fetch All Pokemons With Search, Field Sorting And Order By Filters
        """
        pokemon = []
        if search != "" and search is not None:
            regex_filter = {"$regex": f".*{search}*.", "$options": "i"}
            pokemon = await Pokemon\
                .find({"$or": [
                    {"name": regex_filter}, {"pokemon_id": search}
                ]})\
                .project(ProjectionModel)\
                .sort(f"{order_by}{sort_field}")\
                .limit(20)\
                .to_list()\

        if not pokemon:
            raise PokeException(message="Pokemon not found", status_code=404)
        return pokemon

    async def get_pokemon_by_id(self, pid: int):
        """
        Fetch A Pokemon By ID
        """
        pokemon = await Pokemon.find_one({"pokemon_id": pid})
        return pokemon

    async def update_pokemon(self, pid: int, request: UpdatePokemonRequest):
        """
        Update An Existing Pokemon
        """
        existing_pokemon = await self.get_pokemon_by_id(pid)
        if not existing_pokemon:
            raise PokeException(
                message="Pokemon does not exist",
                status_code=404)
        req = {k: v for k, v in request.dict().items() if v is not None}
        update_query = {field: value for field, value in req.items()}
        await existing_pokemon.update({"$set": (update_query)})
        return existing_pokemon

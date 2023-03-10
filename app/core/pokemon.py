from fastapi import HTTPException
from app.models import Pokemon
from app.utils.CustomException import CustomException
from app.viewModels.pokemon import CreatePokemonRequest, UpdatePokemonRequest


class PokemonCore:
    async def create_pokemon(self, request: CreatePokemonRequest):
        new_model = Pokemon.from_pydantic(request)
        await new_model.create()

    async def get_pokemon(self, search: str = ""):
        response = []
        if search != "" and search is not None:
            pokemon = await Pokemon.find_one(Pokemon.name == search)
            response += pokemon if pokemon is not None else []
        else:
            response = await Pokemon.find().to_list()
        if not response:
            raise CustomException(
                name="Not Found", message="Pokemon not found")
        return response

    async def get_pokemon_by_id(self, pid: int):
        pokemon = await Pokemon.find_one({"pokemon_id": pid})
        return pokemon

    async def update_pokemon(self, pid: int, request: UpdatePokemonRequest):
        existing_pokemon = await self.get_pokemon_by_id(pid=pid)
        if not existing_pokemon:
            raise CustomException(message="Pokemon does not exist", name="Not found"
                                  )
        req = {k: v for k, v in request.dict().items() if v is not None}
        update_query = {"$set": {field: value for field, value in req.items()}}
        await existing_pokemon.update(update_query)
        return existing_pokemon

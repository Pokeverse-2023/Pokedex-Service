from fastapi import HTTPException
from app.models import Pokemon
from app.viewModels.pokemon import CreatePokemonRequest, UpdatePokemonRequest


class PokemonCore:
    async def create_pokemon(self, request: CreatePokemonRequest):
        new_model = Pokemon.from_pydantic(request)
        await new_model.create()

    async def get_pokemon(self, pid: int = 0, name: str = ""):
        pokemon = await Pokemon.find_one(Pokemon.pokemon_id == pid or Pokemon.name == name)
        if not pokemon:
            raise Exception("Pokemon not found")
        return pokemon

    async def update_pokemon(self, pid: int, request: UpdatePokemonRequest):
        existing_pokemon = await self.get_pokemon(id=pid)
        if not existing_pokemon:
            raise HTTPException(
                detail="Review record not found"
            )
        req = {k: v for k, v in request.dict().items() if v is not None}
        update_query = {"$set": {field: value for field, value in req.items()}}
        await existing_pokemon.update(update_query)
        return existing_pokemon

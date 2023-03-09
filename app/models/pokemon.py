from datetime import datetime, date
from beanie import Document
from pydantic import Field

from app.viewModels.pokemon import CreatePokemonRequest


class Pokemon(Document):
    pokemon_id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    last_updated: datetime = datetime.now()

    def from_pydantic(request: CreatePokemonRequest) -> "Pokemon":
        return Pokemon(
            pokemon_id=request.id,
            name=request.name,
            base_experience=request.base_experience,
            height=request.height,
            is_default=request.is_default,
            order=request.order,
            weight=request.weight
        )

    class Settings:
        name = "Pokemon"

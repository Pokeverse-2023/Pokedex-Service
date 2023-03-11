"""Pokemon Core Model"""
from datetime import datetime
from beanie import Document
from app.utils.constants import PokemonType

from app.viewModels.pokemon import CreatePokemonRequest


class Pokemon(Document):
    """
    Schema Document For Pokemon
    """
    pokemon_id: int
    name: str
    base_experience: int
    height: int
    is_default: bool = True
    order: int
    weight: int
    type: PokemonType
    last_updated: datetime = datetime.now()

    @staticmethod
    def from_pydantic(request: CreatePokemonRequest) -> "Pokemon":
        """
        Map Request Model From Request
        """
        return Pokemon(
            pokemon_id=request.id,
            name=request.name,
            base_experience=request.base_experience,
            height=request.height,
            is_default=request.is_default,
            order=request.order,
            weight=request.weight,
            type=request.type
        )

    class Settings:
        """
        Configuration Settings For Core Pokemon Schema
        """
        name = "Pokemon"

from datetime import datetime
from enum import Enum
from uuid import UUID
from beanie import Document

from app.viewModels.pokemon import CreatePokemonRequest


class PokemonType(Enum):
    DARK = "Dark"
    PSYCHIC = "Psychic"
    FIGHTING = "Fighting"
    STEEL = "Steel"
    ICE = "Ice"
    POISON = "Poison"
    FIRE = "Fire"
    GROUND = "Ground"
    FLYING = "Flying"
    ELECTRIC = "Electric"
    FAIRY = "Fairy"
    NORMAL = "Normal"
    BUG = "Bug"
    WATER = "Water"
    ROCK = "Rock"
    GHOST = "Ghost"
    DRAGON = "Dragon"
    GRASS = "Grass"


class Pokemon(Document):
    pokemon_id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    type: PokemonType
    last_updated: datetime = datetime.now()

    @staticmethod
    def from_pydantic(request: CreatePokemonRequest) -> "Pokemon":
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
        name = "Pokemon"

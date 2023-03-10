from pydantic import BaseModel

from app.models import PokemonType as Type


class PokemonRequest(BaseModel):
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int
    type: Type


class CreatePokemonRequest(PokemonRequest):
    id: int


class UpdatePokemonRequest(PokemonRequest):
    pass

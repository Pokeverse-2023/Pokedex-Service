"""Pokemon View Models"""
from typing import Optional
from pydantic import BaseModel

from app.utils.constants import PokemonType


class PokemonRequest(BaseModel):
    """
    Request Model For Pokemon Core Layer
    """
    base_experience: int
    height: int
    is_default: Optional[bool] = True
    order: int
    weight: int
    type: PokemonType


class CreatePokemonRequest(PokemonRequest):
    """
    Request Model For Creating A New Pokemon
    """
    id: int
    name: str


class UpdatePokemonRequest(PokemonRequest):
    """
    Request Model For Updating Existing Pokemon
    """

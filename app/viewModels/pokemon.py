from pydantic import BaseModel


class PokemonRequest(BaseModel):
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int


class CreatePokemonRequest(PokemonRequest):
    id: int


class UpdatePokemonRequest(PokemonRequest):
    pass

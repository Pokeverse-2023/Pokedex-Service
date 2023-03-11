"""Constants For Core Pokemon Module"""
from enum import Enum


class PokemonType(Enum):
    """
    Types Of Pokemon
    """
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


class PokemonSortField(Enum):
    """
    Sort Field Filter For Core Pokemon Model
    """
    NAME = "name"
    ORDER = "order"
    BASE_EXPERIENCE = "base_experience"

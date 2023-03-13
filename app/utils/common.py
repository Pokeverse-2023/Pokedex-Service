"""Common Utils For Pokedex Service"""
from enum import Enum


class OrderBy(Enum):
    """
    General Order By Filter Model
    """

    ASC = "1"
    DESC = "-1"

from enum import Enum
from typing import List, Optional

from ninja import Field, FilterSchema


class PokemoneFilterSchema(FilterSchema):
    name: Optional[str] = Field(q="name__icontains")
    type: Optional[List[str]] = Field(q="type__contains")


class SortDirection(Enum):
    ASC = "asc"
    DESC = "desc"


class SortField(Enum):
    POKEDEX_NUMBER = "pokedex_number"
    HEIGHT_M = "height_m"
    WEIGHT_KG = "weight_kg"

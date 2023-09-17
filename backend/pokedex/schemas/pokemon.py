from typing import List, Optional

from ninja import Schema


class PokemonListItem(Schema):
    id: int
    pokedex_number: int
    name: str
    type: List[str]


class ClassificationName(Schema):
    name: str


class PokemonDetails(PokemonListItem):
    japanese_name: str
    classification: ClassificationName
    attack: int
    defense: int
    height_m: Optional[float]
    weight_kg: Optional[float]
    hp: int
    sp_attack: int
    sp_defense: int
    speed: int
    generation: int
    is_legendary: bool

from ninja import Schema


class PokemonType(Schema):
    id: int
    name: str
    icon_url: str

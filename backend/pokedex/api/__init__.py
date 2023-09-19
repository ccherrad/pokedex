from ninja import NinjaAPI

from .v1.pokemon_api import router as pokemon_router
from .v1.pokemon_type_api import router as pokemon_type_router

api = NinjaAPI()
api.add_router("v1/pokemon/", pokemon_router)
api.add_router("v1/pokemon-type/", pokemon_type_router)

from typing import List

from ninja import Router
from pokedex.models import PokemonType
from pokedex.schemas import PokemonType as PokemonTypeOut

router = Router()


@router.get("/", response=List[PokemonTypeOut])
def get_all_types(request):
    qs = PokemonType.objects.all()
    return qs
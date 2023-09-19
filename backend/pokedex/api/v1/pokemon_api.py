from typing import List

from django.shortcuts import get_object_or_404
from ninja import Query, Router
from ninja.pagination import paginate

from pokedex.models import Pokemon
from pokedex.schemas import PokemonDetails, PokemonListItem

from .helpers import PokemoneFilterSchema, SortDirection, SortField

router = Router()


@router.get("/", response=List[PokemonListItem])
@paginate
def get_all_pokemones(
    request,
    filters: PokemoneFilterSchema = Query(...),
    sort_field: str = Query(SortField.POKEDEX_NUMBER.value),
    sort_direction: str = Query(SortDirection.ASC.value),
):
    """
    Get a list of Pokémon with optional filters and pagination.

    Args:
        request: The HTTP request.
        filters (PokemoneFilterSchema): Filters to apply to the Pokémon list.
        sort_field (str): The field to sort the Pokémon list by.
        sort_direction (str): The sorting direction, either "asc" or "desc".

    Returns:
        List[PokemonListItem]: A list of Pokémon matching the filters and
        sorted as specified.
    """

    qs = Pokemon.objects.all()
    poks = filters.filter(qs)
    if sort_direction == "desc":
        sort_field = "-" + sort_field
    sorted_poks = poks.order_by(sort_field)
    return sorted_poks


@router.get("/{pokemone_id}", response=PokemonDetails)
def get_pokemone(
    request,
    pokemone_id: int,
):
    """
    Get details of a specific Pokémon by its ID.

    Args:
        request: The HTTP request.
        pokemone_id (int): The ID of the Pokémon to retrieve.

    Returns:
        PokemonDetails: Details of the specified Pokémon.
    """

    pokemone = get_object_or_404(Pokemon, id=pokemone_id)
    return pokemone

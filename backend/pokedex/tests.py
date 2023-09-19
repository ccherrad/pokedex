from django.test import Client, TestCase

from .models import Pokemon


class PokemonApiTestCase(TestCase):
    def test_get_all_pokemones(self):
        client = Client()
        url = "/api/v1/pokemon/"
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 801)

    def test_get_all_pokemones_with_filters(self):
        client = Client()
        name_filter = "?name=p"
        type_filter = "&type=electric"
        sort_filters = "&sort_field=pokedex_number&sort_direction=asc"
        filters = name_filter + type_filter + sort_filters
        url = "/api/v1/pokemon/"
        response = client.get(url + filters)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 9)
        self.assertEqual(response.json()["items"][0]["name"], "Pikachu")

    def test_get_pokemone(self):
        client = Client()
        pokemon_id = Pokemon.objects.get(name="Pikachu").id
        url = f"/api/v1/pokemon/{pokemon_id}"
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

const getPokemones = async (
    name = "",
    types = [],
    sort_field = "pokedex_number",
    sort_direction = "asc",
    limit = 12,
    offset = 0,
) => {
    const url = new URL("http://0.0.0.0:8000/api/v1/pokemon/");
    if (name) {
      url.searchParams.set("name", name);
    }
    types.forEach((type) => url.searchParams.append("type", type));
    url.searchParams.set("sort_field", sort_field);
    url.searchParams.set("sort_direction", sort_direction);
    url.searchParams.set("limit", limit);
    url.searchParams.set("offset", offset);
  
    const response = await fetch(url);
    const data = await response.json();
    return data;
};

const getPokemonDetails = async (id) => {
  const response = await fetch(`http://0.0.0.0:8000/api/v1/pokemon/${id}`);
  const data = await response.json();
  return data;
};

const getPokemonImageUrl = (number) => {
  const paddedNumber = String(number).padStart(3, '0');
  return `https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/${paddedNumber}.png`;
};

module.exports = {
  getPokemones,
  getPokemonDetails,
  getPokemonImageUrl,
};

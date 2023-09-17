<template>
  <div>
    <div class="max-w-md mx-auto bg-white rounded-lg shadow-lg p-6">
      <div class="flex">
        <div>
          <h1 class="text-2xl font-semibold text-center mx-4">{{ pokemon.name }}</h1>
          <h3 class="mx-4 text-gray-600 font-semibold">#{{ String(pokemon.pokedex_number).padStart(3, '0')}}</h3>
        </div>
        <span class="w-8 h-8 bg-black rounded-full flex items-center justify-center">
              <p class="text-white text-lg">G{{ pokemon.generation }}</p>
        </span>
      </div>
        <div class="text-center mb-4 flex">
            <img 
              :src="getPokemonImageUrl(pokemon.pokedex_number)"
              :class="(pokemon.is_legendary === false) ? 'border-gree-400' : 'border-yellow-400'" 
              class="w-64 l-64 mx-auto border-l-8 pl-1 border-green-400">
            <div>
              <p class="text-gray-500">{{ pokemon.japanese_name }}</p>
            <div class="text-center">
                <p class="mt-2 text-gray-600">
                  {{ pokemon.classification.name }}
                </p>
            </div>
            <div class="flex justify-center space-x-2">
                <img v-for="type in types" :src="type" class="w-12 h-12">
            </div>
            <div class="text-center">
                <p class="mt-2 text-gray-600">
                  <i class="fa-solid fa-ruler-vertical"></i>
                  0.7 m
                </p>
            </div>
            <div class="text-center">
                <p class="mt-2 text-gray-600">
                  <i class="fa-solid fa-weight-hanging"></i>
                  6,9 kg
                </p>
            </div>
            </div>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <Scale name="HP" :value="pokemon.hp"/>
          <Scale name="Special Attack" :value="pokemon.sp_attack"/>
          <Scale name="Special Defense" :value="pokemon.sp_defense"/>
          <Scale name="Speed" :value="pokemon.speed"/>
          <Scale name="Attck" :value="pokemon.attack"/>  
          <Scale name="Defense" :value="pokemon.defense"/>
        </div>
    </div>
  </div>
</template>

<script>
import { getPokemonDetails, getPokemonImageUrl } from "~/services/pokedexService";

export default {

  data() {
    return {
      pokemon: {
        type: [],
        classification: {
          name: String,
        }
      },
    }
  },

  async mounted() {
    this.pokemon = await getPokemonDetails(this.$route.params.id);
  },

  computed: {
    types() {
      return this.pokemon.type.map((type) => {
        const matchingType = this.$store.state.pokemonTypes.types.find((data) => data.name === type);
        return matchingType ? matchingType.icon_url : null;
      });
    }    
  },

  methods: {
    getPokemonImageUrl(pokedex_number) {
      return getPokemonImageUrl(pokedex_number);
    },
  }

};
</script>
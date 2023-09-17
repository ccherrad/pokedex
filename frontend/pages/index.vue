<template>
    <div class="flex flex-col">
        <div class="filters flex gap-5">
            <div>
            <Search @search="handleSearch" />
        </div>
        <Select
            :options="pokemonTypesOptions"
            :maxSelect="2"
            placeholder="Select types..."
            @select="handleTypeSelect"
        ></Select>
        </div>
        <div class="pokemons mt-5 flex flex-col flex-grow">
            <div class="sorters flex self-end">
                <Select
                    :options="sortingDropdownOptions"
                    @select="handleSortingAttrSelect"
                ></Select>
                <Toggle 
                    class="ml-5"
                    @toggle="handleSortingDirection"
                />
            </div>
            <div class="grid mt-5 grid-cols-4 gap-4 px-16">
                <nuxt-link v-for="pokemon in pokemonList" :to="`/pokemon/${pokemon.id}`">
                    <Card
                        :id="pokemon.id"
                        :key="pokemon.id"
                        :name="pokemon.name"
                        :pokedexNumber="pokemon.pokedex_number" 
                        :imageUrl=getPokemonImageUrl(pokemon.pokedex_number)
                    />
                </nuxt-link>
            </div>
        </div>
        <footer class="p-4 mx-auto">
            <Paginator 
                v-if="pokemonList.length >= 12"
                :itemsPerPage="itemsPerPage" 
                :totalItems="totalItems" 
                :currentPage="currentPage"
                @page-change="handlePageChange" 
            />
        </footer>
    </div>

</template>

<script>
import { getPokemones, getPokemonImageUrl } from "~/services/pokedexService";

export default {
    name: 'IndexPage',
    async asyncData({ store }) {
        await store.dispatch('pokemonTypes/fetchTypes');
        await store.dispatch('pokemonsCount/fetchCount');
    },
    data() {
        return {
            searchQuery: "",
            types: [],
            sortingAttr: 'pokedex_number',
            sortingDirection: 'asc',
            itemsPerPage: 12,
            totalItems: 812,
            currentPage: 1,
            selectedItemCount: 1,
            pokemonList: [],
            sortingDropdownOptions: [
                {
                    text: 'National Pokedex Number',
                    value: "pokedex_number",
                    init_value: true
                },
                {
                    text: 'Weight(kg)',
                    value: "weight_kg"
                },
                {
                    text: 'Height(m)',
                    value: "height_m"
                }
            ],
        };
    },
    async mounted() {
        const pokemones = await getPokemones();
        this.pokemonList = pokemones.items;
        this.totalItems = pokemones.count;
    },
    computed: {
        pokemonTypesOptions() {
            return this.$store.state.pokemonTypes.types.map(item => ({
                text: item.name,
                value: item.name
            }));
        },
    },
    methods: {
        handlePageChange(page) {
            this.currentPage = page;
            this.fetchPokemons();
        },
        handleSearch(value) {
            this.currentPage = 1;
            this.searchQuery = value;
            this.fetchPokemons();
        },
        handleTypeSelect(types){
            this.currentPage = 1;
            this.types = types.map(obj => obj.value);
            this.fetchPokemons();
        },
        handleSortingAttrSelect(sortingAttr) {
            this.currentPage = 1;
            this.sortingAttr = sortingAttr.value;
            this.fetchPokemons();
        },
        handleSortingDirection(sortingDirection) {
            this.currentPage = 1;
            this.sortingDirection = sortingDirection ? 'asc' : 'desc';
            this.fetchPokemons();
        },
        getPokemonImageUrl(pokedex_number) {
            return getPokemonImageUrl(pokedex_number);
        },
        async fetchPokemons() {
            const pokemones = await getPokemones(
                                this.searchQuery,
                                this.types, 
                                this.sortingAttr,
                                this.sortingDirection,
                                this.itemsPerPage,
                                (this.currentPage - 1) * this.itemsPerPage
                              );
            this.pokemonList = pokemones.items;
            this.totalItems = pokemones.count;
        },
    },
}
</script>

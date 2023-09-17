import { getPokemones } from "~/services/pokedexService";

export const state = () => ({
    count: null,
})

export const mutations = {
    setCount(state, count) {
        state.count = count
    },
}

export const actions = {
    async fetchCount({ commit }) {
        try {
            const pokemons = await getPokemones();
            commit('setCount', pokemons.count)
        } catch (error) {
            console.error('Error fetching Pokemon count:', error)
        }
    },
}
export const state = () => ({
    types: [],
})

export const mutations = {
    setTypes(state, types) {
        state.types = types
    },
}

export const actions = {
    async fetchTypes({ commit }) {
        try {
            const response = await fetch('http://0.0.0.0:8000/api/v1/pokemon-type/')
            if (!response.ok) {
                throw new Error('Failed to fetch Pokemon types')
            }
            const types = await response.json()
            commit('setTypes', types)
        } catch (error) {
            console.error('Error fetching Pokemon types:', error)
        }
    },
}
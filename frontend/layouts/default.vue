<template>
    <div class="bg-white bg-light-pattern flex flex-col h-screen w-3/5">
        <nav class="p-4">
            <div class="container mx-auto">
                <div class="flex justify-between items-center">
                    <nuxt-link to="/">
                        <div class="text-black font-bold text-xl"><Logo/></div>
                    </nuxt-link>
                <div class="space-x-4">
                    <button @click="redirectToRandomPokemon" class="text-black rounded-full border-2 p-3">
                        <i class="fa-solid fa-shuffle"></i>
                        Surprise me
                    </button>
                </div>
                </div>
            </div>
        </nav>

        <div class="container mx-auto mt-8 p-4">
            <nuxt />
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        redirectToRandomPokemon() {
            console.log(this.$store.state.pokemonsCount.count);
            const randomId = Math.floor(Math.random() * this.$store.state.pokemonsCount.count) + 1;
            this.$router.push(`/pokemon/${randomId}`);
        },
    }
}
</script>
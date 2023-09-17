<template>
    <div class="bg-neutral-100 rounded-lg shadow-md p-4">
      <div class="text-center">
        <img :src="imageUrl" alt="Pokemon" class="w-24 h-24 mx-auto mb-2">
        <p class="text-gray-600">#{{ String(pokedexNumber).padStart(3, '0') }}</p>
        <p class="text-lg font-semibold">{{ name }}</p>
      </div>
    </div>
  </template>
  
<script>
  export default {
    props: {
      id: {
        type: Number,
        required: true
      },
      name: {
        type: String,
        required: true
      },
      pokedexNumber: {
        type: Number,
        required: true
      },
      imageUrl: {
        type: String,
        required: true
      }
    }
  };
</script>
  
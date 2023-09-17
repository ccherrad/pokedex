<template>
  <div class="flex">
    <div class="relative flex-grow">
      <input
        v-model="searchQuery"
        @input="onInputChange"
        class="w-full border rounded-full py-4 pl-4 pr-10 text-gray-700 placeholder-gray-400 focus:outline-none focus:ring focus:border-blue-300"
        type="text"
        placeholder="Search..."
      />
      <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
        <i class="fas fa-search"></i>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        searchQuery: ''
      };
    },

    methods: {
      onInputChange() {
        this.$emit('search', this.searchQuery);
      }
    }

  };
</script>
  
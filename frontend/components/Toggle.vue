<template>
    <div class="flex items-center space-x-2">
      <a
        @click="toggleSorting"
        class="text-lg cursor-pointer"
      >
      <i :class="isAscending ? 'fa-solid fa-arrow-up-wide-short' : 'fa-solid fa-arrow-down-wide-short'"></i>
    </a>
    </div>
</template>
  
<script>
  export default {
    data() {
      return {
        isAscending: true
      };
    },
    methods: {
      toggleSorting() {
        this.isAscending = !this.isAscending;
        this.$emit('toggle', this.isAscending);
      }
    }
  };
</script>

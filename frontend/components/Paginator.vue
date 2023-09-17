<template>
    <div class="flex items-center justify-between">
      <div class="flex space-x-5 text-xl">
        <a
          @click="goToPage(currentPage - 1)"
          :disabled="currentPage === 1"
          class="cursor-pointer"
        >
        <i class="fa-solid fa-angle-left"></i>
        </a>
        <p class="text-lg text-gray-600">
          {{ currentPage }}
        </p>
        <a
          @click="goToPage(currentPage + 1)"
          :disabled="currentPage === totalPages"
          class="cursor-pointer	"
        >
        <i class="fa-solid fa-angle-right"></i>
        </a>
      </div>
    </div>
</template>
  
<script>
  export default {
    props: {
      itemsPerPage: {
        type: Number,
        required: true
      },
      totalItems: {
        type: Number,
        required: true
      },
      currentPage: {
        type: Number,
        required: true
      }
    },
    computed: {
      startItem() {
        return (this.currentPage - 1) * this.itemsPerPage + 1;
      },
      endItem() {
        const end = this.currentPage * this.itemsPerPage;
        return end > this.totalItems ? this.totalItems : end;
      },
      totalPages() {
        return Math.ceil(this.totalItems / this.itemsPerPage);
      }
    },
    methods: {
      goToPage(page) {
        if (page >= 1 && page <= this.totalPages) {
          this.$emit('page-change', page);
        }
      }
    }
  };
</script>
  
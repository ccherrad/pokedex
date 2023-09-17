<template>
    <div class="relative">
      <div class="multiselect">
        <a
          @click="toggleDropDown"
          class="cursor-pointer"
        >
          <div class="bg-white flex items-center w-64 h-14 border rounded-full py-2 pl-4 pr-10 text-gray-700 placeholder-gray-400 focus:outline-none focus:ring focus:border-blue-300">
            <span v-if="selectedOptions.length === 0" class="select-none text-neutral-400">
              {{ placeholder }}
            </span>
            <div
              v-if="maxSelect > 1"
              v-for="option in selectedOptions"
              :key="option.value"
              class="bg-blue-500 text-white text-xs p-1 rounded-full inline-block m-1"
            >
              {{ option.text }}
              <span
                @click="removeOption(option.value)"
                class="cursor-pointer ml-2"
              >
                &#10005;
              </span>
            </div>
            <div v-else>
              <span class="select-none">
                {{ selectedOptions[0].text }}
              </span>
            </div>
            <div class="absolute inset-y-0 right-0 pr-3 flex items-center">
              <i class="fas fa-caret-down"></i>
            </div>
          </div>
        </a>
        <div class="dropdown w-64 z-50 bg-white rounded-lg mt-3 border border-gray-300"
            :class="{ 'hidden': dropDowntoggled, 'absolute': !dropDowntoggled }"
        >
          <ul class="mt-2 overflow-y-auto max-h-40">
            <li
              v-for="option in options"
              :key="option.id"
              @click="toggleOption(option)"
              class="cursor-pointer py-2 px-4 hover:bg-gray-100"
            >
              {{ option.text}}
            </li>
          </ul>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      selectedOptions: [],
      dropDowntoggled: true,
    };
  },

  props: {
    maxSelect: {
      type: Number,
      default: 1,
    },
    placeholder: {
      type: String,
      default: "Select an option",
    },
    options: {
      type: Array,
      required: true,
      validator: (value) => {
        return value.every((option) => {
          return option.hasOwnProperty('text') && option.hasOwnProperty('value');
        });
      },
    }, 
  },

  mounted() {
    document.addEventListener('click', this.handleOutsideClick);
    this.selectedOptions = this.options.filter((option) => option.init_value).slice(0, this.maxSelect);
  },

  beforeDestroy() {
    document.removeEventListener('click', this.handleOutsideClick);
  },

  methods: {
    toggleOption(option) {
      if (this.selectedOptions.length == 1 && this.maxSelect == 1) {
        this.selectedOptions = [];
      }
      if (this.selectedOptions.includes(option)) {
        this.selectedOptions = this.selectedOptions.filter(
          (selectedOption) => selectedOption !== option
        );
      } else {
        if (this.selectedOptions.length < this.maxSelect) {
          this.selectedOptions.push(option);
        }
      }
      this.$emit('select', this.maxSelect > 1 ? this.selectedOptions : this.selectedOptions[0]);
      this.toggleDropDown();
    },

    removeOption(value) {
      this.selectedOptions = this.selectedOptions.filter(
        (selectedOption) => selectedOption.value !== value
      );
      this.$emit('select', this.maxSelect > 1 ? this.selectedOptions : this.selectedOptions[0]);
    },

    toggleDropDown() {
      this.dropDowntoggled = !this.dropDowntoggled;
    },
  },
};
</script>

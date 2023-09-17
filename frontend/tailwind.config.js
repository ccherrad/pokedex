/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'dark-pattern': "url('@/static/body_bg.png')",
        'light-pattern': "url('@/static/container_bg.png')",
      }
    },
  },
  plugins: [],
}


<template>
    <div class="text-center">
        <p class="font-semibold">{{  name }}</p>
        <div class="bg-gray-300 h-2 rounded-full">
            <div class="bg-green-400 h-2 rounded-full" :style="{ width: `${value / 2.55}%` }"></div>
        </div>
        <p class="mt-2 text-gray-600">{{ value }} / 255</p>
    </div>
</template>

<script>

export default {
    props: {
        name: {
            type: String,
            required: true,
        },
        value: {
            type: Number,
            required: true,
        }
    }
}
</script>
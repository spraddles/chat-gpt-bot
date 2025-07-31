<template>
  <div :class="['message', positionClass]">
    {{ content }}
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  position: {
    type: String,
    default: 'left',
    validator: (val) => ['left', 'right'].includes(val)
  },
  content: {
    type: String,
    required: true
  }
})

const positionClass = computed(() => {
  return props.position === 'right'
    ? 'float-right bg-indigo-600 text-white'
    : 'float-left bg-gray-200 text-gray-800'
})
</script>

<style scoped>
.message {
  clear: both;
  display: inline-block;
  max-width: 75%;
  padding: 0.5rem 1rem;
  border-radius: 1rem;
  margin: 0.5rem 0;
}
</style>

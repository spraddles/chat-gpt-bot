<template>
  <button
    :type="type"
    :disabled="props.disabled"
    @click="$emit('click')"
    :class="[
      'rounded-md font-medium transition px-4 py-2 cursor-pointer',
      props.disabled
        ? 'opacity-50 cursor-not-allowed'
        : 'bg-indigo-600 hover:bg-indigo-700 text-white'
    ]"
  >
    <slot>{{ props.text }}</slot>
  </button>
</template>

<script setup>
const props = defineProps({
  text: {
    type: String,
    default: 'Button',
  },
  type: {
    type: String,
    default: 'button',
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['click'])
</script>

<style scoped>
button {
  width: 100px;
}
</style>

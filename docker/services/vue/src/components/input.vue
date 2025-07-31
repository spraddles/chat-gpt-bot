<template>
  <div id="input-wrapper" class="flex w-full space-x-2 border border-gray-300 rounded-xl">

    <!-- Left column: input -->
    <div class="flex-1">
      <input
        :id="id"
        type="text"
        :value="modelValue" 
        @input="$emit('update:modelValue', $event.target.value)"
        :placeholder="placeholder"
        class="w-full p-2 focus:ring-2 focus:ring-indigo-500 placeholder-gray-400"
      />
    </div>

    <!-- Right column: button -->
    <div>
      <Button 
        text="Send"
        @click="$emit('button-click')"
        :disabled="buttonDisable"
      >
        {{ props.buttonText }}
      </Button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: { type: String, default: '' },
  id: {
    type: String,
    default: () => `text-input-${Math.random().toString(36).substr(2, 9)}`
  },
  placeholder: { type: String, default: '' },
  buttonText: { type: String, default: 'Button' },
  buttonDisable: { type: Boolean, default: false }
});
</script>

<style type="css" scoped>
#input-wrapper {
    margin-top: 20px;
    margin-bottom: 100px;
    padding: 20px;
}

input:focus {
  outline: none !important;
  box-shadow: none !important;
  border-color: #d1d5db;
}
</style>
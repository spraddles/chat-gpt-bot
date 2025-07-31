<template>
  <div class="flex flex-col min-h-screen">

    <main class="flex-1 overflow-auto p-6">
    <p>Welcome to your personal GPT!</p>
    <p>To get started, simply type into the prompt below:</p>
      <Thinking :active="false" />
    </main>

    <div class="sticky bottom-0 bg-white p-4">
      <Input
        placeholder="Ask anything..."
        button-text="Send"
        class="w-full"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const messages = ref([])
</script>

<style scoped>
p {
  margin: 0;
}
</style>

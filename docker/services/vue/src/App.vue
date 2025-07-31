<template>
  <div class="flex flex-col min-h-screen">

    <main class="flex-1 overflow-auto p-6">
        <div v-for="(message, messageIndex) in messages" :key="messageIndex">
            <Message :content="message.content" :position="message.position" />
        </div>
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
const messages = ref([
    { position: 'left', content: 'Welcome to your personal GPT!' },
    { position: 'left', content: 'To get started, simply type into the prompt below:' },
])
</script>

<style scoped>
p {
  margin: 0;
}
</style>

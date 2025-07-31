<template>
  <div class="flex flex-col min-h-screen">
    <main class="flex flex-col flex-1 overflow-auto p-6">
      <div v-for="(message, messageIndex) in messages" :key="messageIndex">
        <Message :content="message.content" :position="message.position" />
      </div>
      <Thinking :active="thinking" />
    </main>

    <div class="sticky bottom-0 bg-white p-4">
      <Input
        v-model="prompt"
        @button-click="onSendClick"
        :button-disable="buttonDisable"
        @keyup.enter="onSendClick"
        placeholder="Ask anything..."
        button-text="Send"
        class="w-full"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
const messages = ref([
  { position: "left", content: "Welcome to your personal GPT!" },
  { position: "left", content: "To get started, simply type into the prompt below:" },
])

const prompt = ref("")

const thinking = ref(false)

const buttonDisable = ref(false)

const onSendClick = async () => {
  console.log("Parent got prompt:", prompt.value)
  messages.value.push({ position: "right", content: prompt.value })
  prompt.value = ""
  buttonDisable.value = true
  await new Promise((resolve) => setTimeout(resolve, 1000))
  thinking.value = true
  await new Promise((resolve) => setTimeout(resolve, 2000))

  messages.value.push({ position: "left", content: 'This is an example response!' })

  thinking.value = false
  buttonDisable.value = false
}
</script>

<style scoped>
p {
  margin: 0
}
</style>

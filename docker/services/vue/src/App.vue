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
import { useBaseStore } from './stores/base.js'

const store = useBaseStore()
const { sendChat } = store

const messages = ref([
  { position: "left", content: "Welcome to your personal GPT!" },
  { position: "left", content: "Please go easy on me, I only have a small model open-source model (EleutherAI/gpt-neo-125M), so I'm not very smart 😅" },
])

const prompt = ref("")

const thinking = ref(false)

const buttonDisable = ref(false)

const onSendClick = async () => {
  buttonDisable.value = true
  messages.value.push({ position: "right", content: prompt.value })
  var tempValue = prompt.value
  prompt.value = ""
  thinking.value = true
  const chatResponse = await sendChat(tempValue)
  await new Promise((resolve) => setTimeout(resolve, 2000))
  messages.value.push({ position: "left", content: chatResponse })
  thinking.value = false
  buttonDisable.value = false
}
</script>

<style scoped>
p {
  margin: 0
}
</style>

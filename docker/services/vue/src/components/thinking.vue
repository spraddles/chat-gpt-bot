<template>
  <div v-if="props.active" class="typing-indicator">
    <span class="dot" :style="{ animationDelay: '0s' }"></span>
    <span class="dot" :style="{ animationDelay: '0.2s' }"></span>
    <span class="dot" :style="{ animationDelay: '0.4s' }"></span>
  </div>
</template>

<script setup>
const props = defineProps({
  active: {
    type: Boolean,
    default: false,
  },
});
</script>

<style scoped>
.typing-indicator {
  display: inline-flex;
  align-items: center;
  background-color: #e5e5ea;
  padding: 12px 16px;
  border-radius: 16px;
  min-width: 80px;
  justify-content: space-between;
}

.dot {
  width: 8px;
  height: 8px;
  background-color: #555;
  border-radius: 50%;
  animation: blink 1.4s infinite both;
  opacity: 0.2;
}

@keyframes blink {
  0%,
  80%,
  100% {
    opacity: 0.2;
  }
  40% {
    opacity: 1;
  }
}
</style>

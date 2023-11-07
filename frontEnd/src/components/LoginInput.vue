<script setup lang="ts">
const props = defineProps<{
  modelValue: string;
}>();
const emit = defineEmits<{
  (e: "update:modelValue", value: string): void;
}>();
function handleInput(e: any) {
  emit("update:modelValue", e.target.value);
}
</script>

<template>
  <div class="input-container">
    <input
      v-bind="$attrs"
      class="input"
      :value="modelValue"
      @input="handleInput"
    />
  </div>
</template>

<style scoped lang="scss">
.input-container {
  border: 1px solid #e4e4e4;
  border-radius: 4px;
  background-color: #f7f7f7;
  padding: 8px;
  border-radius: 20px;
  width: 250px;
  box-shadow:
    // -4px -4px 20px -8px rgba(255, 255, 255, 1),
    4px 4px 20px -8px rgba(0, 0, 0, 0.3);
  .input {
    border: none;
    outline: none;
    width: 100%;
    background-color: transparent;
    font-size: 16px;
    color: #333;
  }
}
</style>

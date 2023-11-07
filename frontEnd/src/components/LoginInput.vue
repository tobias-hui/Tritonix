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
  <div>
    <input :value="modelValue" @input="handleInput" type="text" />
  </div>
</template>

<style scoped></style>

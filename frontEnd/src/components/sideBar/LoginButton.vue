<script setup lang="ts">
import { useEventBus } from "@vueuse/core";
const openModalBus = useEventBus("openModalBus");

function handleClick() {
  openModalBus.emit();
}
</script>

<template>
  <div
    @click="handleClick"
    :style="{
      backgroundColor: '#37CAFF',
      cursor: 'pointer',
      width: '120px',
      height: '40px',
      display: 'inline-flex',
      justifyContent: 'center',
      alignItems: 'center',
      fontWeight: 'bold',
      color: '#fff',
      borderRadius: '20px',
    }"
  >
    登录
  </div>
</template>

<style scoped></style>

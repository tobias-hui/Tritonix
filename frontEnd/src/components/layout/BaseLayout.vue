<script setup lang="ts"></script>

<template>
  <div class="container">
    <slot name="topBar"></slot>
    <div style="width: 100%; flex: 1;display:flex;">
      <slot name="leftBar"></slot>
      <slot name="mainContainer"></slot>
    </div>
  </div>
</template>

<style scoped lang="scss">
.container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
}
</style>

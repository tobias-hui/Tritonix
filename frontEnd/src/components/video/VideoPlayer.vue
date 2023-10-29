<script setup lang='ts'>
import { defineProps } from 'vue';
const props = defineProps({
  src: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="videoContainer">
    <video controls :src="props.src">

    </video>
  </div>
</template>

<style scoped lang="scss">
.videoContainer {
  width: 100%;
  height: 100%;

  video {
    width: 100%;
    height: 100%;
  }
}
</style>
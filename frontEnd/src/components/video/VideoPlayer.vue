<script setup lang='ts'>
import { ref, Ref, onMounted, reactive, onBeforeUnmount } from 'vue';
import videojs from 'video.js';
import Player from 'video.js/dist/types/player';
import 'video.js/dist/video-js.css'


const props = defineProps<{
  options: Object
}>()
const videoRef: Ref<null | HTMLVideoElement> = ref(null)
const player = ref<Player>()

onMounted(() => {

  if (!videoRef.value) return;
  player.value = videojs(videoRef.value, props.options, () => {
    player.value?.log('onPlayerReady', player)
    
  })
})
onBeforeUnmount(() => {
  if (player.value) {
    player.value.dispose()
  }
})
function handleMouseDown(e:MouseEvent){
  console.log('video mouseDown');
  e.stopPropagation()
}
</script>

<template>
  <div class="videoContainer">
    <video ref="videoRef" class="video-js"  @mousedown="handleMouseDown"/>
  </div>
</template>

<style scoped lang="scss">
.videoContainer {
  width: 100%;
  height: 100%;
}
</style>
<script setup lang="ts">
import { ref, Ref, onMounted, reactive, onBeforeUnmount, watch } from "vue";
// import videojs from "video.js";
// import Player from "video.js/dist/types/player";
import "video.js/dist/video-js.css";
// hook
import useVideo from "./hooks/useVideo";
// type
import { SlideState } from "../slider/type/slide";

const props = defineProps<{
  options: Object;
  active: boolean;
  slideState: SlideState;
}>();
const videoRef: Ref<null | HTMLVideoElement> = ref(null);

const { playerRef, playerState } = useVideo(videoRef, props.options);
onMounted(() => {
  if (!playerRef.value) return;
  playerRef.value.on("click", (e: MouseEvent) => {
    const {timeStamp}=e
    if(timeStamp-props.slideState.mouseDownTimeStamp>100) return;
    console.log("click", e.timeStamp);
    // playerRef.value?.play()
    playerState.isPlaying = !playerState.isPlaying;
  });
});

watch(
  () => props.active,
  (newVal, olaVal) => {
    // console.log('v-watch',newVal);
    if (newVal) {
      playerState.isPlaying = true;
    } else {
      playerState.isPlaying = false;
    }
  }
);
</script>

<template>
  <div class="videoContainer">
    <video ref="videoRef" class="video-js" />
  </div>
</template>

<style scoped lang="scss">
.videoContainer {
  width: 100%;
  height: 100%;
}
</style>

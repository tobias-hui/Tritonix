<script setup lang="ts">
import { ref, Ref, onMounted, reactive, onBeforeUnmount, watch } from "vue";
// import videojs from "video.js";
// import Player from "video.js/dist/types/player";

import "video.js/dist/video-js.css";
// components
import ProgressBar from "./ProgressBar.vue";
// hook
import useVideo from "./hooks/useVideo";
import { useEventBus } from "@vueuse/core";
// type
import { SlideState } from "../slider/type/slide";

const props = defineProps<{
  options: Object;
  active: boolean;
  slideState: SlideState;
}>();
const videoRef: Ref<null | HTMLVideoElement> = ref(null);

const changeVideoStatusBus = useEventBus("changeVideoStatusBus");
const { playerRef, playerState } = useVideo(videoRef, props.options);

onMounted(() => {
  if (!playerRef.value) return;

  changeVideoStatusBus.on((e) => {
    if(!props.active) return;
    const isPaused = playerRef.value?.paused();
    if (isPaused) {
      playerRef.value?.play();
    } else {
      playerRef.value?.pause();
    }
  });
 
});

watch(
  () => props.active,
  (newVal, olaVal) => {
    // console.log('v-watch',newVal);
    // console.log(playerRef.value?.currentTime());

    if (newVal) {
      playerState.isPlaying = true;
    } else {
      playerState.isPlaying = false;
    }
  },
);

</script>

<template>
  <div class="videoContainer">
    <video
      ref="videoRef"
      class="video-js"
      style="background-color: transparent;outline: none;"
    />
    <svg
      v-show="!playerState.isPlaying"
      :style="{
        position: 'absolute',
        left: '50%',
        top: '50%',
        transform: 'translate3d(-50%,-50%,0)',
      }"
      t="1699068972588"
      class="icon"
      viewBox="0 0 1024 1024"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      p-id="1851"
      width="40"
      height="40"
    >
      <path
        d="M889.969872 459.055243L243.248317 20.157773l-0.209453 0.18618A75.147141 75.147141 0 0 0 191.420295 0.003724a73.890422 73.890422 0 0 0-74.635145 73.145699c0 22.202035-0.977448 65.651931 0 64.697756v813.027368A73.890422 73.890422 0 0 0 191.420295 1023.996975a74.984233 74.984233 0 0 0 51.758204-20.503138L889.9466 564.642911A72.144979 72.144979 0 0 0 912.776995 512.000349v-0.325816a72.144979 72.144979 0 0 0-22.807123-52.61929z"
        fill="#ffffff"
        fill-opacity="0.85"
        p-id="1852"
      ></path>
    </svg>
    <ProgressBar :player="playerRef" />
  </div>
</template>

<style scoped lang="scss">
.videoContainer {
  width: 100%;
  height: 100%;
  position: relative;
}
</style>

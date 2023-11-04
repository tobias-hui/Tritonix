<script setup lang="ts">
import { ref } from "vue";
import VideoPlayer from "../video/VideoPlayer.vue";
// type
import { SlideState } from "./type/slide";

const props = defineProps<{
  src: string;
  index: number;
  // mouseDownTimeStamp:number
  slideState: SlideState;
  // transitionY: number
}>();
console.log("slide-item", props, props.index);
function getRandomColor() {
  var r = Math.floor(Math.random() * 256); // 生成 0 到 255 之间的随机整数
  var g = Math.floor(Math.random() * 256);
  var b = Math.floor(Math.random() * 256);
  const color = "rgb(" + r + ", " + g + ", " + b + ")"; // 将三个随机数拼接成 RGB 颜色字符串
  return color;
}
const colorRef = ref(getRandomColor());
</script>

<template>
  <div
    class="swiper-slide"
    :style="{
      backgroundColor: colorRef,
      width: `${slideState.wrapper.width}px`,
      height: `${slideState.wrapper.height}px`,
      top: `${index * slideState.wrapper.height}px`,
      left: `${0}px`,
    }"
  >
    <video-player
      :active="index === slideState.currentIndex"
      :options="{
        autoplay: index === 0,
        // controls: true,
        fill: true,
        sources: [
          {
            src: src,
            type: 'video/mp4',
          },
        ],
      }"
      :slide-state="slideState"
    ></video-player>
  </div>
</template>

<style scoped lang="scss">
.swiper-slide {
  width: 100%;
  position: absolute;
  text-align: center;
  font-size: 18px;
  display: flex;
  justify-content: center;
  align-items: center;
  user-select: none;
}
</style>

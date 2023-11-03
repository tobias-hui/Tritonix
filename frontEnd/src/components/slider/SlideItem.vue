<script setup lang="ts">
import { ref } from "vue";
import VideoPlayer from "../video/VideoPlayer.vue";
const props = defineProps<{
  sliderIndex: number;
  src: string;
  // bgc: string
  size: {
    width: number;
    height: number;
  };
  position: {
    top: number;
    left: number;
  };
  // transitionY: number
}>();
console.log("slide-item", props);
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
      width: `${size.width}px`,
      height: `${size.height}px`,
      top: `${position.top}px`,
      left: `${position.left}px`,
      // transform: `translate3d(0,${transitionY}px,0)`
    }"
  >
    <!-- <div>

      {{ sliderIndex }}
    </div>
    -------
    <div>

      {{ src }}
    </div> -->
    <!-- <video :src="qq1" style="width: 100%;height: 100%;"></video> -->
    <video-player
      :options="{
        autoplay: true,
        controls: true,
        fill: true,
        sources: [
          {
            src: src,
            type: 'video/mp4',
          },
        ],
      }"
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

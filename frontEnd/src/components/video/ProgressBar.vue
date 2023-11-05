<script setup lang="ts">
import { onMounted, onBeforeMount, watch, reactive, ref } from "vue";
import Player from "video.js/dist/types/player";

import { useEventListener } from "@vueuse/core";

const props = defineProps<{
  player: Player | undefined;
}>();
const progressState = reactive({
  total: 0,
  currentTime: 0,
  x: 0,
  isMouseDown: false,
});
// 一秒对应像素
const stepRef = ref(0);
const progressBarRef = ref<HTMLDivElement | null>(null);
watch(
  () => props.player,
  (newVal) => {
    if (!newVal) return;
    console.log("watch");

    newVal.on("loadedmetadata", () => {
      console.log("duration", newVal.duration(), newVal.currentTime());
      progressState.total = newVal.duration()!;
      progressState.currentTime = newVal.currentTime()!;
      stepRef.value =
        progressBarRef.value!.offsetWidth / Math.floor(progressState.total);
      console.log(stepRef.value, "step");

      newVal.on("timeupdate", (e: Event) => {
        progressState.currentTime = Math.ceil(newVal.currentTime()!);
        progressState.x = (progressState.currentTime - 1) * stepRef.value;
        // console.log(progressState.currentTime);
      });
    });
    // console.log(newVal.duration(10), "-----");
  }
);
function handleMouseDown(e: MouseEvent) {
  e.stopPropagation();
  props.player?.pause();
  const { offsetX } = e;
  progressState.isMouseDown = true;
  console.log("down");

  window.addEventListener("mousemove", handleMouseMove, { capture: true });
  window.addEventListener("mouseup", handleMouseUp, { capture: true });
}
// useEventListener(window, "mousemove", handleMouseMove);
// useEventListener(window, "mouseup", handleMouseUp);
function handleMouseMove(e: MouseEvent) {
  e.stopPropagation();
  if (!progressBarRef.value) return;
  changeX(e);
}

function handleMouseUp(e: MouseEvent) {
  e.stopPropagation();
  progressState.isMouseDown = false;
  // 一并处理没有mousemove的点击事件
  changeX(e);
  console.log("end time", progressState.x, progressState.x / stepRef.value);
  progressState.currentTime = progressState.x / stepRef.value;
  props.player?.currentTime(progressState.currentTime);
  props.player?.play();
  // 注意要写参数，不然移除不了
  window.removeEventListener("mousemove", handleMouseMove, { capture: true });
  window.removeEventListener("mouseup", handleMouseUp, { capture: true });
}
function changeX(e: MouseEvent) {
  if (!progressBarRef.value) return;
  const { offsetX, clientX } = e;
  const { left, width, right } = progressBarRef.value.getBoundingClientRect();
  console.log(left, clientX);
  const pointerX = clientX > left + width ? left + width : clientX;
  progressState.x = pointerX - left > 0 ? pointerX - left : 0;
}
// console.log(props.player.duration());
</script>

<template>
  <div
    ref="progressBarRef"
    class="progress-bar"
    @mousedown.capture="handleMouseDown"
  >
    <div
      class="progress"
      :style="{
        width: `${progressState.x}px`,
      }"
    >
      <div class="circle"></div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.progress-bar {
  position: absolute;
  bottom: 10px;
  width: 90%;
  background-color: rgba(255, 255, 255, 0.5);
  height: 4px;
  left: 50%;
  transform: translate3d(-50%, 0, 0);
  border-radius: 2px;
  .progress {
    position: relative;
    background-color: #fff;
    height: 100%;
    width: 50%;
  }
  .circle {
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #fff;
  }
}
</style>

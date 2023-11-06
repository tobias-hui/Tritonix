<script setup lang="ts">
import qq1 from "../../assets/video/qq3.mp4";
// import { getLocalVideos } from "@/mock/resource"
// // vue
import { ref, onMounted, reactive, createApp, App, h, watch } from "vue";
// component
// import { Swiper, SwiperSlide } from 'swiper/vue'
import SlideItem from "./SlideItem.vue";
import Swiper from "swiper";
import { SwiperOptions } from "swiper/types";
import "swiper/scss";
import "swiper/scss/pagination";
import { Pagination } from "swiper/modules";

import VideoPlayer from "@/components/video/VideoPlayer.vue";
// hook

import useSwiper from "./hooks/useSwiper";
import { useEventListener, useEventBus } from "@vueuse/core";

// request
import { getRecommendVideo } from "@/request";
import { getCategories, getVideos } from "@/request/server/video";
// type
// import { RecommendVideo, VideoInfo } from "@/types/video";
import { SlideState } from "./type/slide";
import { VideoInfo, VideoInformation } from "@/types/video";

const props = defineProps<{
  dataList: VideoInformation[];
}>();
const emit = defineEmits<{
  (e: "loadMore"): void;
}>();

const slideState = reactive({
  currentIndex: 0,
  start: {
    x: 0,
    y: 0,
  },
  isMouseDown: false,
  move: { x: 0, y: 0 },
  wrapper: { width: 0, height: 0, childrenLength: 0 },
  lastTransition: {
    x: 0,
    y: 0,
  },
  transition: { x: 0, y: 0 },
  durationTime: 0,
  mouseDownTimeStamp: 0,
});
// const dataList = reactive<VideoInfo[]>([]);

const slideListRef = ref<HTMLDivElement | null>(null);
const wrapperRef = ref<HTMLDivElement | null>(null);

watch(
  () => slideState.currentIndex,
  (newVal, oldVal) => {
    // console.log('watch',newVal, oldVal);
    console.log("currentIndex", newVal);
    if (newVal + 5 > props.dataList.length) {
      emit("loadMore");
    }
    changeDistance(newVal);
  },
);
onMounted(async () => {
  if (!(wrapperRef.value && slideListRef.value)) return;
  slideState.wrapper.width = wrapperRef.value.offsetWidth;
  slideState.wrapper.height = wrapperRef.value.offsetHeight;

  // const res = await getRecommendVideo({ currentPage: 1, currentPageSize: 5 });
  // // console.log(res);
  // Object.assign(dataList, res.videos);
});

function handleVerticalMouseDown(e: MouseEvent) {
  console.log("vertical-slider-mouseDown", e.timeStamp);
  slideState.mouseDownTimeStamp = e.timeStamp;
  slideState.isMouseDown = true;
  slideState.durationTime = 0;
  const { pageX, pageY } = e;
  slideState.start.x = pageX;
  slideState.start.y = pageY;

  // console.log("mouseDown", e, pageX, pageY);
}
function handleVerticalMouseUp(e: MouseEvent) {
  console.log("vertical-slider-mouseUp", e.timeStamp);

  e.preventDefault();
  slideState.isMouseDown = false;
  slideState.durationTime = 0.3;
  // console.log('mouseUp', e);
  const dy = slideState.transition.y - slideState.lastTransition.y;
  // console.log("change", dy);
  if (canSlide(dy, 50)) {
    if (dy > 0) {
      // 列表向下
      if (slideState.currentIndex <= 0) {
        changeDistance(0);
        return;
      }
      const changeIndex = Math.ceil(dy / slideState.wrapper.height);
      // console.log('changeIndex', changeIndex);
      slideState.currentIndex -= changeIndex;
    } else {
      // 向上
      if (slideState.currentIndex === props.dataList.length - 1) {
        changeDistance(slideState.currentIndex);
      } else {
        const changeIndex = -Math.floor(dy / slideState.wrapper.height);
        // console.log('changeIndex', changeIndex);
        slideState.currentIndex += changeIndex;
      }
    }
  } else {
    changeDistance(slideState.currentIndex);
  }

  // console.log(slideState.lastTransition);
}

function handleVerticalMouseMove(e: MouseEvent) {
  // console.log('vertical-slider-mouseMove');
  if (!slideState.isMouseDown) return;

  e.preventDefault();
  // console.log('mouseMove', e);
  // 当前位置
  const { pageX, pageY } = e;

  slideState.move.x = pageX - slideState.start.x;
  slideState.move.y = pageY - slideState.start.y;

  slideState.start.x = pageX;
  slideState.start.y = pageY;

  const dx = slideState.move.x;
  const dy = slideState.move.y;
  // console.log('dx,dy', dx, dy);
  slideState.transition.y += dy;
  // console.log('transition-y', slideState.transition.y);
}
function handleKeyDown(e: KeyboardEvent) {
  // if(!slideListRef.value )return;
  e.preventDefault();
  console.log(e, slideState.currentIndex);
  const { code } = e;
  if (code === "ArrowDown") {
    if (props.dataList.length - 1 > slideState.currentIndex) {
      slideState.currentIndex++;
    }
  } else if (code === "ArrowUp") {
    if (slideState.currentIndex === 0) return;
    slideState.currentIndex--;
  }
}

function canSlide(moveValue: number, judgeValue: number) {
  if (
    Math.abs(moveValue) > judgeValue
    // dataList.length - 1 > slideState.currentIndex
  ) {
    return true;
  } else return false;
}
function getDistance(index: number) {
  return -index * slideState.wrapper.height;
}
function changeDistance(index: number) {
  const distance = getDistance(index);
  slideState.transition.y = distance;
  slideState.lastTransition.x = slideState.transition.x;
  slideState.lastTransition.y = slideState.transition.y;
}
</script>

<template>
  <!-- <div style="padding: 0 10px 0; background-color: pink"> -->
  <div
    class="slide-wrapper"
    ref="wrapperRef"
    @mousedown="handleVerticalMouseDown"
    @mouseup="handleVerticalMouseUp"
    @mousemove="handleVerticalMouseMove"
    @keydown="handleKeyDown"
  >
    <div
      class="slide-list"
      ref="slideListRef"
      :style="{
        transform: `translate3d(0,${slideState.transition.y}px,0)`,
        transitionDuration: `${slideState.durationTime}s`,
      }"
    >
      <SlideItem
        v-for="(item, index) in dataList"
        :key="item.id"
        :src="item.playback_url"
        :index="index"
        :slide-state="slideState"
      />
    </div>
  </div>
  <!-- </div> -->
</template>

<style scoped lang="scss">
.slide-wrapper {
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  // background-color: pink;

  // border: 2px solid red;
  overflow: hidden;
  border-radius: 10px;
  .slide-list {
    // width: 100%;
    box-sizing: border-box;
    position: relative;
  }
}
</style>

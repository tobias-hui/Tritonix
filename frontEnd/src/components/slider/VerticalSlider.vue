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
// type
import { RecommendVideo, VideoInfo } from "@/types/video";

const eventBus = useEventBus("swiper");
// eventBus.on(()=>{
//   console.log('reach')
//   const e=createEl(5,qq1)
//   const firstChild=swiperWrapperRef.value!.firstChild
//   console.log('firstChild',firstChild);

//   swiperWrapperRef.value?.removeChild(firstChild)
//   swiperWrapperRef.value?.appendChild(e)
// })
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
});
const dataList = reactive<VideoInfo[]>([]);
const sliderMap = new Map<number, App<Element>>();
const slideListRef = ref<HTMLDivElement | null>(null);
const wrapperRef = ref<HTMLDivElement | null>(null);
const arr = reactive([]);

watch(dataList, (newVal, oldVal) => {
  console.log("watch", wrapperRef.value && slideListRef.value);
  // for (let i = 0; i < testCount; i++) {
  //   const e = createEl(i, qq1)
  //   slideListRef.value?.appendChild(e)
  //   console.log('finish');

  // }
});
onMounted(async () => {
  if (!(wrapperRef.value && slideListRef.value)) return;
  slideState.wrapper.width = wrapperRef.value.offsetWidth;
  slideState.wrapper.height = wrapperRef.value.offsetHeight;

  // const res = await getRecommendVideo({ currentPage: 1, currentPageSize: 5 })
  // Object.assign(arr, res.videos)
  // console.log(res);
  const res = await getRecommendVideo({ currentPage: 1, currentPageSize: 5 });
  console.log("res", res);
  const newData = res.videos.map((item) => {});
  Object.assign(dataList, res.videos);
});
const { swiperRef } = useSwiper();

function handleClick(
  swiper: Swiper,
  e: MouseEvent | TouchEvent | PointerEvent
) {
  // e.stopPropagation()
  console.log("click", swiper, e);
  // e.stopPropagation()
}
function handleScroll() {
  console.log("scroll");
}
function handleMouseDown(e: MouseEvent) {
  slideState.isMouseDown = true;
  slideState.durationTime = 0;
  const { pageX, pageY } = e;
  slideState.start.x = pageX;
  slideState.start.y = pageY;

  console.log("mouseDown", e, pageX, pageY);
}
function handleMouseUp(e: MouseEvent) {
  slideState.isMouseDown = false;
  slideState.durationTime = 0.3;
  // console.log('mouseUp', e);
  const dy = slideState.transition.y - slideState.lastTransition.y;
  console.log("change", dy);
  if (canSlide(dy, 50)) {
    if (dy > 0) {
      // 列表向下
      if (slideState.currentIndex <= 0) return;
      const changeIndex = Math.ceil(dy / slideState.wrapper.height);
      // console.log('changeIndex', changeIndex);
      slideState.currentIndex -= changeIndex;
    } else {
      // 向上
      const changeIndex = -Math.floor(dy / slideState.wrapper.height);
      // console.log('changeIndex', changeIndex);
      slideState.currentIndex += changeIndex;
    }
  }
  changeDistance();

  slideState.lastTransition.x = slideState.transition.x;
  slideState.lastTransition.y = slideState.transition.y;
  // console.log(slideState.lastTransition);
}

function handleMouseMove(e: MouseEvent) {
  if (!slideState.isMouseDown) return;
  // console.log('mouseMove', e);
  // 当前位置
  const { pageX, pageY } = e;

  // const lastX = slideState.move.x
  // const lastY = slideState.move.y

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

function canSlide(moveValue: number, judgeValue: number) {
  if (Math.abs(moveValue) > judgeValue) {
    return true;
  } else return false;
}
function getDistance() {
  return -slideState.currentIndex * slideState.wrapper.height;
}
function changeDistance() {
  const distance = getDistance();
  slideState.transition.y = distance;
}

/* function createEl(sliderIndex: number, src: string) {
  const app = createApp({
    render: () => h(SlideItem, {
      sliderIndex,
      src,
      bgc: getRandomColor()
    })
  })
  const parent = document.createElement('div')
  const insertELement = app.mount(parent)
  sliderMap.set(sliderIndex, app)
  console.log(sliderMap);

  return insertELement.$el
} */
</script>

<template>
  <div style="padding: 0 10px 0; background-color: pink">
    <div
      class="slide-wrapper"
      ref="wrapperRef"
      @mousedown="handleMouseDown"
      @mouseup="handleMouseUp"
      @mousemove="handleMouseMove"
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
          :slider-index="index"
          :src="item.url"
          :position="{
            left: 0,
            top: slideState.wrapper.height * index,
          }"
          :size="{
            width: slideState.wrapper.width,
            height: slideState.wrapper.height,
          }"
        />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.slide-wrapper {
  width: 400px;
  height: 600px;
  box-sizing: border-box;
  background-color: pink;

  // border: 2px solid red;
  // overflow: hidden;
  .slide-list {
    // width: 100%;
    box-sizing: border-box;
    position: relative;
  }
}
</style>

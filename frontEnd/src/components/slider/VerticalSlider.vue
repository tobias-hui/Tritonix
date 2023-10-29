<script setup lang='ts'>
import qq1 from "../../assets/video/qq5.mp4"
// import { getLocalVideos } from "@/mock/resource"
// // vue
// import { ref, onMounted } from 'vue'
// component
import { Swiper, SwiperSlide } from 'swiper/vue'
import 'swiper/css'
import 'swiper/css/pagination';
import { Pagination } from 'swiper/modules';

import VideoPlayer from "@/components/video/VideoPlayer.vue"
// hook
import { useOffsetPagination } from "@vueuse/core"
import { onMounted } from "vue";
// request
import { getRecommendVideo } from "@/request";

onMounted(async () => {
  const res = await getRecommendVideo({ currentPage: 1, currentPageSize: 5 })
  

})


const {
  currentPage,
  currentPageSize,
  pageCount,
  isFirstPage,
  isLastPage,
  prev,
  next,
} = useOffsetPagination({
  total: 18,
  page: 1,
  pageSize: 5,

})

</script>

<template>
  <div class="sliderContent">

    <swiper :direction="'vertical'" :pagination="{
      clickable: true,
    }" :modules="[Pagination]" class="mySwiper">
      <swiper-slide v-for="item in 5">
        <video-player :src="qq1"></video-player>
      </swiper-slide>

    </swiper>
  </div>
</template>

<style scoped lang="scss">
.sliderContent {
  width: 300px;
  height: 400px;
  background-color: #F1F3F4;
}

.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: gray;

  /* Center slide text vertically */
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
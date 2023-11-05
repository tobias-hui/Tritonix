<template>
  <div class="app">
    <VerticalSlider></VerticalSlider>
    <!-- <useOffsetPagination></useOffsetPagination> -->
  </div>
</template>

<script setup lang="ts">
// import { getRecommendVideo } from "./request"
// import { getLocalVideos } from "@/mock/resource";
import VerticalSlider from "@/components/slider/VerticalSlider.vue";
import useOffsetPagination from "./demo/useOffsetPagination.vue";

// function getVideo() {
//   // getRecommendVideo({ pageCount: 0, pageSize: 10 })
//   getLocalVideos()
// }
</script>

<style scoped lang="scss">
.app {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>

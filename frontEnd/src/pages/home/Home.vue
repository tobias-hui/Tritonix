<script setup lang="ts">
import {
  getCurrentInstance,
  onBeforeUpdate,
  onUpdated,
  reactive,
  onMounted,
} from "vue";
import { useRouter, useRoute } from "vue-router";
// component
import VerticalSlider from "@/components/slider/VerticalSlider.vue";
// type
import { VideoInformation, VideoInfo } from "@/types/video";
// request
import { getVideos, getRecommendVideos } from "@/request/server/video";
// mock
import { getRecommendVideo } from "@/request/mock/video";

const dataList = reactive<VideoInformation[]>([]);
const pageState = reactive({
  category: "",
  currentPage: 0,
  size: 10,
});
const router = useRouter();
const route = useRoute();
pageState.category = route.fullPath.slice(1);
console.log("path", route.fullPath, pageState.category);
onMounted(async () => {
  loadVideo();
});
async function loadVideo() {
  const res = await getVideos({
    category_id: pageState.category,
    page: pageState.currentPage,
    size: pageState.size,
  });
  console.log("res", res);
  // Object.assign(dataList, res);
  if (res === undefined) return;
  for (let item of res) {
    dataList.push(item);
  }
  console.log("dataList", dataList);
}
// const { ctx } = getCurrentInstance() as any;
// const forceUpdate = () => {
//   ctx.$forceUpdate();
// };
function handleLoadMore() {
  console.log("loadMore");
  pageState.currentPage++;
  loadVideo();
}
onBeforeUpdate(() => {
  console.log("onBeforeUpdate");
});
onUpdated(() => {
  console.log("onUpdated");
});
</script>

<template>
  <div class="home">
    <VerticalSlider
      :data-list="dataList"
      @load-more="handleLoadMore"
    ></VerticalSlider>
  </div>
</template>

<style scoped lang="scss">
.home {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}
</style>

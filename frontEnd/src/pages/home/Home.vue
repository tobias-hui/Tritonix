<script setup lang="ts">
import {
  getCurrentInstance,
  onBeforeUpdate,
  onUpdated,
  reactive,
  onMounted,
  ref,
  nextTick,
} from "vue";
import { useRouter, useRoute } from "vue-router";
// component
import VerticalSlider from "@/components/slider/VerticalSlider.vue";
import LoadingPage from "@/components/LoadingPage.vue";
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
const refreshKeyRef = ref(true);
const isLoading = ref(false);
const router = useRouter();
router.afterEach(async (to, from, failure) => {
  console.log(to.name);
  pageState.category = to.name as string;
  pageState.currentPage = 0;
  isLoading.value = true;
  // 销毁slider重新渲染
  refreshKeyRef.value = false;
  dataList.splice(0, dataList.length);
  await loadVideo();
  isLoading.value = false;
  refreshKeyRef.value = true;
});
// const route = useRoute();
// pageState.category = route.fullPath.slice(1);
pageState.category = router.currentRoute.value.name as string;
onMounted(async () => {
  isLoading.value = true;
  loadVideo().finally(() => {
    isLoading.value = false;
  });
});
async function loadVideo() {
  let res: VideoInformation[] | undefined;
  if (pageState.category === "recommend") {
    res = await getRecommendVideos({
      page: pageState.currentPage,
      size: pageState.size,
    });
  } else {
    res = await getVideos({
      category_id: pageState.category,
      page: pageState.currentPage,
      size: pageState.size,
    });
  }
  console.log("res", res);
  // Object.assign(dataList, res);
  if (res === undefined) return;
  for (let item of res) {
    dataList.push(item);
  }
  console.log("dataList", dataList);
}

function handleLoadMore() {
  console.log("loadMore");
  pageState.currentPage++;
  isLoading.value = true;
  loadVideo().finally(() => {
    isLoading.value = false;
  });
}
</script>

<template>
  <div class="home">
    <LoadingPage v-show="isLoading" />
    <VerticalSlider
      v-if="refreshKeyRef"
      v-show="!isLoading"
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

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
import { VideoInformation } from "@/types/video";
// request
import { getVideos } from "@/request/server/video";

const dataList = reactive<VideoInformation[]>([]);
const router = useRouter();
const route = useRoute();
const category = route.fullPath.slice(1);
console.log("path", route.fullPath);
onMounted(async () => {
  const res=await loadVideo()
  console.log(res[0].frame_url===res[0].cover_url,'123124214214124124');
  console.log(res[0].cover_url);
  console.log(res[0].frame_url);
  
  // Object.assign(dataList,res)
});
async function loadVideo() {
  const res =await getVideos({ category_id: category, page: 1, size: 10 });
  return res as VideoInformation[]
  
}
// const { ctx } = getCurrentInstance() as any;
// const forceUpdate = () => {
//   ctx.$forceUpdate();
// };
onBeforeUpdate(() => {
  console.log("onBeforeUpdate");
});
onUpdated(() => {
  console.log("onUpdated");
});
</script>

<template>
  <div class="home">
    <VerticalSlider :data-list="dataList"></VerticalSlider>
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

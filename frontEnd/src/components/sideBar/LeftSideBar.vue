<script setup lang="ts">
import SideBarItem from "./SideBarItem.vue";
import { reactive } from "vue";

const sideList = reactive([
  {
    name: "推荐",
    url: "/",
  },
  {
    name: "二次元",
    url: "/Otaku",
  },
  {
    name: "体育",
    url: "/sports",
  },
  {
    name: "宠物",
    url: "/pet",
  },
]);
</script>

<template>
  <div class="side-bar">
    <SideBarItem
      v-for="item in sideList"
      :name="item.name"
      :url="item.url"
    ></SideBarItem>
  </div>
</template>

<style scoped lang="scss">
.side-bar {
  width: 80px;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-content:start;
  // background-color: pink;
}
</style>

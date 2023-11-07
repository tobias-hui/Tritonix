<script setup lang="ts">
import SideBarItem from "./SideBarItem.vue";
import LoginButton from "./LoginButton.vue";
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

    <div
      style="
        height: 1px;
        width: 90%;
        margin: 20px 0 20px;
        background-color: #dbdcdd;
      "
    />
    <LoginButton></LoginButton>
  </div>
</template>

<style scoped lang="scss">
.side-bar {
  width: 160px;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-content: start;
  // background-color: pink;
}
</style>

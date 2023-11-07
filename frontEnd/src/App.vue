<template>
  <div class="app">
    <BaseLayout>
      <template #topBar>
        <TopBar></TopBar>
      </template>
      <template #leftBar>
        <LeftSideBar></LeftSideBar>
      </template>

      <template #mainContainer>
        <MainContainer>
          <router-view v-slot="{ Component }">
            <transition :name="''">
              <component :is="Component" />
            </transition>
          </router-view>
        </MainContainer>
      </template>
    </BaseLayout>
    
    <LoginContainer></LoginContainer>
    <!-- <VerticalSlider></VerticalSlider> -->
    <!-- <useOffsetPagination></useOffsetPagination> -->
  </div>
</template>

<script setup lang="ts">
import BaseLayout from "@/components/layout/BaseLayout.vue";
import MainContainer from "@/components/layout/MainContainer.vue";
// import { getRecommendVideo } from "./request"
// import { getLocalVideos } from "@/mock/resource";
import LoginContainer from "./components/LoginContainer.vue";
import VerticalSlider from "@/components/slider/VerticalSlider.vue";
import useOffsetPagination from "./demo/useOffsetPagination.vue";
import LeftSideBar from "@/components/sideBar/LeftSideBar.vue";
import TopBar from "@/components/topBar/TopBar.vue";
</script>

<style scoped lang="scss">
.app {
  height: 100vh;
  width: 100vw;
}
</style>

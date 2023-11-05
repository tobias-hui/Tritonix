<script setup lang="ts">
import { SideItemInfo } from "./sideBar";
import { useRouter } from "vue-router";
const props = defineProps<SideItemInfo>();

const router = useRouter();
function handleClick() {
  router.push(`${props.url}`);
}
</script>

<template>
  <div class="container" :style="{}" @click="handleClick">
    {{ name }}
  </div>
</template>

<style scoped lang="scss">
.container {
  height: 50px;
  width: 50px;
  color: rgba(52, 51, 51, 0.8);
  font-weight: bold;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  background-color: #fff;
  cursor: pointer;
  border-radius: 12px;
  margin-top: 10px;
}
.container:hover {
  background-color: #f7f7f7;
}
</style>

<script setup lang="ts">
import { SideItemInfo } from "./sideBar";
import { useRouter } from "vue-router";
import { ref, computed } from "vue";
const props = defineProps<SideItemInfo>();

const router = useRouter();
const currentUrlRef = ref(router.currentRoute.value.fullPath);
const isMoveIn = ref(false);
const bgColor = computed(() => {
  if (isMoveIn.value) return "#E5E5E5";
  return props.url === currentUrlRef.value ? "#E5E5E5" : "#fff";
});

router.afterEach((to, from) => {
  currentUrlRef.value = to.fullPath;
});

function handleClick() {
  router.push(`${props.url}`);
}
function handleMouseOver() {
  isMoveIn.value = true;
}
function handleMouseLeave() {
  isMoveIn.value = false;
}
</script>

<template>
  <div
    class="container"
    :style="{
      backgroundColor: bgColor,
    }"
    @click="handleClick"
    @mouseover="handleMouseOver"
    @mouseleave="handleMouseLeave"
  >
    {{ name }}
  </div>
</template>

<style scoped lang="scss">
.container {
  height: 50px;
  width: 128px;
  color: rgba(52, 51, 51, 0.8);
  font-weight: bold;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  background-color: #fff;
  cursor: pointer;
  border-radius: 12px;
  margin-top: 10px;
  transition: all 0.3s;
}
// .container:hover {
//   background-color: #e5e5e5;
// }
</style>

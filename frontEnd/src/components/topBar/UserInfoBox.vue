<script setup lang="ts">
import { ref, onMounted, reactive } from "vue";
import { useEventListener } from "@vueuse/core";
import { ElPopover } from "element-plus";
const props = defineProps<{
  src: string;
  userName: string;
}>();
const fatherRef = ref<null | HTMLDivElement>(null);
const isShow = ref(false);
const position = reactive({
  top: 0,
  left: 0,
});
onMounted(() => {
  if (!fatherRef.value) return;
  const rect = fatherRef.value.getBoundingClientRect();
  position.left = rect.left + 10;
  position.top = rect.top + rect.height + 10;
});
function handleMouseEnter() {
  isShow.value = true;
}
function handleMouseLeave() {
  isShow.value = false;
}
function logout() {
  localStorage.removeItem("token");
  location.reload();
}
</script>

<template>
  <ElPopover placement="top-start" :width="200" trigger="hover">
    <template #reference>
      <div
        class="user-capsule"
        ref="fatherRef"
        @mouseenter="handleMouseEnter"
        @mouseleave="handleMouseLeave"
      >
        <img :src="src" alt="User Avatar" class="avatar" />
        <span class="username">{{ userName }}</span>
      </div>
    </template>
    <div
      class="btn"
      @click="logout"
      :style="{
        display: 'inline-flex',
        justifyContent: 'center',
        alignItems: 'center',
        fontWeight: 'bold',
        color: 'red',
        cursor: 'pointer',
        padding: '10px 0 10px',
        width: '150px',
        borderRadius: '10px',
        // width:'100%'
      }"
    >
      退出登录
    </div>
  </ElPopover>
</template>
<!-- <div
      v-show="isShow"
      :style="{
        position: 'fixed',
        zIndex: 101,
        top: `${position.top}px`,
        left: `${position.left}px`,
        backgroundColor: '#fff',
        borderRadius: '5px',
        width: '150px',
        height: '40px',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        fontWeight: 'bold',
        color: 'red',
        transition: 'all 0.5s',
      }"
      >
      <div>退出登录</div>
    </div> -->

<style scoped lang="scss">
.btn:hover {
  background-color: #e8eaed;
}
.user-capsule {
  position: relative;
  display: flex;
  align-items: center;
  border: 1px solid #ccc;
  border-radius: 20px;
  padding: 5px 10px;
  background-color: #f2f2f2;
  cursor: pointer;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  margin-right: 10px;
}

.username {
  font-weight: bold;
}
</style>

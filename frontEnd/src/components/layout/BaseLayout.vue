<template>
  <div class="container">
    <!-- 背景图片 -->
    <div class="fullscreen-background"></div>

    <!-- 页面顶部的栏位 -->
    <slot name="topBar"></slot>

    <!-- 页面主体的布局 -->
    <div style="width: 100%; flex: 1; display: flex;">
      <!-- 侧边栏 -->
      <slot name="leftBar"></slot>
      <!-- 主容器 -->
      <slot name="mainContainer"></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
// TypeScript脚本（如果有需要）
</script>

<style scoped lang="scss">
.container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  position: relative; /* 为了定位背景图片 */
}

.fullscreen-background {
  position: absolute; /* 绝对定位 */
  top: 0;
  left: 0;
  width: 100%; /* 背景宽度 */
  height: 100%; /* 背景高度 */
  background: url('@/assets/background.png') no-repeat center center; 
  background-size: cover; /* 背景图片覆盖整个元素 */
  z-index: -1; /* 确保背景在内容之下 */
}
</style>

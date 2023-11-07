<script setup lang="ts">
import { SyncRefOptions } from "@vueuse/core";
import SideBarItem from "./SideBarItem.vue";
import { reactive } from "vue";
import { ref } from 'vue';

const sideList = reactive([
  {
    name: "推荐",
    url: "/",
  },
  {
    name: "知识",
    url: "/",
  },
  {
    name: "体育",
    url: "/sports",
  },
  {
    name: "宠物",
    url: "/pet",
  },
  {
    name: "娱乐",
    url: "/",
  },
  {
    name: "美食",
    url: "/",
  },
  {
    name: "二次元",
    url: "/Otaku",
  },
]);
// 当前激活的项
const currentActive = ref('');

// 设置当前激活的项
const selectItem = (itemName: string) => {
  currentActive.value = itemName;
};

</script>

<template>
  <div class="side-bar">
    <!-- 侧边栏容器 -->
    <div class="sidebar-container">
      <!-- 循环遍历侧边栏条目 -->
      <SideBarItem
        v-for="item in sideList"
        :key="item.name"
        :name="item.name"
        :url="item.url"
        :class="{ 'sidebar-item': true, active: item.name === currentActive }"
        @click="selectItem(item.name)"
      >
        {{ item.name }}
      ></SideBarItem>

      <!-- 插入的图片 -->
      <a href="https://colingo.ai/copilot/22e2bdc21c3a35ade2ec" class="image-link">
        <img src="@/assets/toothless.png" alt="Toothless" class="sidebar-image">
        <!-- 图片下方的文字 -->
        <span class="image-text">Tritonix AI</span>
      </a>

      <!-- 新增的上传按钮 -->
      <div class="special-button" @click="selectItem('upload')">
        <!-- 使用img标签引入SVG文件 -->
        <img class="icon" src="@/assets/add.svg" alt="Add">
        <!-- 添加上传文字 -->
        <span class="upload-text">上传</span>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.side-bar {
  width: 10%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-content:start;
  background-color: #191919; /* 侧边栏背景色 */
}

.sidebar-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: #1C1C1C;
  border-radius: 36px; /* 容器圆角 */
  width: 80%; /* 与侧边栏同宽 */
  height: 96%;
  margin-top: 20px; /* 与顶部栏的距离 */
  margin: auto;
  padding: 10px 0; /* 容器内上下内边距 */
}

.sidebar-item {
  display: flex; /* 设置为flex布局 */
  flex-direction: column; /* 子元素垂直排列 */
  align-items: center; /* 子元素水平居中对齐 */
  justify-content: center; /* 子元素垂直居中对齐 */
  background-color: #242424 !important; /* 按钮背景色 */
  border-radius: 24px; /* 按钮圆角 */
  color: #FFFFFF; /* 按钮文字颜色 */
  font-size: 24px;
  font-weight: 400; /* 设置字体字重为普通 */
  font-family: 'Microsoft YaHei', '微软雅黑', 'Heiti SC', '黑体', sans-serif;
  margin: 12px auto; /* 修改为 'auto' 实现水平居中 */
  padding: 10px 0; /* 按钮上下内边距 */
  width: 60%; /* 按钮宽度 */
  height: 4%;
  text-align: center; /* 文字居中 */
  cursor: pointer; /* 鼠标悬停时的指针样式 */
  transition: background-color 0.3s; /* 背景色变化的过渡效果 */
  &:hover {
    background-color: #656567 !important;
    color: #CAFF33; /* 鼠标悬停时的按钮背景色 */
  }
  &.active {
    color: #CAFF33; /* 激活状态的文字颜色 */
  }
}

.image-link {
  display: block; /* 块级元素，使链接填满容器宽度 */
  margin: 32px auto; /* 上下外边距，根据需要调整 */
  text-align: center; /* 使图片在链接内居中 */
  transition: background-color 0.3s; /* 添加过渡效果 */
  border-radius: 16px; /* 添加圆角效果 */

  &:hover {
    background-color: #CAFF33; /* 鼠标悬停时的背景色 */
  }
}

.sidebar-image {
  max-width: 100%; /* 限制图片最大宽度 */
  max-height: 220px; /* 增加图片最大高度 */
  margin-bottom: 16px; /* 在图片和上传按钮之间增加空间 */
}

.image-text {
  color: #CAFF33; /* 文字颜色 */
  font-size: 24px; /* 文字大小 */
  font-weight: 400; /* 设置字体字重为普通 */
  font-family: 'Microsoft YaHei', '微软雅黑', 'Heiti SC', '黑体', sans-serif;
  text-align: center; /* 文字居中 */
  display: block; /* 块级元素，使文本在新的一行显示 */
}


.special-button {
  background-color: #242424; /* 按钮背景色 */
  border-radius: 18px; /* 按钮圆角 */
  width: 70%; /* 按钮宽度 */
  height: 12%;
  display: flex;
  flex-direction: column; /* 使用flex布局使内容居中 */
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  margin: 12px auto; /* 上下外边距 */
  margin-top: auto;
  cursor: pointer; /* 鼠标悬停时的指针样式 */
}

.icon {
  fill: white; /* SVG图标颜色 */
  width: 80px; /* SVG图标宽度 */
  height: 80px; /* SVG图标高度 */
  margin-bottom: 4px;
}
.upload-text {
  color: white; /* 文字颜色 */
  font-size: 16px; /* 文字大小 */
  font-weight: 400; /* 设置字体字重为普通 */
  font-family: 'Microsoft YaHei', '微软雅黑', 'Heiti SC', '黑体', sans-serif;
  text-align: center; /* 文字居中 */
  &:hover {
    color: #CAFF33; /* 鼠标悬停时的按钮背景色 */
  }
}

</style>

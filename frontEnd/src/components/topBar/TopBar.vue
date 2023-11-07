<script setup lang="ts">
// 引入logo图片
import logo from "@/assets/logo.png"; // @ 是 src/ 目录的别名
import { reactive } from "vue";
const screen = reactive({
  width: window.innerWidth,
  height: window.innerHeight,
});
</script>

<template>
  <div
    class="top-bar"
    :style="{
      width: `${screen.width}px`,
      // height: `${screen.height}px`,
    }"
  >
    <div class="bar-container">
      <!-- Logo图片 -->
      <img :src="logo" alt="Logo" class="logo" />
      <!-- 品牌文字 -->
      <span class="brand">Tritonix 潮汐智螈</span>
      <!-- 搜索框和放大镜图标 -->
      <div class="search-container">
        <input
          type="text"
          class="search-box"
          placeholder="搜索你感兴趣的内容"
        />
        <button class="search-button">
          <img src="@/assets/search.svg" alt="搜索" />
        </button>
      </div>
      <!-- 登录和注册按钮（根据你的需求添加） -->
      <button class="signup-button">注册</button>
      <button class="login-button">登录</button>
    </div>
  </div>
</template>

<style scoped lang="scss">
.top-bar {
  // width: 100%;
  overflow: hidden;
  box-sizing: border-box;
  height: 120px;
  background-color: rgba(25, 25, 25, 0.9); /* 背景色 */
  display: flex;
  justify-content: center;
  align-items: center;
}

.bar-container {
  display: flex;
  align-items: center;
  gap: 20px;
  justify-content: space-between;
  background-color: #242424; /* 你可以根据需要更改这个颜色 */
  border-radius: 36px; /* 圆角的大小 */
  padding: 10px 30px; /* 内边距 */
  // box-sizing: border-box;
  width: 82%;
  height: 48px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* 根据需要添加更多的样式，如阴影等 */
}

/* 搜索容器样式 */
.search-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 500px;
  width: 600px; /* 设置宽度为70% */
  height: 92%;
  position: relative;
  //max-width: 600px; /* 你可以设置一个最大宽度 */
}

/* 搜索框样式 */
.search-box {
  padding: 8px 16px;
  min-width: 200px;
  background-color: #242424; /* 搜索框背景颜色 */
  border: 2px solid #ffffff; /* 搜索框边框颜色 */
  border-radius: 14px; /* 圆角边框 */
  font-size: 16px; /* 文本大小 */
  font-family: "Helvetica Neue", Arial, sans-serif;
  color: #ffffff; /* 输入文本颜色 */
  outline: none; /* 移除焦点轮廓 */
  width: 100%; /* 宽度 - 可根据需要调整 */
  //max-width: 300px; /* 最大宽度 */
  box-sizing: border-box; /* 盒模型定义 */
}

/* 搜索按钮样式 */
.search-button {
  background-color: transparent; /* 透明背景 */
  border: none; /* 无边框 */
  cursor: pointer;
  position: absolute;
  right: 20px; /* 右对齐 */
  top: 50%; /* 垂直居中 */
  transform: translateY(-50%); /* 垂直居中的微调 */
}

/* 搜索图标样式 */
.search-button img {
  width: 20px; /* 图标大小 */
  height: 20px; /* 图标大小 */
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo {
  height: 70px; /* 或者你希望的任何尺寸 */
  margin-right: 10px; /* logo和文字之间的间距 */
}

.brand {
  color: white;
  font-size: 24px;
  font-weight: 400; /* 设置字体字重为普通 */
  font-family: "Microsoft YaHei", "微软雅黑", "Heiti SC", "黑体", sans-serif; /* 设置字体 */
  margin-right: auto;
  white-space: nowrap;
  /* 其他你需要的样式 */
}

.signup-button {
  margin-left: 10px;
  padding: 5px 15px;
  background-color: #242424;
  color: #ffffff; /* 登录文字颜色 */
  font-weight: 400; /* 设置字体字重为普通 */
  font-family: "Microsoft YaHei", "微软雅黑", "Heiti SC", "黑体", sans-serif;
  border: 2px solid #242424; /* 边框颜色和大小 */
  border-radius: 30px;
  cursor: pointer;
  &:hover {
    background-color: #656567; /* 按钮悬停效果颜色 */
  }
}

.login-button {
  margin-left: 10px;
  padding: 5px 15px;
  background-color: #242424; /* 按钮背景颜色 */
  color: #caff33; /* 登录文字颜色 */
  font-weight: 400; /* 设置字体字重为普通 */
  font-family: "Microsoft YaHei", "微软雅黑", "Heiti SC", "黑体", sans-serif;
  border: 2px solid #caff33; /* 边框颜色和大小 */
  border-radius: 30px;
  cursor: pointer;
  &:hover {
    background-color: #656567; /* 按钮悬停效果颜色 */
  }
}
</style>

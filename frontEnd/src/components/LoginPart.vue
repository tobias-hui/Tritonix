<script setup lang="ts">
import LoginInput from "./LoginInput.vue";
import MainButton from "./button/MainButton.vue";

import { reactive } from "vue";
import { ModalStatus } from "@/types/components";

const emit = defineEmits<{
  (e: "changeStatus", status: ModalStatus): void;
}>();
const userInfo = reactive({
  username: "",
  password: "",
});

function handleLogin() {}
function changeStatus() {
  emit("changeStatus", "register");
}
</script>

<template>
  <div>
    <div style="padding: 0 20px 0">
      <div
        style="
          color: rgba(0, 0, 0, 0.6);
          font-size: 24px;
          font-weight: bold;
          border-bottom: 2px solid rgba(0, 0, 0, 0.6);
          width: 160px;
          padding-bottom: 10px;
        "
      >
        登录
      </div>
    </div>
    <div>
      <div class="input-wrapper">
        <LoginInput v-model="userInfo.username" placeholder="用户名" />
      </div>
      <div class="input-wrapper">
        <LoginInput
          type="password"
          v-model="userInfo.password"
          placeholder="密码"
        />
      </div>
      <div
        style="
          margin-top: 20px;
          display: flex;
          justify-content: center;
          gap: 20px;
        "
      >
        <MainButton :mode="'fill'" @click="handleLogin">登录</MainButton>
        <MainButton :mode="'blank'" @click="changeStatus"
          >没有账户,去注册</MainButton
        >
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.input-wrapper {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin: 20px 0 0;
  width: 100%;
}
</style>

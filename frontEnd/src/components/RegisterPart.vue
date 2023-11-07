<script setup lang="ts">
import { reactive, ref } from "vue";

import LoginInput from "./LoginInput.vue";
import MainButton from "@/components/button/MainButton.vue";

// import { register } from '@/request/server/user';
import { ModalStatus } from "@/types/components";
import { RegisterProps, register } from "@/request/server/user";
import { useThrottleFn, useStorage } from "@vueuse/core";

const emit = defineEmits<{
  (e: "changeStatus", status: ModalStatus): void;
}>();

const userInfo = reactive<RegisterProps>({
  email: "",
  username: "",
  avatar: "https://ibb.co/NrhsTc5",
  password: "",
});

const handleRegister = useThrottleFn(async () => {
  if (!testParams()) return;

    const res = await register(userInfo);
    // console.log("register", res);
    alert("注册成功！");
});

function changeStatus() {
  emit("changeStatus", "login");
}

function testParams() {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(userInfo.email)) {
    alert("错误的邮箱格式");
    return false;
  }
  if (!userInfo.username) {
    alert("用户名不能为空");
    return false;
  }
  if (userInfo.password.length < 6) {
    alert("密码长度应该大于6位");
    return false;
  }
  return true;
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
        新用户注册
      </div>
    </div>
    <div>
      <div class="input-wrapper">
        <LoginInput v-model="userInfo.email" placeholder="邮箱" />
      </div>
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
        <MainButton :mode="'fill'" @click="handleRegister">注册</MainButton>
        <MainButton :mode="'blank'" @click="changeStatus"
          >已有账户,去登录</MainButton
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

<script setup lang="ts">
import { reactive } from "vue";
import LoginInput from "./LoginInput.vue";
import MainButton from "./button/MainButton.vue";
import { ModalStatus } from "@/types/components";
import { login } from "@/request/server/user";

import { closeModalBusKey,loginBusKey } from "@/components/busKey";

import { useThrottleFn, useStorage, useEventBus } from "@vueuse/core";

const emit = defineEmits<{
  (e: "changeStatus", status: ModalStatus): void;
}>();
const closeModalBus = useEventBus(closeModalBusKey);
const loginBus=useEventBus(loginBusKey)
const userInfo = reactive({
  email: "",
  password: "",
});
const handleLogin = useThrottleFn(async () => {
  if (userInfo.email === "" || userInfo.password === "") {
    alert("密码或邮箱为空");
    return;
  }
  const res = await login(userInfo);
  localStorage.removeItem("token");
  const token = useStorage("token", res!.access_token);
  loginBus.emit()
  closeModalBus.emit();
});

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
        <LoginInput v-model="userInfo.email" placeholder="邮箱" />
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

<script setup lang="ts">
import { onClickOutside, useEventBus, EventBusKey } from "@vueuse/core";
import { ref, reactive } from "vue";

import LoginPart from "@/components/LoginPart.vue";
import RegisterPart from "@/components/RegisterPart.vue";
import CloseIcon from "@/components/CloseIcon.vue";

import { ModalStatus } from "@/types/components";

import { openModalBusKey, closeModalBusKey } from "./busKey";

const isOpenModal = ref(false);
const currentStatus = ref<ModalStatus>("login");

const maskSize = reactive({
  width: window.innerWidth,
  height: window.innerHeight,
});

const openModalBus = useEventBus(openModalBusKey);
const closeModalBus = useEventBus(closeModalBusKey);
closeModalBus.on(closeModal);
openModalBus.on(openModal);

function openModal({ type }: { type: ModalStatus }) {
  currentStatus.value = type;
  isOpenModal.value = true;
}
function closeModal() {
  isOpenModal.value = false;
}
function handleChangeStatus(status: ModalStatus) {
  console.log(status);

  currentStatus.value = status;
}
</script>

<template>
  <Transition>
    <div class="login-container" v-if="isOpenModal">
      <div style="padding: 15px; display: flex; flex-direction: row-reverse">
        <CloseIcon @click="closeModal" />
      </div>
      <LoginPart
        v-show="currentStatus === 'login'"
        @changeStatus="handleChangeStatus"
      ></LoginPart>
      <RegisterPart
        v-show="currentStatus === 'register'"
        @changeStatus="handleChangeStatus"
      ></RegisterPart>
    </div>
  </Transition>
  <div
    class="mask"
    v-if="isOpenModal"
    :style="{
      width: `${maskSize.width}px`,
      height: `${maskSize.height}px`,
      backgroundColor: 'rgba(0,0,0,0.3)',
      position: 'fixed',
      left: 0,
      top: 0,
      zIndex: 100,
    }"
  ></div>
</template>

<style scoped lang="scss">
.login-container {
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate3d(-50%, -50%, 0);
  width: 400px;
  height: 410px;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
  z-index: 101;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.2s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>

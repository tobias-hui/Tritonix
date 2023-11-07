<script setup lang="ts">
import { onClickOutside, useEventBus } from "@vueuse/core";
import { ref, reactive } from "vue";

import LoginPart from "@/components/LoginPart.vue";
import RegisterPart from "@/components/RegisterPart.vue";

const isOpenModal = ref(false);
const currentStatus = ref<"login" | "register">("login");

const maskSize = reactive({
  width: window.innerWidth,
  height: window.innerHeight,
});

const closeModalBus = useEventBus("closeModalBus");
const openModalBus = useEventBus("openModalBus");
closeModalBus.on(closeModal);
openModalBus.on(openModal);
function openModal() {
  isOpenModal.value = true;
}
function closeModal() {
  isOpenModal.value = false;
}
</script>

<template>
  <Transition>
    <div class="login-container" v-if="isOpenModal">
      <div style="padding: 15px">
        <div class="close" @click="closeModal">
          <svg
            t="1699291868813"
            class="icon"
            viewBox="0 0 1024 1024"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            p-id="4171"
            width="16"
            height="16"
          >
            <path
              d="M569.578831 512l378.213892-378.213892c15.805954-15.805954 15.805954-41.772878 0-57.578831s-41.772878-15.805954-57.578831 0l-378.213892 378.213892-378.213892-378.213892c-15.805954-15.805954-41.772878-15.805954-57.578831 0l0 0c-15.805954 15.805954-15.805954 41.772878 0 57.578831l378.213892 378.213892-378.213892 378.213892c-15.805954 15.805954-15.805954 41.772878 0 57.578831l0 0c15.805954 15.805954 41.772878 15.805954 57.578831 0l378.213892-378.213892 378.213892 378.213892c15.805954 15.805954 41.772878 15.805954 57.578831 0l0 0c15.805954-15.805954 15.805954-41.772878 0-57.578831L569.578831 512z"
              p-id="4172"
              fill="#43423F"
            ></path>
          </svg>
        </div>
      </div>
      <component
        :is="currentStatus === 'login' ? LoginPart : RegisterPart"
      ></component>
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
  height: 432px;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
  z-index: 101;
  .close {
    width: 35px;
    height: 35px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    border-radius: 50%;
  }
  .close:hover {
    background-color: #f7f7f7;
  }
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

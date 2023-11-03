import { ref, onMounted } from "vue";

import { useEventListener, useEventBus } from "@vueuse/core";

import Swiper from "swiper";
import { SwiperOptions } from "swiper/types";
import "swiper/scss";
import "swiper/scss/pagination";

export default function useSwiper() {
  const eventBus = useEventBus("swiper");
  const currSlider = ref(0);
  const swiperRef = ref<Swiper | null>(null);
  useEventListener(window, "keydown", handleKeyPress);
  onMounted(() => {
    console.log("swiperInit");

    swiperRef.value = new Swiper(".mySwiper", {
      direction: "vertical",
      // pagination: {
      //   el: ".swiper-pagination",
      //   clickable: true,
      // },
      // loop: true,
      // allowTouchMove:false,
      // autoHeight:true,
      on: {
        slideChange(swiper) {
          console.log("active-index", swiper.activeIndex);
          if (swiper.activeIndex === 4) {
            eventBus.emit("react");
          }
        },
      },
    });
  });
  function handleKeyPress(event: KeyboardEvent) {
    const { code } = event;
    // console.log(code);
    if (code === "ArrowDown") {
      swiperRef.value?.slideNext();
      // swiperRef.value?.setProgress(0.01,3000)
    } else if (code === "ArrowUp") {
      swiperRef.value?.slidePrev();
    }
  }
  return {
    swiperRef,
  };
}

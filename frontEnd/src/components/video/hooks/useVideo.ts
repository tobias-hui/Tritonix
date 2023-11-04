import { ref, Ref, onMounted, reactive, onBeforeUnmount, watch } from "vue";
import videojs from "video.js";
import Player from "video.js/dist/types/player";


export default function useVideo(videoRef: Ref<HTMLVideoElement | null>, options: Record<string, any>) {
  const playerRef = ref<Player>();
  const playerState = reactive({
    isPlaying: false
  })
  onMounted(() => {
    if (!videoRef.value) return;
    console.log(options);

    playerRef.value = videojs(videoRef.value, options, () => {
      // playerRef.value?.log("onPlayerReady", player);
    });


  });


  watch(() => playerState.isPlaying, (newVal, oldVal) => {
    if (playerState.isPlaying) {
      playerRef.value?.play()
    } else {
      playerRef.value?.pause()
    }
  })
  onBeforeUnmount(() => {
    if (playerRef.value) {
      playerRef.value.dispose();
    }
  });
  return {
    playerRef,
    playerState
  }
}
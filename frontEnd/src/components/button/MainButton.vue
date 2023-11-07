<script setup lang="ts">
const props = defineProps<{
  mode: "fill" | "blank";
}>();
</script>

<template>
  <div>
    <button class="gradient-button" :class="mode">
      <slot></slot>
    </button>
  </div>
</template>

<style scoped lang="scss">
.gradient-button {
  padding: 10px 20px;
  min-width: 140px;
  border: none;
  border-radius: 20px;

  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  outline: none;
  transition: all 0.3s;
}
.gradient-button:hover {
  box-shadow:
  -4px -4px 20px -8px rgba(255, 255, 255, 1),
  4px 4px 20px -8px rgba(0, 0, 0, 0.5);

}


.fill {
  background: linear-gradient(135deg, #90c31c, #51e66f);
  color: white;
}
.blank {
  background: #fff;
  color:gray
}

// .gradient-button:hover {
//   background: linear-gradient(45deg, #a1c4fd, #c2e9fb);
// }
</style>

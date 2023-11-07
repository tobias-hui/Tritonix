<script setup lang='ts'>
import LoginInput from './LoginInput.vue';

import {ref} from 'vue'

const v=ref('')
</script>

<template>
  <div>
    login
    <div>
      <LoginInput v-model="v"></LoginInput>
      {{ v }}
    </div>
  </div>
</template>

<style scoped>

</style>
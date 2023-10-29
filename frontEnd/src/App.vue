<template>
  <div>
    hello
    <button @click="test">click</button>
  </div>
</template>

<script setup lang="ts">
import {getVideo} from "./request"


function test(){
  getVideo()
}
</script>

<style scoped>

</style>
import { RouteRecordRaw } from "vue-router"
import Home from "@/pages/home/Home.vue"

export const routes: RouteRecordRaw[] = [
  { path: '/', component:Home },

  { path: '/Otaku', component: Home },
  { path: '/sports', component: Home },
  { path: '/pet', component: Home },
]

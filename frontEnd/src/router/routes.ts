import { RouteRecordRaw } from "vue-router"
import Home from "@/pages/home/Home.vue"

export const routes: RouteRecordRaw[] = [
  { path: '/', component: Home, name: 'recommend' },

  { path: '/Otaku', component: Home, name: 'Otaku' },
  { path: '/sports', component: Home, name: 'sports' },
  { path: '/pet', component: Home, name: 'pet' },
]

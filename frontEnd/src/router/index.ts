import {createRouter,createWebHashHistory} from "vue-router"
import Home from "@/pages/home/Home.vue"

import { routes } from "./routes"


export const router = createRouter({
  history: createWebHashHistory(),
  routes
})

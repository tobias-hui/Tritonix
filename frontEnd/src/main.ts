import { createApp } from "vue";
import "./style.scss";
import App from "./App.vue";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import "./mock";
import { router } from "./router";



const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.mount("#app");

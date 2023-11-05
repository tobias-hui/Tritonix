import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": "/src",
    },
  },
  server: {
    proxy: {
      // host:'12',
      '/proxy': {
        target: 'http://118.31.56.248:7860',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/proxy/, '')
      }
    },
    cors: true
  }
});

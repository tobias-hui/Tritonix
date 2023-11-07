import axios from "axios";

// const baseURL='http://127.0.0.1:5173/proxy'
const baseURL = 'http://118.31.56.248:7860'

const instance = axios.create({
  baseURL
});

instance.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config
})
export default instance;

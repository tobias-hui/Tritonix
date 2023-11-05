import axios from "axios";

const baseURL='http://127.0.0.1:5173/proxy'
// const baseURL='http://118.31.56.248:7860'

const instance = axios.create({
  baseURL
});
export default instance;

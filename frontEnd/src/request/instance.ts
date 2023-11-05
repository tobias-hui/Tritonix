import axios from "axios";

const baseURL='http://localhost:5173/'
// const baseURL='http://118.31.56.248:7860/'

const instance = axios.create({
  baseURL
});
export default instance;

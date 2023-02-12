import axios from "axios"
import Vue from "vue";
const apiUrl = 'http://127.0.0.1:8000/';

const axiosIns = axios.create({
    baseURL: apiUrl,
});

Vue.prototype.$http = axiosIns;

export default axiosIns;
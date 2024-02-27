// axios.js
import { inject } from 'vue';
import axios from 'axios';

const apiUrl = 'http://pendu.arkansoap.tech/';
// const apiUrl = 'http://localhost:8000/';

const axiosIns = axios.create({
    baseURL: apiUrl,
});

const AxiosInstanceSymbol = Symbol('AxiosInstance');

export function useAxios() {
  const axiosInstance = inject(AxiosInstanceSymbol);
  if (!axiosInstance) {
    throw new Error('No axios instance provided');
  }
  return axiosInstance;
}

export default {
  install(app) {
    app.provide(AxiosInstanceSymbol, axiosIns);
  }
};

// Export axiosIns directly
export { axiosIns };

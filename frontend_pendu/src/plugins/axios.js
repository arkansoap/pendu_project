import { inject, provide} from 'vue';
import axios from 'axios';

// const apiUrl = 'http://pendu.arkansoap.tech/';
const apiUrl = 'http://127.0.0.1:8000/';

const axiosIns = axios.create({
    baseURL: apiUrl,
});

// Key for providing/injecting axios instance
const AxiosInstanceSymbol = Symbol('AxiosInstance');

export function provideAxios() {
  provide(AxiosInstanceSymbol, axiosIns);
}

export function useAxios() {
  const axiosInstance = inject(AxiosInstanceSymbol);
  if (!axiosInstance) {
    throw new Error('No axios instance provided');
  }
  return axiosInstance;
}

export default axiosIns;
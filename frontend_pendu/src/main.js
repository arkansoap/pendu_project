import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Routes from "./routes"
import Vuetify from 'vuetify'; // Import Vuetify
// import 'vuetify/dist/vuetify.min.css'; // Import Vuetify CSS

Vue.use(VueRouter);
// Vue.use(Vuetify); // Use Vuetify

const router = new VueRouter({
  routes: Routes,
  mode: 'history'
});

new Vue({
  el: '#app',
  router: router,
  // vuetify: new Vuetify(), // Initialize Vuetify instance
  render: h => h(App)
})

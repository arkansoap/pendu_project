import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import { createVuetify } from 'vuetify'
import axiosPlugin from './plugins/axios.js'; 

import App from './App.vue'

import game from './components/game.vue'
import acceuil from './components/acceuil.vue'
import rules from './components/rules.vue'
import highscore from './components/highscore.vue'

const routes = [
    { path: '/', component: acceuil },
    { path: '/game', component: game },
    { path: '/rules', component: rules },
    { path: '/highscore', component: highscore }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


// Create app
const app = createApp(App);



// Create Vuetify
const vuetify = createVuetify({
  // configuration options
});

// Use router and Vuetify
app.use(axiosPlugin);
app.use(router);
app.use(vuetify);

// Mount app
app.mount('#app');
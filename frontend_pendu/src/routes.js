import game from './components/game.vue'
import acceuil from './components/acceuil.vue'
import rules from './components/rules.vue'
import highscore from './components/highscore.vue'

export default [
    { path: '/', component: acceuil },
    { path: '/game', component: game },
    { path: '/rules', component: rules },
    { path: '/highscore', component: highscore }
]
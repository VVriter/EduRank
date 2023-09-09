import Landing from './components/Landing.vue'
import School from './components/School.vue'

const routes = [
    { path: '/', component: Landing },
    { path: '/school/:id', component: School}
]

export default routes
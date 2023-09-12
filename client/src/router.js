import Landing from './components/Landing.vue'
import School from './components/School.vue'
import NotFound from './components/NotFound.vue'
import Registration from './components/Registration.vue'

const routes = [
    { path: '/', component: Landing },
    { path: '/school/:id', component: School},
    { path: '/404/:message', component: NotFound },
    { path: '/registration', component: Registration }
]

export default routes
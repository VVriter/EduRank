import { createApp } from 'vue'
import '@/assets/style.css'
import App from './App.vue'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import 'element-plus/theme-chalk/dark/css-vars.css'

import { createPinia } from 'pinia'
const pinia = createPinia()

import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes'

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior(to, from, savedPosition) {
        return { top: 0 }
    }
})

import VueGoogleMaps from '@fawmi/vue-google-maps'

createApp(App)
    .use(router)
    .use(ElementPlus)
    .use(pinia)
    .use(VueGoogleMaps, {
        load: {
            key: 'AIzaSyDDy5IUrvL4bVAdeQ_MBvcqsy1rgs5X3V4',
            language: "UA"
        },
    })
    .mount('#app')

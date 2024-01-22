export default [
    {
        name: "Home",
        path: "/",
        component: () => import('@/views/Landing.vue')
    },
    {
        name: "EJournal",
        path: "/projects/eJournal",
        component: () => import('@/views/EJournal.vue')
    },
    {
        name: "Donate",
        path: "/donate",
        component: () => import('@/views/Donate.vue')
    },
    {
        name: "Login",
        path: "/login",
        component: () => import('@/views/Login.vue')
    },
    {
        name: "CheckEmail",
        path: "/email",
        component: () => import('@/views/CheckEmail.vue')
    },
    {
        name: "Verify",
        path: "/verify/:id",
        component: () => import('@/views/Verify.vue')
    },
    {
        name: "School",
        path: "/school/:id",
        component: () => import('@/views/School.vue')
    },
    {
        name: "GPSSearch",
        path: "/search/",
        component: () => import('@/views/GpsSearch.vue')
    },

    {
        name: "NotFound",
        path: "/:pathMatch(.*)*",
        component: () => import('@/views/NotFound.vue')
    }
]
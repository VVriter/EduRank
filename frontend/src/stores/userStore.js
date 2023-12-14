import { defineStore } from 'pinia'

export const useUserStore = defineStore('userStore', {
    state: () => ({
        loginned: localStorage.getItem('token') ? localStorage.getItem('token') : false,
        token: localStorage.getItem('token'),
        profile: null
    }),
    actions: {
        async updateUserInfo() {
            const res = await fetch('/api/me', {
                method: "GET",
                headers: {
                    'token': this.token
                }
            })

            if (res.status != 200) {
                localStorage.removeItem('token')
                return
            }

            this.profile = (await res.json()).user
        }
    }
})

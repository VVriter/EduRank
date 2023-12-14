import { defineStore } from 'pinia'

export const useUiConfigStore = defineStore('useUiConfigStore', {
    state: () => ({
        darkModeName: 'dark',
        isDarkModeOn: localStorage.getItem('isDark') ? JSON.parse(localStorage.getItem('isDark')) : true
    }),
    getters: {
        htmlNode() {
            return document.querySelector("html");
        },
    },
    actions: {
        applyTheme() {
            this.isDarkModeOn
                ? this.htmlNode.classList.add(this.darkModeName)
                : this.htmlNode.classList.remove(this.darkModeName);
        },
    }
})

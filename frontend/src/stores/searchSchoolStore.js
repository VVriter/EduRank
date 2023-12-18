import { defineStore } from 'pinia'

export const useSearchSchoolStore = defineStore('searchSchoolStore', {
    state: () => ({
        input: null,
        recommended: [
            '140971',
            '142195'
        ]
    }),
    actions: {
        async schoolsList() {
            if (!this.input)
                return null
            const respose = await fetch(`/api/search?query=${this.input}`)
            const json = await respose.json()
            return json
        },
        async schoolsListWithLimit(limit) {
            if (!this.input)
                return null
            const respose = await fetch(`/api/search?query=${this.input}&limit=${limit}`)
            const json = await respose.json()
            return json
        },
        async recommendedSchoolsList() {
            const promises = this.recommended.map(async (recommendation) => {
                const response = await fetch(`/api/edbo?query=${recommendation}`);
                const json = await response.json();
                return json;
            });

            const list = await Promise.all(promises);
            return list;
        },
        async getSchoolById(id) {
            const response = await fetch(`/api/edbo?query=${id}`);
            const json = await response.json();
            return json;
        }
    }
})

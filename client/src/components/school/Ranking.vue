<template v-if="loaded">
    <p style="font-size: 30px;">Відгуки на {{data.short_name }}</p>
    {{data}}
</template>

<script>
    import UserManager from '../../util/UserManager'

    export default {
        props: {
            data: {
                required: true
            }
        },
        data() {
            return {
                loaded: null,
                loginned: null
            }
        },
        async mounted() {
            const loginned = UserManager.isLoginned()
            this.loginned = loginned

            this.loaded = true
        }
    }
</script>
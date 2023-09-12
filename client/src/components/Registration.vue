<template>
    <div class="container" v-if="!isAlreadyAuthentificated && data">
        <p>reg</p>
    </div>
</template>

<script>
    export default {
        name: 'Registration',
        data() {
            return {
                isAlreadyAuthentificated: false,
                data: null
            }
        },
        mounted() {
            fetch(`/api/register`, { method: 'GET' })
                .then(response => {
                    if (response.status != 200)
                        throw Error('Iternal server error')
                    return response.json()
                })
                .then(data => this.data = data)
                .catch(error => {
                    console.error('Error fetching data:', error)
                    location.replace(`/404/${error}`)
                })
        }
    }
</script>
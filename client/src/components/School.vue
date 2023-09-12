<template>
    <div>
        
    </div>
</template>

<script>
    export default {
        components: {
            
        },
        data() {
            return {
                id: null,
                data: null,
                notFound: false,
                images: null,
                mapData: null
            }
        },  
        created() {
            this.id = this.$route.params.id

            fetch(`http://127.0.0.1:5000/api/edbo?query=${this.id}`, { method: 'GET' })
                .then(response => response.json())
                .then(data => this.data = data)
                .catch(error => console.error('Error fetching data:', error))

            .then(() => {
                fetch(`http://127.0.0.1:5000/api/images?query=${this.data.short_name}`)
                .then(res => res.json())
                .then(data => this.images = data)
                .catch(error => console.error('Error fetching data:', error))
            })

            .then(() => {
                fetch(`http://127.0.0.1:5000/api/map?query=Україна ${this.data.region_name} ${this.data.koatuu_name} ${this.data.address}`)
                .then(res => res.json())
                .then(data => this.mapData = data)
                .catch(error => console.error('Error fetching data:', error))
            })
        }
    }
</script>

<style>
  @import '@/assets/style/School.css';
</style>
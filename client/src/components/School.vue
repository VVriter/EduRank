<template>
    <div v-if="data" class="main">
        <a href="/" class="a_school_image">
            <img src="@/assets/school.png" alt="" class="school_image">
        </a>
        <p class="title">{{data.institution_name}}</p>

        <div class="main_info">
            <SchoolInfoPlate :data="data" v-if="data"/>
        </div>

        <p class="title">Зображення по запиту "{{data.short_name}}"</p>
        <Galery v-if="images" :data="images"/>
        
    </div>

    <Loading v-if="!data && !notFound"/>
    <NotFound v-if="notFound"/>
</template>

<script>
    import Loading from './sub/Loading.vue';
    import NotFound from './sub/NotFound.vue';
    import Galery from './sub/Galery.vue';
    import Map from './sub/Map.vue';
    import SchoolInfoPlate from './sub/SchoolInfoPlate.vue';


    export default {
        components: {
            Loading,
            NotFound,
            Galery,
            Map,
            SchoolInfoPlate
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
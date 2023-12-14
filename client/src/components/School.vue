<template>
    <div class="content" v-if="data">
        <img src="@/assets/logo.png" alt="" class="logo" @click="replace">
        <p class="school-title">{{ data.institution_name }}</p>
        <SchoolInfoPlate :data="data"/>
        <ReplaceButtons :data="data"/>
        <Ranking :data="data"/>
        <Galery :images="images" :name="data.short_name" v-if="images && data"/>
    </div>

    <SchoolLoadingPlate v-if="!data"/>
</template>

<script>
    import SchoolInfoPlate from './school/SchoolInfoPlate.vue'
    import SchoolLoadingPlate from './landing/SchoolLoadingPlate.vue'
    import ReplaceButtons from './school/ReplaceButtons.vue'
    import Galery from './school/Galery.vue'
    import Ranking from './school/Ranking.vue'

    export default {
        components: {
            SchoolInfoPlate,
            SchoolLoadingPlate,
            ReplaceButtons,
            Galery,
            Ranking
        },
        data() {
            return {
                id: null,
                data: null,
                notFound: false,
                images: null,
                mapData: null,
            }
        },  
        methods: {
            replace() {
                this.$router.push('/')
            }
        },
        created() {
            this.id = this.$route.params.id

            fetch(`/api/edbo?query=${this.id}`, { method: 'GET' })
                .then(response => {
                    if (response.status != 200) 
                        throw new Error('And error ocured, responce code is not 200')
                    return response.json()
                })
                .then(data => this.data = data)
                .catch(error => {
                    console.error('Error fetching data:', error)
                    this.notFound = true
                    location.replace('/404/Школа не знайдена 🙃')
                    return
                })

            .then(() => {
                fetch(`/api/images?query=${this.data.short_name}`)
                .then(res => res.json())
                .then(data => this.images = data)
                .catch(error => console.error('Error fetching data:', error))
            })

            .then(() => {
                fetch(`/api/map?query=Україна ${this.data.region_name} ${this.data.koatuu_name} ${this.data.address}`)
                .then(res => res.json())
                .then(data => this.mapData = data)
                .catch(error => console.error('Error fetching data:', error))
            })

        }
    }
</script>

<style>
    p {
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        font-weight: 900;
    }

    .content {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .logo {
        border-radius: 50%;
        margin-top: 5vh;
        width: 40vh;
    }

    .logo:hover {
        cursor: pointer;
    }

    .school-title {
        font-size: 3vh;
        text-align: center;
        margin-right: 3vh;
        margin-left: 3vh;
        width: 50%;
    }


    @media only screen and (max-width: 1000px) {
        .school-title {
            font-size: 3vh;
            text-align: center;
            margin-right: 3vh;
            margin-left: 3vh;
            width: 90%;
        }
    }

</style>
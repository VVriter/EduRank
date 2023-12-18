<template>
    <main v-if="school">
        <div class="left">
            <SchoolPlate :school="school"/>
            <Map style="width: 100%; margin-top: 10px;" :prompt="school.koatuu_name + ' ' + school.address"/>
        </div> 
        <div class="center">
            <Reviews :school="school"/>
        </div>
        <div class="right">
            <ViewsStatistic/>
            <InformationActualization/>
            <Rating/>
        </div>
    </main>

    <main v-loading v-else style="min-height: 70vh; display: flex; justify-content: center; align-items: center;"></main>
</template>

<style scoped>
    main {
        max-width: 90%;
        min-width: 90%;
        width: 90%;
        margin-top: 10px;
        display: flex;
        flex-direction: row;
        gap: 10px;
        justify-content: center;
        align-items: start;
    }

    .left {
        width: 33%;
    }

    .center {
        width: 57%;
    }

    .right {
        width: 23.3%;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    @media only screen and (max-width: 767px) {
        main {
            flex-direction: column;
        }

        .left {
            width: 100%;
        }

        .right {
            width: 100%;
        }

        .center {
            width: 100%;
        }
    }
</style>

<script setup>

    import Map from '../components/school/Map.vue'

    import SchoolPlate from '@/components/school/SchoolPlate.vue';
    import Reviews from '@/components/school/Reviews.vue';
    import Rating from '@/components/school/Rating.vue';
    import ViewsStatistic from '@/components/school/ViewsStatistic.vue';
    import InformationActualization from '@/components/school/InformationActualization.vue';

    import { useSearchSchoolStore } from '../stores/searchSchoolStore'
    import { ElLoading } from 'element-plus'
    const searchSchoolStore = useSearchSchoolStore()
    import { onMounted, ref } from 'vue'
    import { useRouter, useRoute } from 'vue-router'
    const route = useRoute()
    
    const school = ref()

    onMounted(async () => {

        const loading = ElLoading.service({
            lock: true,
            text: 'Завантаження',
            background: 'rgba(0, 0, 0, 0.0)',
        })

   
        school.value = await searchSchoolStore.getSchoolById(route.params.id)
        loading.close()
      
    })
</script>
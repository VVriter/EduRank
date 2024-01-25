<template>
    <main v-if="school" style="width: 100%; min-height: 55vh; display: flex; justify-content: center; align-items: center;">
        <div style="width: 90%; display: flex; flex-direction: column; gap: 10px;">
            <Map
                style="width: 100%; height: 70vh; border-radius: 15px; border: solid 1px;"
                :prompt="school.koatuu_name + ' ' + school.address"
                :name="school.short_name"
            />

            <el-card shadow="hover" style="border-radius: 10px;">
                <template #header>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center;">
                        <el-button size="large" @click="pageSelected = 'top_reviews'" :type="pageSelected == 'top_reviews' ? 'primary' : ''" style="margin: 0;" round>Топ відгуків</el-button>
                        <el-button size="large" @click="pageSelected = 'rating'" :type="pageSelected == 'rating' ? 'primary' : ''" style="margin: 0;" round>Рейтинг</el-button>
                        <el-button size="large" @click="pageSelected = 'main_info'" :type="pageSelected == 'main_info' ? 'primary' : ''" style="margin: 0;" round>Основна інформація</el-button>
                        <el-button size="large" @click="pageSelected = 'teachers'" :type="pageSelected == 'teachers' ? 'primary' : ''" style="margin: 0;" round>Вчительський колектив</el-button>
                        <el-button size="large" @click="pageSelected = 'photos'" :type="pageSelected == 'photos' ? 'primary' : ''" style="margin: 0;" round>Фотографії</el-button>
                    </div>
                </template>

                <Reviews v-if="pageSelected == 'top_reviews'" :school="school"/>
            </el-card>

            <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                <InformationActualization style="max-width: 360px;"/>
                <ViewStatistic style="max-width: 360px;"/>
                <Rating style="max-width: 360px;"/>
            </div>
        </div>
    </main>

    <main v-loading v-else style="min-height: 70vh; display: flex; justify-content: center; align-items: center;"></main>
</template>

<script setup>

    import Reviews from '@/components/school/Reviews.vue'

    import Map from '@/components/school/Map.vue'
    import InformationActualization from '@/components/school/InformationActualization.vue'
    import ViewStatistic from '@/components/school/ViewsStatistic.vue'
    import Rating from '@/components/school/Rating.vue'

    import { useSearchSchoolStore } from '../stores/searchSchoolStore'
    import { ElLoading } from 'element-plus'
    const searchSchoolStore = useSearchSchoolStore()
    import { onMounted, ref } from 'vue'
    import { useRouter, useRoute } from 'vue-router'
    const route = useRoute()
    
    const school = ref()
    const pageSelected = ref('top_reviews')

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

<style scoped>
    @media (min-width: 769px) {
        main {
            margin-top: 10px;
        }
    }
</style>
<template>
    <div v-if="searchedSchools && searchedSchools.length !== 0 && searchSchoolStore.input != null" class="containager">
        <SearchedSchoolPlate v-for="(school, index) in searchedSchools" :key="index" :school="school"/>
        <el-button type="info" plain v-if="showMoreMayBeShown" :loading="loading" @click="showMore" :icon="ArrowDownBold" style="width: 100%;">Показати більше</el-button>
    </div>

    <div v-else class="containager">
        <SearchedSchoolPlate v-for="(school, index) in recomended" :key="index" :school="school"/>
    </div>

</template>

<style scoped>
 .containager {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    gap: 10px;
    margin-top: 10px;
    max-height: 40vh;
    overflow-y: scroll;
    overflow-x: hidden;
    position: relative;
    padding: 10px;
    background-color: var(--el-color-info-light-8);
    border-radius: 5px;
}

/* width */
.containager::-webkit-scrollbar {
    width: 1px;
    border-radius: 10px;
}

/* Track */
.containager::-webkit-scrollbar-track {
    background: var(--el-color-info-light-9);
    border-radius: 10px;
}

/* Handle */
.containager::-webkit-scrollbar-thumb {
    background: var(--el-color-info);
}

/* Handle on hover */
.containager::-webkit-scrollbar-thumb:hover {
    background: var(--el-color-info);
}
</style>

<script setup>
    import { ArrowDownBold } from '@element-plus/icons-vue'
    import SearchedSchoolPlate from './SearchedSchoolPlate.vue';
    import { ref, onMounted, watch } from 'vue' 
    import { useSearchSchoolStore } from '../../stores/searchSchoolStore';
    const searchSchoolStore = useSearchSchoolStore()    

    const searchedSchools = ref()
    const recomended = ref([])
    const loading = ref(false)
    const limit = ref(0)
    const showMoreMayBeShown = ref(true)

    onMounted(async () => {
        searchedSchools.value = await searchSchoolStore.schoolsList()

        const recomendedSchoolsResponse = await searchSchoolStore.recommendedSchoolsList()
        recomendedSchoolsResponse.forEach(recommendedSchool => recomended.value.push(recommendedSchool))
    })

    watch(() => searchSchoolStore.input, 
    async (newValue, oldValue) => {
        showMoreMayBeShown.value = true
        limit.value = 0
        searchedSchools.value = await searchSchoolStore.schoolsList()
    })

    async function showMore() {
        limit.value += 10
        loading.value  = true
        const schools = await searchSchoolStore.schoolsListWithLimit(limit.value)
        if (schools.length <= (limit.value + 10))
            showMoreMayBeShown.value = false
        searchedSchools.value = schools
        loading.value = false
    }
</script>
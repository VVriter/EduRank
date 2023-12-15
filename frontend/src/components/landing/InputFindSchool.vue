<template>
    <div class="container">
        <el-input v-model="searchSchoolStore.input" placeholder="Введіть назву школи..." size="large">
            <template #prepend>
                <el-button :icon="Search" />
            </template>
          <!--  <template #append>
                <el-button :icon="Promotion" />
            </template>-->
        </el-input>
        <!--<el-button :icon="Filter" size="large" plain type="info">

        </el-button>-->
    </div>
</template>

<script setup>
    import { Search, Promotion, Filter } from '@element-plus/icons-vue'
    import { useSearchSchoolStore } from '../../stores/searchSchoolStore';
    const searchSchoolStore = useSearchSchoolStore()
</script>

<style scoped>
    .container {
        width: 100%;
        margin-top: 10px;
        display: flex;
        flex-direction: row;
        gap: 10px;
    }
</style>
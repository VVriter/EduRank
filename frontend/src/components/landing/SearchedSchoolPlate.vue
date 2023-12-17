<template>
    <el-card @click="$router.push(`/school/${school.institution_id}`)" body-style="min-height: fit-content;" shadow="hover" class="card">
        <template #header>
            <el-row>
                <el-text v-if="school.short_name" style="font-size: 20px; width: 80%;">{{ school.short_name }}</el-text>
                <el-text v-if="school.institution_name && !school.short_name" style="font-size: 20px; width: 80%;">{{ school.institution_name }}</el-text>
                
                <el-icon style="margin-left: auto;" size="30px">
                    <School/>
                </el-icon>
            </el-row>
        </template>

        <el-text type="info" style="margin-bottom: 20px;">{{school.institution_name}}</el-text>
    
        <el-row style="gap: 10px; margin-top: 10px;">
            <el-tag round size="large">Відчинено</el-tag>
            <el-tag round size="large">{{ school.phone }}</el-tag>
        </el-row>
        <el-tag round :icon="Position" style="margin-top: 10px;" type="success" size="large">{{ school.address }}</el-tag>
    </el-card>
</template>

<script setup>
    import { School, Position } from '@element-plus/icons-vue'
    const props = defineProps({
        school: { required: true }
    })
</script>

<style scoped>

.card {
    width: 100%;
    cursor: pointer;
    border-radius: 10px;
    min-height: 250px;
}

@media only screen and (max-width: 767px) {
    .card {
        min-height: 300px;
    }
}
</style>
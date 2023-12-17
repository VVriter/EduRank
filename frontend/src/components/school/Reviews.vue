<template>
    <el-menu
    class="menu"
    mode="horizontal"
    :default-active="menu"
    @select="handleSelect"
    >
        <el-menu-item index="0">Всі</el-menu-item>
        <el-menu-item index="1">Учнів</el-menu-item>
        <el-menu-item index="2">Батьків</el-menu-item>
        <el-menu-item index="3">Вчителів</el-menu-item>
        <el-menu-item index="4">Анонімні</el-menu-item>
    </el-menu>
    

    <div>
        <el-button :icon="icon" size="large" plain type="primary" @click="isReviewAdd = !isReviewAdd" style="margin-top: 10px; width: 100%;">Додати відгук</el-button>

        <div v-if="isReviewAdd">
            <LeaveReviews v-if="userStore.loginned && menu != 4" style="margin-top: 10px;" :school="props.school"/>
            <NotLoginned :action="() => { menu = 4 }" v-if="!userStore.loginned && menu != 4"/>
            <AnnonReview :school="props.school" v-if="menu == 4"/>
        </div>
    </div>

</template>

<script setup>
    import LeaveReviews from './LeaveReviews.vue';
    import NotLoginned from './NotLoginned.vue';
    import AnnonReview from './AnnonReview.vue';

    import {ArrowDownBold, ArrowUpBold} from '@element-plus/icons-vue'

    import { useUserStore } from '../../stores/userStore'
    const userStore = useUserStore()

    import { ref, computed } from 'vue'

    const isReviewAdd = ref(false)

    const icon = computed(() => {
        return isReviewAdd.value ? ArrowUpBold : ArrowDownBold
    })

    const menu = ref('0')

    const handleSelect = (key, keyPath) => {
        menu.value = `${key}`
    }

    const props = defineProps({
        school: { required: true }
    })
</script>

<style scoped>
    .menu {
        justify-content: center;
    }
</style>
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


    <div style="background-color: var(--el-color-primary-light-7); border-radius: 10px; padding: 10px; max-height: 500px; margin-top: 10px; display: flex; flex-direction: column; gap: 10px;">
        <div style="width: 100%; display: flex; align-items: center; justify-content: center; flex-direction: column;">
            <el-card style="width: 100%; border-radius: 10px;">
                <div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                    <el-text>Середнє значення</el-text>
                    <el-rate disabled show-score size="large" v-model="midleValueOfRank" clearable />
                </div>
            </el-card>
        </div>
        <div style="overflow-y: scroll; overflow-x: hidden; gap: 10px; display: flex; flex-direction: column;">
            <div v-for="(item, index) in filteredReviews" :key="index">
                <el-card shadow="hover" style="border-radius: 10px;" v-if="item.user">
                    <el-row style="margin-bottom: 10px; display: flex;">
                        <el-icon size="35px"><UserFilled/></el-icon>
                        <el-text type="info" size="large" style="margin-left: 5px;">{{ item.user.name }}</el-text>
                        <el-text type="info" size="large" style="margin-left: 10px;">{{ item.user.surname }}</el-text>
                        <el-rate disabled show-score size="large" style="margin-left: auto;" v-model="item.review.rate" clearable />
                    </el-row>

                    <el-text style="margin-top: 20px;">{{ item.review.description }}</el-text>
                    <hr style="border: none; height:1px; background-color: white; margin-top: 10px; margin-bottom: 10px;">
                    <el-text type="info">{{ item.time }} | {{ item.user.email }} | {{ item.review.rate }}</el-text>
                </el-card>

                <el-card shadow="hover" style="border-radius: 10px;" v-else>
                    <el-row style="margin-bottom: 10px; display: flex;">
                            <el-icon size="35px"><UserFilled/></el-icon>
                            <el-text type="info" size="large" style="margin-left: 5px;">Анонімний користувач</el-text>
                            <el-rate disabled show-score size="large" style="margin-left: auto;" v-model="item.review.rate" clearable />
                        </el-row>

                        <el-text style="margin-top: 20px;">{{ item.review.description }}</el-text>
                        <hr style="border: none; height:1px; background-color: white; margin-top: 10px; margin-bottom: 10px;">
                        <el-text type="info">{{ item.time }} | {{ item.review.rate }}</el-text>
                </el-card>
            </div>
        </div>
    </div>


      <div style="padding: 10px; margin-top: 10px; background-color: var(--el-color-primary-light-8); border-radius: 10px;" v-if="userStore.profile && !userStore.profile.reviews.includes(school.institution_id)">
            <el-button :icon="icon" size="large" plain type="primary" @click="isReviewAdd = !isReviewAdd" style="width: 100%;">Додати відгук</el-button>

            <div v-if="isReviewAdd">
                <LeaveReviews v-if="userStore.loginned && menu != 4" style="margin-top: 10px;" :school="props.school"/>
                <NotLoginned :action="() => { menu = 4 }" v-if="!userStore.loginned && menu != 4"/>
                <AnnonReview :school="props.school" v-if="menu == 4"/>
            </div>
        </div>

        <div style="padding: 10px; margin-top: 10px; background-color: var(--el-color-primary-light-8); border-radius: 10px;" v-if="!userStore.profile">
            <el-button :icon="icon" size="large" plain type="primary" @click="isReviewAdd = !isReviewAdd" style="width: 100%;">Додати відгук</el-button>

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

    import {Minus, Plus, UserFilled} from '@element-plus/icons-vue'

    import { useUserStore } from '../../stores/userStore'
    const userStore = useUserStore()

    import { ref, computed, onMounted } from 'vue'

    const isReviewAdd = ref(true)

    const icon = computed(() => {
        return isReviewAdd.value ? Minus : Plus
    })

    const menu = ref('0')

    const handleSelect = (key, keyPath) => {
        menu.value = `${key}`
    }

    const props = defineProps({
        school: { required: true }
    })

    const reviews = ref([])

    onMounted(async () => {
        const res = await fetch(`/api/reviews?edbo=${props.school.institution_id}`)
        const json = await res.json()
        const reviewses = json.reviews
        reviewses.forEach(element => {
            const rev = JSON.parse(element)
            reviews.value.push(rev)
        });

        console.log(reviews.value)
    })

    const filteredReviews = computed(() => {
        if (menu.value == '0') {
            return reviews.value
        } else if (menu.value == '1') {
            return reviews.value.filter(review => review.user).filter(review => review.user.userType == 'pupil')
        } else if (menu.value == '2') {
            return reviews.value.filter(review => review.user).filter(review => review.user.userType == 'parrent')
        } else if (menu.value == '3') {
            return reviews.value.filter(review => review.user).filter(review => review.user.userType == 'teacher')
        } else if (menu.value == '4') {
            return reviews.value.filter(review => !review.user)
        } else {
            return []
        }
    })

    const midleValueOfRank = computed(() => {
        if (reviews.value.length === 0) {
            return '5'; // Default value if there are no reviews
        }

        let allValuesInc = 0;
        for (const review of reviews.value) {
            allValuesInc += review.review.rate;
        }

        const average = allValuesInc / reviews.value.length;
        if (isNaN(average)) {
            return '5'; // Return default value if average is NaN
        } else {
            const strValue = average.toFixed(2); // Fix the average to two decimal places
            return strValue.slice(0, 3); // Return the first three characters of the string representation of the average
        }
    });

</script>

<style scoped>
    .menu {
        justify-content: center;
        margin: auto;
        background-color: var(--el-color-primary-light-9);
        margin-top: 10px;
        border-radius: 10px;
    }
</style>
<template>
    <el-card style="margin-top: 10px;">
        <template #header>
            <div style="display: flex; flex-direction: row;">
                <el-text>Залиште відгук на цю установу!</el-text>
                <el-icon style="margin-left: auto;" size="20px">
                    <Star />
                </el-icon>
            </div>
        </template>

        <div style="display: flex; flex-direction: column; gap: 10px;" v-if="state == 1">
            <el-input v-model="name" placeholder="Ім'я (опціонально)"/>
            <el-input v-model="age" type="number" placeholder="Вік (опціонально)"/>
            <el-input v-model="description" type="textarea" :rows="5" size="large" placeholder="Опишіть ваші враження" />
            <el-button :disabled="!description" @click="state++" :icon="ArrowRightBold" size="large">Наступний
                етап</el-button>
        </div>

        <div style="display: flex; flex-direction: column; gap: 10px; justify-content: center; align-items: center;"
            v-if="state == 2">
            <el-text style="font-size: 20px; text-align: center;">Поставте зірочки, від меншого до більшого, від поганого до
                хорошого.</el-text>
            <el-rate size="large" v-model="rate" allow-half />
            <el-button :disabled="!rate" @click="sendReview" :icon="ArrowRightBold" size="large">Наступний етап</el-button>
        </div>

        <div style="display: flex; flex-direction: column; gap: 10px; justify-content: center; align-items: center;"
            v-if="state == 3">
            <img style="width: 200px;" src="@/assets/img/trophy.png" alt="">
            <el-text style="font-size: 20px; text-align: center;">Ваш відгук записано! Дякую, що сприяєте розвитку
            демократії в нашій країні :). Приблизно за годину ваш відгук з'явиться на сайті.</el-text>
        </div>
    </el-card>
</template>

<script setup>

    import { Star, ArrowRightBold } from '@element-plus/icons-vue'

    import { ref } from 'vue'
    const description = ref()
    const state = ref(1)
    const rate = ref()
    const name = ref()
    const age = ref()

    async function sendReview() {
        state.value++
    }

    const props = defineProps({
        school: { required: true }
    })
</script>
<template>
    <main style="display: flex; justify-content: center; align-items: center; height: 80vh;">
        <el-card style="width: 400px;" v-if="isSuccess === true">
            <template #header>
                <el-row>
                    <el-text style="font-size: 20px;">Успішний вхід в систему</el-text>
                    <el-icon style="margin-left: auto;" size="30px">
                        <Check/>
                    </el-icon>
                </el-row>
            </template>

            <el-text type="info">Дякую, що вибрали нас! Обіцяємо вам найприємніші враження від використання нашого додатку.</el-text>
            <el-row style="margin-top: 10px;">
                <el-button @click="toMain" :icon="Trophy" plain size="large" type="warning">Оцінити школу!</el-button>
                <el-button @click="toMain" size="large" type="success" plain :icon="HomeFilled">Додому</el-button>
            </el-row>
        </el-card>

        <el-card v-if="isSuccess === false" style="width: 400px;">
            <template #header>
                <el-row>
                    <el-text style="font-size: 20px;">Щось пішло не так</el-text>
                    <el-icon style="margin-left: auto;" size="30px">
                        <Close/>
                    </el-icon>
                </el-row>
            </template>

            <el-text type="info">Під час входу щось пішло не так, спробуйте ще раз будьласка!</el-text>
        </el-card>
    </main>
</template>

<script setup>
    import { Check, Trophy, HomeFilled, Close } from '@element-plus/icons-vue'
    import { useRouter, useRoute } from 'vue-router'
    import { onMounted, ref } from 'vue'
    import { useUserStore } from '../stores/userStore'
    const userStore = useUserStore()
    const router = useRouter()
    const route = useRoute()
    const id = route.params.id

    const isSuccess = ref()

    function toMain() {
        location.replace('/')
    }

    onMounted(async () => {
        const response = await fetch(`/api/verify?id=${id}`, { method: "POST" })

        if (response.status == 200) {
            isSuccess.value = true
        } else {
            isSuccess.value = false
            return
        }

        const json = await response.json()
        localStorage.setItem('token', json.token)
        userStore.updateUserInfo()
    })
</script>
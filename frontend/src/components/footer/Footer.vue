<template>
    <el-card class="card">
        <div class="con">
            <div style="display: flex; flex-direction: column;">
                <el-text style="font-size: 40px;">EDURANK</el-text>
                <el-text style="font-size: 23px;">Разом з кожним</el-text>
                <el-button @click="$router.push('/donate')" style="margin-top: 10px;">Підтримати сервіс</el-button>
            </div>
            <div style="display: flex; flex-direction: column;">
                <el-text style="font-size: 20px; text-align: start; width: 100%;">Документи</el-text>

                <el-text style="margin-top: 20px; text-align: start; width: 100%;">Політика конфіденційності</el-text>
                <el-text style="text-align: start; width: 100%;">Користувацьке згодження</el-text>
                <el-text style="text-align: start; width: 100%;">Офферта</el-text>
            </div>
            <div style="display: flex; flex-direction: column;">
                <el-text style="font-size: 20px; text-align: start; width: 100%;">Суб-проєкти</el-text>

                <el-text style="margin-top: 20px; text-align: start; width: 100%;">Є-Журнал</el-text>
                <el-text style="text-align: start; width: 100%;">Є-Розклад</el-text>
                <el-text style="text-align: start; width: 100%;">Є-Підручник</el-text>
            </div>

            <div class="news">
                <el-text style="font-size: 24px;">Підписатись на новини</el-text>
                <el-input v-model="input" placeholder="Електронна пошта"/>
                <el-button :disabled="!input" style="margin-top: 5px;">Підписатись!</el-button>
            </div>
        </div>
    </el-card>
</template>

<script setup>
    import { ref } from 'vue'
    const input = ref()
</script>

<style scoped>
    .card {
        margin-top: 10px;
        border-radius: 10px 10px 0 0;
    }

    .con {
        gap: 100px;display: flex; flex-direction: row; justify-content: center; align-items: center;
    }

    .news {
        margin-left: auto; display: flex; flex-direction: column; margin-right: 100px;
    }

    @media only screen and (max-width: 1000px) {
        .con {
            flex-direction: column;
            margin-bottom: 100px;
            gap: 50px;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        .news {
            margin: 0;
        }
    }
</style>
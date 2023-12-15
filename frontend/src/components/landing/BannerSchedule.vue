<template>
    <el-card class="container">
        <el-icon style="position: absolute; opacity: 50%;margin-left: 33%; margin-top: 23%;" size="100px">
            <Lock/>
        </el-icon>
        <div class="wrapper">
            <div class="right">
                <el-text style="font-size: 28px; text-align: start; width: 100%;">Є-Розклад</el-text>
                <el-text type="info" style="font-size: 15px; margin-top: 20px;">Рішення для учнів та студентів, складай розклади для любих подій та уроків!</el-text>
                <el-button disabled size="large" style="margin-top: 20px;">Створити розклад!</el-button>
            </div>
            <div class="left">
                <img src="@/assets/img/note.png" alt="">
            </div>
        </div>
    </el-card>
</template>

<script setup>
    import { Lock } from '@element-plus/icons-vue'
</script>

<style scoped>
    .container {
        cursor: not-allowed;
        width: 100%;
        border-radius: 10px;
        display: flex;
        position: relative;
    }

    .right {
        display: flex;
        flex-direction: column;
        width: 60%;
    }

    .left {
        width: 20%;
    }

    .wrapper {
        display: flex;
        flex-direction: row;
        opacity: 20%;
    }

    @media only screen and (max-width: 767px) {
    }
</style>
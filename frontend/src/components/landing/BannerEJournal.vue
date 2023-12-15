<template>
    <el-card class="container">
        <div class="wrapper">
            <div class="right">
                <el-text style="font-size: 28px; text-align: start; width: 100%;">Є-Журнал</el-text>
                <el-text type="info" style="font-size: 15px; margin-top: 20px;">Найкраще, безкоштовне рішення серед конкурентів. Виберіть наш журнал та переглядайте оцінки своїх дітей в будь-який час!</el-text>
                <el-button @click="$router.push('/projects/eJournal')" size="large" style="margin-top: auto;">Використати!</el-button>
            </div>
            <div class="left">
                <img class="img" src="@/assets/img/alarm.png" alt="">
            </div>
        </div>
    </el-card>
</template>

<style scoped>
.container {
    width: 100%;
    border-radius: 10px;
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
}

.img {
    translate: -50px;
}

@media only screen and (max-width: 767px) {}
</style>
<template>
    <el-card class="container">
        <div class="wrapper">
            <div class="right">
                <el-text style="font-size: 28px;">Є-Журнал</el-text>
                <el-text type="info" style="font-size: 15px; margin-top: 20px;">
    Учні та їх батьки можуть використовувати цей журнал для перегляду оцінок та отримання сповіщень від вчителів. Це єлектронний журнал для контролю за оцінками, відвідуваністю та отриманням повідомлень від учителів.</el-text>
                <el-button size="large" style="margin-top: 10px;">Використати!</el-button>
            </div>
            <div class="left">
                <img src="@/assets/img/alarm.png" alt="">
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
    width: 50%;
}

.wrapper {
    display: flex;
    flex-direction: row;
}

@media only screen and (max-width: 767px) {}
</style>
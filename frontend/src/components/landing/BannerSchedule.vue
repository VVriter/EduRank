<template>
    <el-card class="container">
        <div class="wrapper">
            <div class="right">
                <el-text style="font-size: 28px;">Є-Розклад</el-text>
                <el-text type="info" style="font-size: 15px; margin-top: 20px;">Давайте створимо особистий графік з уроками, лекціями та важливими дедлайнами для завдань. Отримання повідомлень і нагадувань допоможе бути в курсі майбутніх подій.</el-text>
                <el-button size="large" style="margin-top: 10px;">Створити розклад!</el-button>
            </div>
            <div class="left">
                <img src="@/assets/img/note.png" alt="">
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

    @media only screen and (max-width: 767px) {
    }
</style>
<template>
    <div class="banner">
        <div style="border: solid; border-radius: 10px; padding: 20px; display: flex; flex-direction: column; justify-content: start; align-items: start; text-align: start;">
            <el-text style="font-size: 30px; font-weight: 800;">ЗНАЙТИ ЗАКЛАД</el-text>
            <el-text style="font-size: 40px; font-weight: 800; width: fit-content; text-align: start; margin-right: auto;">ЦЕ ЛЕГКО!</el-text>
        </div>
    </div>
</template>

<style scoped>
    .banner {
        width: 100%;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-image: url(@/assets/img/banner_background.png);
        border-radius: 10px;
        background-repeat: no-repeat;
        background-size: cover;
    }

    @media only screen and (max-width: 767px) {
        .banner {
            margin-top: 10px;
        }
    }
</style>
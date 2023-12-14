<template>
    <el-card class="container">
        <div class="wrapper">
            <div class="left">
                <el-text style="font-size: 36px; font-weight: 300;">EduRank - ваша дитина буде у безпеці.</el-text>
                <el-text style="margin-top: 30px; font-size: 16px;" type="info">Вчителі, які порушують права людини, погана якість освіти, не відповідні умови навчання - все це вирішує наш сервіс.</el-text>
                <el-text style="margin-top: 30px; font-size: 16px;" type="info">Свобода слова виходить на новий рівень, роблячи відомими недоліки навчальних закладів і таким чином борючись з численними порушеннями. На сторінці школи все, що потрібно відзначити, може бути як зауваженнями, так і позитивними відгуками.</el-text>
                <el-text style="margin-top: 30px; font-size: 20px; font-weight: 300;">Це допоможе батькам обрати навчальний заклад для своєї дитини.</el-text>
            </div>
            <div class="right">
                <img class="img" src="@/assets/img/search mobile.png" alt="">
            </div>
        </div>
    </el-card>
</template>

<style scoped>
    .container {
        width: 100%;
        display: flex;
        flex-direction: row;
        border-radius: 10px;
    }

    .left {
        width: 50%;
        display: flex;
        flex-direction: column;
    }

    .right {
        display: flex;
        width: 50%;
    }

    .wrapper {
        display: flex;
        flex-direction: row;
    }

    @media only screen and (max-width: 767px) {

        .container {
            margin-top: 10px;
        }
        .wrapper {
            flex-direction: column;
        }

        .right {
            width: 100%;
        }

        .left {
            width: 90%;
        }

        .img {
            translate: -50px;
        }
    }
</style>
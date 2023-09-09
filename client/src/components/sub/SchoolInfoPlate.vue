<template>
    <div class="school_info">

        <div class="info_title">
            <p>Інформація про навчальний заклад</p>
        </div>

        <div class="info_box">
            <p class="sub_title">Скорочена назва: </p>
            <p class="main_title">{{data.short_name}}</p>
        </div>
        <div class="info_box">
            <p class="sub_title">Регіон: </p>
            <p class="main_title">{{data.region_name}}</p>
        </div>
        <div class="info_box">
            <p class="sub_title">Адресса: </p>
            <p class="main_title">{{data.address}}</p>
        </div>
        <div class="info_box">
            <p class="sub_title">Населений пункт: </p>
            <p class="main_title">{{data.koatuu_name}}</p>
        </div>
        <div class="info_box">
            <p class="sub_title">Телефон адміністрації: </p>
            <p class="main_title">{{data.phone}}</p>
        </div>
        <div class="info_box">
            <p class="sub_title">Електронна пошта: </p>
            <p class="main_title">{{data.email}}</p>
        </div>
        <div class="info_box" v-if="data.website">
            <p class="sub_title">Вебсайт: </p>
            <p class="main_title">{{data.website}}</p>
        </div>
        <div class="info_box">
            <p class="sub_title">Управління: </p>
            <p class="main_title">{{data.boss}}</p>
        </div>
        <div class="info_box" v-if="data.approved_count">
            <p class="sub_title">Кол-во учнів: </p>
            <p class="main_title">{{data.approved_count}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SchoolInfoPlate",
        props: {
            data: {
                required: true
            }
        }
    }
</script>

<style scoped>
    .school_info {
        width: 50%;
        height: fit-content;
        border-radius: 1vh;
        background: linear-gradient(to bottom, #74324c, #55118d);
        margin-left: 1vh;
        margin-right: 1vh;
        display: flex;
        flex-direction: column;
    }

    .info_title {
        border-radius: 1vh;
        margin: 1vh;
        background: linear-gradient(to bottom, #0466c2, #6b5b95);
        width: 96%;
    }

    .info_title {
        color: white;
        text-align: center;
        font-size: 2vh;
    }

    .info_box {
        display: flex;
        flex-direction: row;
    }

    .main_title {
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        color: white;
        font-size: 1.6vh;
        margin-left: 1vh;
    }

    .sub_title {
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        color: rgba(255, 255, 255, 0.726);
        font-size: 1.6vh;
        margin-left: 1vh;
    }

    .info_box p {
        margin-left: 1vh;
        margin-right: 1vh;
        margin-top: 0.5vh;
        margin-bottom: 0.5vh;
    }
</style>

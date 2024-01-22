<template>
    <div :style="{'background-image': !uiConfigStore.isDarkModeOn ? 'url(banner_background.png)' : 'url(map-dark.png)'}" class="banner">
        <div style="padding: 20px; display: flex; flex-direction: column; justify-content: start; align-items: start; text-align: start;">
            <el-text style="font-size: 25px; font-weight: 800;">ЗНАЙТИ <el-text type="success" style="font-size: 25px; font-weight: 800;">НАВЧАЛЬНИЙ</el-text> ЗАКЛАД</el-text>
            <el-text style="font-size: 40px; font-weight: 800; width: fit-content; text-align: start; margin-right: auto;">ЦЕ ЛЕГКО!</el-text>
        </div>
    </div>
</template>

<script setup>
    import { useUiConfigStore } from '@/stores/uiThemeStore';
    const uiConfigStore = useUiConfigStore()
</script>

<style scoped>
    .banner {
        width: 100%;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-repeat: no-repeat;
        background-size: cover;
        border: solid;
        border-radius: 10px;
        border-width: 1px;
    }

    @media only screen and (max-width: 767px) {
        .banner {
            margin-top: 10px;
        }
    }
</style>
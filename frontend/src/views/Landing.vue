<template>
    <main>
        <div class="containage">
            <div class="left">
                <BannerYourChildIsSecured/>
                <div class="sub-projects-wrapper">
                    <BannerSchedule class="banner-schedule"/>
                    <BannerEJournal class="banner-eJournal"/>
                </div>
            </div>
            <div class="right">
                <BannerFindSchool/>
                <InputFindSchool/>
                <SearchResult/>
            </div>
        </div>
    </main>
</template>

<script setup>
    import BannerFindSchool from '@/components/landing/BannerFindSchool.vue';
    import BannerYourChildIsSecured from '@/components/landing/BannerYourChildIsSecured.vue';
    import BannerSchedule from '@/components/landing/BannerSchedule.vue';
    import BannerEJournal from '@/components/landing/BannerEJournal.vue';
    import InputFindSchool from '@/components/landing/InputFindSchool.vue';
    import SearchResult from '@/components/landing/SearchResult.vue';
</script>

<style scoped>
    main {
        width: 90%;
        display: flex;
        flex-direction: row;
        gap: 10px;
    }

    .containage {
        width: 100%;
        display: flex;
        gap: 10px;
        flex-direction: row;
    }

    .right {
        width: 40%;
        display: flex;
        flex-direction: column;
    }

    .left {
        width: 60%;
        display: flex;
        flex-direction: column;
        height: 100%;
        align-items: start;
    }

    .sub-projects-wrapper {
        margin-top: 10px;
        width: 100%;
        display: flex;
        flex-direction: row;
        gap: 10px;
    }

    @media only screen and (max-width: 767px) {
        main {
            flex-direction: column-reverse;
            margin-bottom: 100px;
        }

        .containage {
            flex-direction: column-reverse;
        }

        .sub-projects-wrapper {
            flex-direction: column;
        }

        .right {
            width: 100%;
        }

        .left {
            width: 100%;
        }
    }
</style>
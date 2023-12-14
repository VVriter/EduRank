<template>
    <main>
        <div class="banner_holder">
            <Banner class="banner"/>
        </div>
    </main>
</template>

<script setup>
    import Banner from '@/components/landing/Banner.vue';
</script>

<style scoped>
    main {
        width: 90%;
    }

    .banner_holder {
        display: flex;
        flex-direction: row;
        width: 100%;
    }

    .banner {
        width: 50%;
    }

    @media only screen and (max-width: 767px) {
        .banner_holder {
            flex-direction: column;
        }
        .banner {
            margin-top: 10px;
            width: 100%;
        }
    }
</style>
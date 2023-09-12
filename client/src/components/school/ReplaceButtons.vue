<template>
    <div class="replace-buttons" v-if="data">
        <a :href="data.website" v-if="data.website" class="button-link">
            <div class="button-icon">
                <p>🌐</p>
            </div>
            <p class="button-label">Сайи</p>
        </a>
        <a :href="'tel:' + data.phone" v-if="data.phone" class="button-link">
            <div class="button-icon">
                <p>📞</p>
            </div>
            <p class="button-label">Звінок</p>
        </a>
        <a :href="'mailto:' + data.email" v-if="data.email" class="button-link">
            <div class="button-icon">
                <p>💬</p>
            </div>
            <p class="button-label">Пошта</p>
        </a>
        <a :href="'https://www.google.com.ua/maps/search/' + data.koatuu_name + data.address" v-if="data.address" class="button-link">
            <div class="button-icon">
                <p>📍</p>
            </div>
            <p class="button-label">Карта</p>
        </a>
    </div>
</template>

<script>
    export default {
        name: 'ReplaceButtons',
        props: {
            data: {
                required: true
            }
        }
    }
</script>

<style scoped>
    .replace-buttons {
        display: flex;
        flex-direction: row;
        margin-top: 1vh;
    }

    .button-link {
        text-decoration: none;
        margin-left: 1rem;
        margin-right: 1rem;
        text-align: center;
        transition: transform 0.2s, background-color 0.2s;
    }

    .button-link:hover {
        transform: translateY(-3px);
    }

    .button-icon {
        font-size: 3.5vh;
        border-radius: 1vh;
        background: linear-gradient(to right, #0466c263, #6b5b95);
        color: white;
        width: 6vh;
        height: 6vh;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 0.5vh;
        transition: background-color 0.2s;
    }

    .button-icon p {
        margin: 0;
    }

    .button-label {
        font-size: 1rem;
        margin-top: 0.5rem;
        color: black;
    }
</style>

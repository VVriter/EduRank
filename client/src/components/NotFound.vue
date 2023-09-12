<template>
    <div class="content">
        <img src="@/assets/404.webp" alt="" class="fourzerofour" @click="replace">
        <div class="message_box" v-if="message" @click="replace">
            <p v-if="message" @click="replace">{{ message }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'NotFound',
        methods: {
            replace() {
                location.replace('/')
            }
        },
        data() {
            return {
                message: null
            }
        },
        created() {
            this.message = this.$route.params.message
        }
    }
</script>

<style scoped>
    .content {
        display: flex;
        flex-direction: column;
        margin: 0;
        height: 100vh;
        margin-left: auto;
        margin-right: auto;
        align-items: center;
        align-content: center;
    }

    .fourzerofour {
        margin-top: 20vh;
        width: 60vh;
        margin-left: auto;
        margin-right: auto;
        animation: bounce 1.3s infinite alternate;
    }

    .fourzerofour:hover {
        cursor: pointer; /* Change cursor to pointer for better UX */
    }
    .content p {
        color: white;
        font-size: 4vh;
        font-weight: 200;
        text-align: center;
        margin: 1vh;
    }

    @keyframes bounce {
        0% {
            transform: translateY(15);
        }
        100% {
            transform: translateY(-5px); /* Измените это значение для желаемой высоты подъема */
        }
    }

    .message_box {
        margin-left: auto;
        margin-right: auto;
        width: fit-content;
        background: linear-gradient(to bottom, #0466c2, #6b5b95);
        border-radius: 1vh;
    }

    .message_box:hover {
        cursor: pointer; /* Change cursor to pointer for better UX */
    }
</style>
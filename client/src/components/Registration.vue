<template>
    <div class="content" v-if="loaded">
        <img src="@/assets/logo.png" alt="" class="logo" @click="toMain">
        <p class="title">Вхід</p>
        <div class="box">
            <div class="btns">

                <button class="google" @click="loginViaGoogle">
                    <img src="@/assets/google.png" alt="">
                    <span>Ввійти через google</span>
                </button>

                <button class="fb">
                    <img src="@/assets/fb.webp" alt="">
                    <span>Ввійти через facebook</span>
                </button>

                <button class="tg" @click="loginViaTg">
                    <img src="@/assets/tg.webp" alt="">
                    <span>Ввійти через telegram</span>
                </button>
                
                <button class="fb">
                    <img src="@/assets/ds.png" alt="">
                    <span>Ввійти через discord</span>
                </button>

            </div>
        </div>
    </div>
</template>

<style scoped>

    .title {
        margin: 0;
        margin-top: 3vh;
        font-size: 3vh;
        letter-spacing: 1vh;
        font-weight: 800;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        width: fit-content;
    }
    .logo:hover {
        cursor: pointer;
    }
    .box {
        margin-top: 3vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        align-content: center;
        width: 40vh;
        background-color: rgb(238, 232, 232);
        border-radius: 1vh;
        box-shadow:
            inset 0 -3em 3em rgba(0, 0, 0, 0.1),
            0 0 0 2px rgb(255, 255, 255),
            0.3em 0.3em 1em rgba(0, 0, 0, 0.3);
    }

    .btns {
        display: flex;
        flex-direction: column;
        margin-top: 1vh;
        margin-bottom: 1vh;
        width: 100%;
        align-items: center;
    }

    .box button {
        margin: 0.5vh;
        width: 90%;
        display: flex;
        flex-direction: row;
        height: 4vh;
        border-radius: 0.5vh;
        margin-left: 1vh;
        margin-right: 1vh;
        user-select: none;
    }

    .box button img {
        width: 3vh;
        margin-top: auto;
        margin-bottom: auto;
    }

    .box button span {
        margin: 0;
        margin-top: auto;
        margin-bottom: auto;
        font-size: 2vh;
        margin-left: 1vh;
    }

    .box button:hover {
        cursor: pointer;
    }

    .google {
        background-color: white;
    }

    .fb {
        background-color: cornflowerblue;
        color: white;
    }

    .tg {
        background-color: white;
    }
</style>

<script>
    import { googleSdkLoaded } from "vue3-google-login";

    export default {
        name: "RegistrationPage",
        data() {
            return {
                loaded: false,
                logined: null,
                tgAppended: false
            }
        },  
        async mounted() {
            const res = await fetch('/api/me')
            const json = await res.json()
            if (json.success) this.loaded = true
            if (json.logined) this.logined = true
            else this.logined = false

            if (this.logined) this.toMain()
        },
        methods: {
            toMain() {
                location.replace('/')
            },

            loginViaTg() {
                fetch('/api/credentials/tg', { method: "GET" })
                    .then(data => data.json())
                    .then(json => {
                        const botName = json.username;
                        const url = json.url;
                        const botId = json.bot_id

                        if (this.tgAppended) {
                            Telegram.Login.auth({
                                bot_id: botId
                            })
                            return
                        }

                        const script = document.createElement('script')
                        script.async = true
                        script.src = 'https://telegram.org/js/telegram-widget.js?22'
                        script.setAttribute('data-telegram-login', botName)
                        script.setAttribute('data-size', 'large')
                        script.setAttribute('data-auth-url', `${url}tg`)
                        script.setAttribute('data-request-access', 'write')
                        document.head.appendChild(script)
                        this.tgAppended = true

                        script.onload = function () {
                            Telegram.Login.auth({ 
                                bot_id: botId 
                            })
                        }
                    })
            },

            loginViaGoogle() {
                fetch('/api/credentials/google', {method: "GET"}).then(res => res.json())
                    .then(json => {
                        googleSdkLoaded(google => {
                            google.accounts.oauth2.initCodeClient({
                                client_id: json.id,
                                scope: "email profile openid",
                                redirect_uri: `https://google.com`,
                                callback: responce => {
                                    if (responce.code) {
                                        fetch('/api/login/google').then(res => res.json())
                                            .then(json => {
                                                if (json.success) 
                                                    console.log('EZZZZZZ', JSON.stringify(responce))
                                            })
                                    }
                                }
                            }).requestCode()
                        })
                    })
            }

        }
    }
</script>   
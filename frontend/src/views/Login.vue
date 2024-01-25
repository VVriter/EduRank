<template>
    <main style="min-height: 80vh; display: flex; justify-content: center; align-items: center;">
        <el-card style="width: 370px;">
            <template #header>
                <el-row>
                    <el-text style="font-size: 25px;">{{titleText}}</el-text>
                    <el-icon style="margin-left: auto;" size="30px">
                        <User/>
                    </el-icon>
                </el-row>
            </template>


            <div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <el-radio-group v-model="loginType">
                    <el-radio-button label="login">Ввійти</el-radio-button>
                    <el-radio-button label="registration">Зареєструватись</el-radio-button>
                </el-radio-group>   
            </div>

            <div style="margin-top: 10px; display: flex; flex-direction: column; width: 100%;" v-if="loginType == 'registration'">
                <el-input v-model="name" placeholder="Ім'я"/>
                <el-input v-model="surname" style="margin-top: 10px;" placeholder="Прізвище"/>
                <el-radio-group v-model="userType" style="margin-top: 10px;">
                    <el-radio-button label="pupil">Я учень</el-radio-button>
                    <el-radio-button label="parrent">Я батько / мати</el-radio-button>
                    <el-radio-button label="teacher">Я вчитель</el-radio-button>
                </el-radio-group>
                <el-input v-model="email" style="margin-top: 10px;" placeholder="Електронна пошта"/>
                <el-button :disabled="!(name && surname && email && userType)" :loading="loading" @click="register" size="large" type="primary" style="margin-top: 10px;">
                    Зареєструватись
                </el-button>
            </div>

            <div style="margin-top: 10px; display: flex; flex-direction: column; width: 100%;" v-else>
                <el-input v-model="email" placeholder="Електронна пошта"/>
                <el-button @click="login" :loading="loading" :disabled="!email" size="large" type="primary" style="margin-top: 10px;">Ввійти</el-button>
            </div>
        </el-card>
    </main>
</template>

<script setup>
    import { User } from '@element-plus/icons-vue'
    import { ref, computed, onMounted } from 'vue'
    import { useUserStore } from '../stores/userStore'
    import { ElNotification } from 'element-plus'
    import { useRouter } from 'vue-router'

    const router = useRouter()

    const userStore = useUserStore()
    onMounted(async () => {
        if (userStore.loginned) 
            router.push({name: "Home"})
    })

    const loginType = ref('registration')
    const titleText = computed(() => {
        return loginType.value == 'login' ? "Вхід" : "Реєстрація"
    })

    const name = ref()
    const surname = ref()
    const email = ref()
    const userType = ref('pupil')
    const loading = ref(false)

    async function login() {
        loading.value = true

        if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value)) {
            ElNotification({
                title: 'Помилка',
                message: 'Електронна пошта введена не правильно',
                type: 'error',
            })
            setTimeout(() => {
                loading.value = false
                email.value = null
            }, 1000)
            return
        }

        const res = await fetch(`/api/login`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email.value
            })
        })

        if (res.status == 200) {
            router.push(`/email?email=${email.value}`)
        } else {
            ElNotification({
                title: 'Невідома помилка',
                message: 'Перевірте чи правильно заповнена форма, та чи не використовували ви цей емайл раніше на нашому сайті.',
                type: 'error',
            })
            setTimeout(() => {
                loading.value = false
            }, 1000)
        }
    }

    async function register() {
        loading.value = true

        if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value)) {
            ElNotification({
                title: 'Помилка',
                message: 'Електронна пошта введена не правильно',
                type: 'error',
            })
            setTimeout(() => {
                loading.value = false
                email.value = null
            }, 1000)
            return
        }

        if (!name.value || !surname.value || !email.value || !userType.value) {

            loading.value = false
            return
        }

        const res = await fetch("/api/register", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name.value,
                surname: surname.value,
                email: email.value,
                userType: userType.value
            })
        })

        if (res.status == 200) {
            router.push(`/email?email=${email.value}`)
        } else {
            ElNotification({
                title: 'Невідома помилка',
                message: 'Перевірте чи правильно заповнена форма, та чи не використовували ви цей емайл раніше на нашому сайті.',
                type: 'error',
            })
            setTimeout(() => {
                loading.value = false
            }, 1000)
        }

        loading.value = false
    }
</script>
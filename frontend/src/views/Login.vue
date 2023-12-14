<template>
    <main style="min-height: 80vh; display: flex; justify-content: center; align-items: center;">
        <el-card style="min-width: 400px;">
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
                <el-button :loading="loading" @click="register" size="large" type="primary" style="margin-top: 10px;">
                    Зареєструватись
                </el-button>
            </div>

            <div style="margin-top: 10px; display: flex; flex-direction: column; width: 100%;" v-else>
                <el-input placeholder="Електронна пошта"/>
                <el-button size="large" type="primary" style="margin-top: 10px;">Ввійти</el-button>
            </div>
        </el-card>
    </main>
</template>

<script setup>
    import { User } from '@element-plus/icons-vue'
    import { ref, computed } from 'vue'
    const loginType = ref('registration')
    const titleText = computed(() => {
        return loginType.value == 'login' ? "Вхід" : "Реєстрація"
    })

    const name = ref()
    const surname = ref()
    const email = ref()
    const userType = ref('pupil')
    const loading = ref(false)

    function register() {
        loading.value = true
        fetch("/api/register", {
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
        loading.value = false
    }
</script>
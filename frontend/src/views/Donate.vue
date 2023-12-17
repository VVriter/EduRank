<template>
    <main style="width: 80%; min-height: 80vh; justify-content: center; align-items: center;">
        <div class="wrapper">
            <div class="side">
                <el-icon size="300px">
                    <Money/>
                </el-icon>
            </div>
            <div class="side">
                <el-text style="font-size: 35px; text-align: start; width: 100%;">Ваша підтримка для нас все!</el-text>
                <el-text type="info" style="margin-top: 20px; font-size: 18px;">Підтримуючи наш проект копійкою - ви інвестуєте в майбутнє нашої країни. Рішення, що ми розробляємо - як ніколи потрібні сучасній освітній системі. Кількість фінансів на нашому рахунку прямопропорційно впливають на швидкість розробки продукту.</el-text>
                <el-text type="info" style="margin-top: 20px; font-size: 18px;">Виберіть тариф котрий вам найбільше підходить, та підтримайте майбутнє нашої держави!</el-text>

                <div v-if="state == 1" style="gap: 10px; margin-top: 50px; width: 100%; display: flex; flex-wrap: wrap; justify-content: center; align-items: center;">
                    <el-button type="info" plain @click="setCount(50)" style="margin: 0; width: 15vh; height: 15vh;">50₴</el-button>
                    <el-button type="info" plain @click="setCount(100)" style="margin: 0; width: 15vh; height: 15vh;">100₴</el-button>
                    <el-button type="info" plain @click="setCount(300)" style="margin: 0; width: 15vh; height: 15vh;">300₴</el-button>
                    <el-button type="info" plain @click="setCount(500)" style="margin: 0; width: 15vh; height: 15vh;">500₴</el-button>
                    <el-button type="danger" plain @click="myCount" style="margin: 0; width: 15vh; height: 15vh;">Своя сумма</el-button>
                </div>

                <div v-if="state == 2" style="margin-top: 50px; width: 100%;">
                    <el-input v-model="name" style="margin-top: 10px;" placeholder="Ім'я та прізвище" size="large"/>
                    <el-input v-model="contact" style="margin-top: 10px;" placeholder="Контактні данні" size="large"/>
                    <el-input placeholder="Поставте сумму для оплати" size="large" style="margin-top: 10px;" type="number" v-if="isSelfChooSeCount" v-model="plan"/>
                    <el-input v-model="message" style="margin-top: 10px;" type="textarea" placeholder="Повідомлення розробникам (не обов'язково)" size="large"/>
                    <el-button @click="donate" :loading="loading" :disabled="!(name && contact)" style="margin-top: 10px; width: 100%;" size="large" plain type="primary">Задонатити!</el-button>
                </div>

                <div class="delimiter"></div>
            </div>
        </div>
    </main>
</template>

<script setup>
    import { Money } from '@element-plus/icons-vue'
    import { ref } from 'vue'

    const state = ref(1)
    const plan = ref(null)

    const name = ref()
    const contact = ref()
    const message = ref()

    const loading = ref(false)

    function setCount(num) {
        plan.value = num
        state.value++
    }

    const isSelfChooSeCount = ref(false)

    function myCount() {
        isSelfChooSeCount.value = true
        plan.value = 350
        state.value++
    }

    async function donate() {
        loading.value = true
        const res = await fetch(`/api/donate?amount=${plan.value}00`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                contact: contact.value,
                description: message.value ? message.value : "Без повідомлення"
            })
        })

        if (res.status == 200) {
            const json = await res.json()
            const page = json.mono.pageUrl
            location.replace(page)
            loading.value = false
        } else {
            ElNotification({
                title: 'Невідома помилка',
                message: 'Щось пішло не так, спробуйте пізніше',
                type: 'error',
            })
            setTimeout(() => {
                loading.value = false
            }, 1000)
        }
    }
</script>

<style scoped>
    .wrapper {
        display: flex; 
        width: 100%;
        flex-direction: row;
    }

    .side {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        width: 50%;
    }

    @media only screen and (max-width: 767px) {
        .wrapper {
            flex-direction: column;
        }

        .side {
            width: 100%;
        }

        .delimiter {
            margin-bottom: 100px;
        }
    }
</style>
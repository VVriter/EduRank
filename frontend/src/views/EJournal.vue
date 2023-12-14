<template>
    <main>
        <div style="width: 100%; margin-top: 20px;">
            <div class="box">
                <div class="subBox" style="display: flex; justify-content: center; align-items: center; padding: 10px;">
                    <img class="img" style="border-radius: 30px;" src="@/assets/img/logo.png" alt="">
                </div>
                <div class="subBox" style="display: flex; flex-direction: column;">
                    <el-text style="font-size: 30px;">Сучасні проблеми потребують СУЧАСНИХ рішень. Суб-проєк EduJournal вирішує проблему взаємодії учнів та батьків.</el-text>
                    <el-text style="font-size: 30px; margin-top: 50px;">Проєкт EduJournal вирішує проблеми з якими зіштовхуються батьки та адміністрації шкіл при спробі приєднатись до інших ресурсів таких як Є-Школа.</el-text>
                </div>
            </div>
        </div>

        <div style="width: 100%; margin-top: 100px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <el-text style="font-size: 40px;">Чому ми?</el-text>
            <div style="gap: 30px; display: flex; flex-wrap: wrap; margin-top: 30px; user-select: none;">
                <el-row>
                    <el-button type="warning" :icon="Star" circle size="large" />
                    <div style="margin-left: 10px; display: flex; flex-direction: column;">
                        <el-text style="font-size: 30px;">Безоплатність</el-text>
                        <el-text type="info" style="font-size: 25px; width: 240px;">Наш проєкт розроблюється абсолютно на безоплатній основі</el-text>
                    </div>
                </el-row>

                <el-row>
                    <el-button type="success" :icon="Paperclip" circle size="large" />
                    <div style="margin-left: 10px; display: flex; flex-direction: column;">
                        <p style="font-size: 30px;">Легкість</p>
                        <el-text type="info" style="font-size: 25px; width: 240px;">Використати наш журнал можна буквально за 2 кліки</el-text>
                    </div>
                </el-row>

                <el-row>
                    <el-button type="danger" :icon="Position" circle size="large" />
                    <div style="margin-left: 10px; display: flex; flex-direction: column;">
                        <p style="font-size: 30px;">Якість</p>
                        <el-text type="info" style="font-size: 25px; width: 240px;">На розробку витрачається часу рівно стільки, скільки потрібно</el-text>
                    </div>
                </el-row>

                <el-row>
                    <el-button type="primary" :icon="DataLine" circle size="large" />
                    <div style="margin-left: 10px; display: flex; flex-direction: column;">
                        <p style="font-size: 30px;">Довіра</p>
                        <el-text type="info" style="font-size: 25px; width: 240px;">Використовуючи наш продукт ви впевнені за збереження данних</el-text>
                    </div>
                </el-row>
            </div>
        </div>

        <div style="margin-top: 100px; margin-bottom: 100px;">
            <el-card shadow="hover" style="min-width: 400px; max-width: 400px;">
                <template #header>
                    <el-row>
                        <el-text style="font-size: 20px;">Підтримати нас!</el-text>
                        <el-icon style="margin-left: auto;" size="30px">
                            <Money/>
                        </el-icon>
                    </el-row>
                </template>

                <el-text>Ваша підтримка безумовно важлива для нас, кожен хто пітримає нас - матиме доступ до БЕТА-ТЕСТУ нашого застосунку.</el-text>

                <div style="margin-top: 10px; height: 50px; border-radius: 3px; background-color: var(--el-color-success-light-3); width: 100%; display: flex; flex-direction: row; align-items: center;">
                    <img style="width: 30px; margin-left: 10px; border-radius: 5px;" src="@/assets/img/mono.jpg" alt="">
                    <el-text style="margin-left: 10px;">4441 1111 3499 1490</el-text>
                </div>
            </el-card>
        </div>
    </main>
</template>

<script setup>
    import {Star, Paperclip, DataLine, Position, Money} from '@element-plus/icons-vue'
</script>

<style scoped>
    main {
        width: 90%;
    }

    .box {
        display: flex;
        flex-direction: row;
    }

    .subBox {
        width: 50%;
    }

    @media only screen and (max-width: 767px) {
        .box {
            flex-direction: column;
        }

        .subBox {
            width: 90%;
        }

        .img {
            width: 99%;
        }
    }
</style>
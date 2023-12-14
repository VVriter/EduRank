<template>
    <main style="width: 80%; height: 80vh; justify-content: center; align-items: center;">
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
    </main>
</template>
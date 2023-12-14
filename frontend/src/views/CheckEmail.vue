<template>
    <main style="display: flex; height: 80vh; justify-content: center; align-items: center;">
        <el-card style="min-width: 400px; max-width: 400px;">
            <template #header>
                <el-row>
                    <el-text style="font-size: 20px;">Підтвердження емайлу</el-text>
                    <el-icon size="30px" style="margin-left: auto;">
                        <Postcard/>
                    </el-icon>
                </el-row>
            </template>

            <el-text type="info">На емайл <el-text type="primary">{{ $route.query.email }}</el-text> був відправлений лист з підтвердженням облікового запису. Перейдіть в ваш поштовий ящик та слідуйте інструкціям.</el-text>
        </el-card>
    </main>
</template>

<script setup>
    import { Postcard } from '@element-plus/icons-vue'
</script>
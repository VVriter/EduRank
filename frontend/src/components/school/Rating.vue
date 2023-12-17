<template>
    <el-card shadow="hover" style="border-radius: 10px;">
        <template #header>
            <el-row>
                <el-text style="font-size: 15px;">Рейтинг</el-text>
                <el-icon style="margin-left: auto;" size="30px">
                    <Star />
                </el-icon>
            </el-row>
        </template>

        <div style="display: flex; flex-direction: row;">
            <el-text type="info" style="width: 80%;">Завдяки рейтингу користувачі можуть побачити більш важливу інформацію, яку потрібно невідкладно поділитися.</el-text>
            <img style="width: 100px; object-fit: cover; overflow: visible; scale: 0.8;" src="@/assets/img/study lamp.png" alt="">
        </div>
    </el-card>
</template>

<script setup>
import { Star } from '@element-plus/icons-vue'
</script>
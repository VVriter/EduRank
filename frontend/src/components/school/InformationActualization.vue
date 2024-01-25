<template>
    <el-card shadow="hover" style="border-radius: 10px;">
        <template #header>
            <el-row>
                <el-text style="font-size: 20px;">Актуалізація інформації</el-text>
                <el-icon style="margin-left: auto;" size="30px">
                    <Edit />
                </el-icon>
            </el-row>
        </template>
        
        <div style="display: flex; flex-direction: row;">
            <el-text type="info" style="width: 80%;">Якщо ви є представником навчального закладу, ви можете оновити інформацію на сторінках школи.</el-text>
            <img style="width: 100px; object-fit: cover;" src="@/assets/img/academic hat.png" alt="">
        </div>

        <el-button round size="large" style="margin-top: 10px; width: 100%;">Оформити заявку</el-button>
    </el-card>
</template>

<script setup>
import { Edit } from '@element-plus/icons-vue'
</script>
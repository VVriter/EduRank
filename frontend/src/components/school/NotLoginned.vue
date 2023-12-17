<template>
    <el-card style="margin-top: 10px;">
        <template #header>
            <div style="opacity: 50%; display: flex; flex-direction: row;">
                <el-text>Залиште відгук на цю установу!</el-text>
                <el-icon style="margin-left: auto;" size="20px">
                    <Star/>
                </el-icon>
            </div>
        </template>

        <el-text type="danger">
            Ви не можете залишити відгук в цій категорії тому, що ви не ввійшли в свій обліковий запис.
        </el-text>
        <div style="margin-top: 10px;">
            <el-button @click="$router.push('/login')" size="large" plain type="success">Ввійти!</el-button>
            <el-button @click="action" size="large" plain type="warning">Залишити анонімно.</el-button>
        </div>
    </el-card>
</template>

<script setup>
    const props = defineProps({
        action: { required: true, type: Object }
    })
</script>
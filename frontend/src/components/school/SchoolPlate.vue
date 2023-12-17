<template>
    <el-card style="border-radius: 10px; margin-top: 10px;" body-style="padding: 0;">
        <div style="padding: 10px;">
            <img @error="erroredImageLoading = true" style="border-radius: 10px; width: 100%; max-height: 200px;" v-if="image" :src="image" alt="">
            <div v-else style="padding: 10px;">
                <el-skeleton/>
            </div>
            <img style="border-radius: 10px; width: 100%; max-height: 300px; scale: 0.5;" v-if="erroredImageLoading" src="@/assets/img/school.png" alt="">
        </div>

        <div style="padding: 10px; display: flex; flex-direction: column; gap: 10px;">
            <el-card body-style="padding: 10px;" style="cursor: pointer; display: flex; justify-content: start; align-items: center;" shadow="hover">
                <div style="display: flex; flex-direction: row;">
                    <el-icon size="30px"><School/></el-icon>
                    <el-text style="width: 55%; margin-left: 5px;" truncated>{{ school.institution_name }}</el-text>
                </div>
            </el-card>

            <el-card body-style="padding: 10px;" style="cursor: pointer; display: flex; justify-content: start; align-items: center;" shadow="hover">
                <div style="display: flex; flex-direction: row;">
                    <el-icon size="30px"><LocationFilled/></el-icon>
                    <el-text style="margin-left: 5px;" truncated>{{ school.address }}</el-text>
                </div>
            </el-card>

            <div style="display: flex; flex-direction: row; width: 100%; gap: 10px;">
                <el-card body-style="padding: 10px;" style="cursor: pointer; display: flex; justify-content: start; align-items: center; width: 50%;" shadow="hover">
                    <div style="display: flex; flex-direction: row;">
                        <el-icon size="30px"><View/></el-icon>
                        <el-text style="margin-left: 5px;" truncated>Відкрито</el-text>
                    </div>
                </el-card>
                <el-card body-style="padding: 10px;" style="cursor: pointer; display: flex; justify-content: start; align-items: center; width: 50%;" shadow="hover">
                    <div style="display: flex; flex-direction: row;">
                        <el-icon size="30px"><Clock/></el-icon>
                        <el-text style="margin-left: 5px;">06:00-19:00</el-text>
                    </div>
                </el-card>
            </div>

            <el-card body-style="padding: 10px;" style="cursor: pointer; display: flex; justify-content: start; align-items: center;" shadow="hover">
                <div style="display: flex; flex-direction: row;">
                    <el-icon size="30px"><Avatar/></el-icon>
                    <el-text style="margin-left: 5px;" truncated>{{ school.boss }}</el-text>
                </div>
            </el-card>

            <hr>

            <el-card body-style="padding: 10px;" style="cursor: pointer; display: flex; justify-content: start; align-items: center;" shadow="hover">
                <div style="display: flex; flex-direction: row; width: 100%;">
                    <el-icon size="30px"><Phone/></el-icon>
                    <el-text style="margin-left: 5px; width: 120px;">+{{ school.phone }}</el-text>
                </div>
            </el-card>

            <el-card body-style="padding: 10px;" style="cursor: pointer; display: flex; justify-content: start; align-items: center;" shadow="hover">
                <div style="display: flex; flex-direction: row; width: 100%;">
                    <el-icon size="30px"><Message/></el-icon>
                    <el-text style="margin-left: 5px; width: 200px;">{{ school.email }}</el-text>
                </div>
            </el-card>
        </div>

    </el-card>
</template>

<script setup>
    import { School, Position, Postcard, Phone, LocationFilled, View, Clock, Avatar, CopyDocument, Message } from '@element-plus/icons-vue'
    import { ref, onMounted } from 'vue' 

    const props = defineProps({
        school: { required: true }
    })

    const image = ref()
    const reviews = ref()

    const erroredImageLoading = ref(false)

    onMounted(async () => {
        const res = await fetch(`/api/images?query=${props.school.institution_name}`)
        const json = await res.json()
        image.value = json.items[0].link
    })

</script>
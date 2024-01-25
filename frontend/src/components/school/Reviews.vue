<template>
	<div class="container">
		<div class="side">
			<el-empty style="width: 50%;" description="В цієї школи ще немає відгуків, станьте першим, хто його залишить!" v-if="reviews.length == 0"/>
		</div>
		<hr>
		<div v-if="!leaveAnnon" class="side" style="min-height: 45vh;">
			<el-text style="font-size: 30px;">Залиште відгук!</el-text>
			<div v-if="userStore.loginned">

			</div>
			<div style="gap: 10px; display: flex; flex-direction: column; justify-content: center; align-items: center;" v-else>
				<el-divider style="width: 200px; margin: 0; margin-top: 10px; "/>
				<p>але...</p>
				<el-button @click="$router.push('/login')" size="large" round type="danger">Спочатку потрібно ввійти</el-button>
				<el-divider style="width: 240px; margin: 0;"/>
				<p>aбо</p>
				<el-button @click="leaveAnnon = true" size="large" round type="primary">Залишити анонімно</el-button>
			</div>
		</div>
		<div v-else class="side" style="justify-content: start; align-items: start; padding: 10px;">
			<el-button @click="leaveAnnon = false" type="primary" :icon="ArrowLeftBold" size="large" round>Назад</el-button>
			<div style="gap: 10px; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;" >
				<div style="width: 300px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
					<el-icon size="100px"><Avatar/></el-icon>
					<p style="margin-left: 3px; text-align: start; width: 100%;">Ім'я (опціонально)</p>
					<el-input placeholder="Ім'я"/>
					<p style="margin-left: 3px; margin-top: 10px; text-align: start; width: 100%;">Відгук <el-text type="danger">*</el-text></p>
					<el-input type="textarea" :rows="3" size="large" placeholder="Відгук"/>
					<el-button style="margin-top: 10px; width: 100%;" round size="large">Відправити</el-button>
				</div>
			</div>
		</div>	
	</div>
</template>

<script setup>
	import {ArrowLeftBold, Avatar} from '@element-plus/icons-vue'
	import { useUserStore } from '../../stores/userStore';
	const userStore = useUserStore()
	import { ref, computed, onMounted } from 'vue'
	const reviews = ref([])
	const leaveAnnon = ref(false)

	const props = defineProps({
		school: { required: true }
	})

	onMounted(async () => {
		const res = await fetch(`/api/reviews?edbo=${props.school.institution_id}`)
		const json = await res.json()
		const reviewses = json.reviews
		reviewses.forEach(element => {
			const rev = JSON.parse(element)
			reviews.value.push(rev)
		});
	})
</script>

<style scoped>

	.side {
		width: 50%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.container {
		display: flex;
		width: 100%;
		min-height: 55vh;
	}

	@media (max-width: 769px) {
        .container {
			flex-direction: column;
        }

		.side {
			width: 100%;
			min-height: 30vh;
		}
    }
</style>
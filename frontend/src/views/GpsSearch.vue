<template>
	<main style="height: 80vh; margin-bottom: 20px;" v-if="!positionGetted">
		<el-icon size="300px">
			<Position/>
		</el-icon>
		<el-text style="font-size: 30px; width: 50%; text-align: center;">Надайте будьласка доступ до вашого місця знаходження</el-text>
	</main>

	<main v-else>
		<main style="height: 55vh; display: flex; flex-direction: column; gap: 10px; justify-content: center; align-items: center;" v-if="!finded">
			<el-text style="margin-right: 40px; font-size: 20px; text-align: center;">Завантажуємо список</el-text>
			<el-progress :format="format" style="width: 400px;" :duration="2" :percentage="80" :indeterminate="true" :stroke-width="15" striped  />
		</main>

		<main style="min-height: 55vh;" v-else>
			{{positionGetted.coords.longitude}}
			{{positionGetted.coords.latitude}}
		</main>
	</main>
</template>

<script setup>
	import { Position } from '@element-plus/icons-vue'
	import { onMounted, ref } from 'vue';

	const positionGetted = ref()
	const finded = ref(false)

	onMounted(async () => {
        navigator.geolocation.getCurrentPosition((position) => {
			positionGetted.value = position
		}, (err) => {

		});
	})

	
	const format = (percentage) => ("")
</script>
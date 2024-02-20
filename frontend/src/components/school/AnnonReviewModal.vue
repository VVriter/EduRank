<template>
	<el-card shadow="hover" style="border-radius: 10px;">
		<el-button @click="closeModal" type="primary" :icon="ArrowLeftBold" size="large" round>Назад</el-button>
		<div style="gap: 10px; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;" >
			<div style="width: 320px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
				<el-text style="font-size: 20px; text-align: center; margin-top: 30px; margin-bottom: 30px;">Залишити анонімний відгук</el-text>
				<p style="margin-left: 3px; text-align: start; width: 100%;">Ім'я (опціонально)</p>
				<el-input placeholder="Ім'я"/>
				<p style="margin-left: 3px; margin-top: 10px; text-align: start; width: 100%;">Відгук <el-text type="danger">*</el-text></p>
				<el-input type="textarea" :rows="3" size="large" placeholder="Відгук"/>
				<el-button style="margin-top: 10px; width: 100%;" round size="large">Відправити</el-button>
			</div>
		</div>
	</el-card>
</template>

<script setup>
	import { closeModal } from 'jenesius-vue-modal'
	import { ArrowLeftBold, Avatar } from '@element-plus/icons-vue';
</script>
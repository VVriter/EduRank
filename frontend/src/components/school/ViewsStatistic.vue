<template>
    <el-card shadow="hover" style="border-radius: 10px;">
        <template #header>
            <el-row>
                <el-text style="font-size: 18px;">Статистика відвідувань</el-text>
                <el-icon style="margin-left: auto;" size="30px">
                    <View/>
                </el-icon>
            </el-row>
        </template>

        <Bar
            id="my-chart-id"
            :options="chartOptions"
            :data="chartData"
        />
    </el-card>
</template>

<script setup>
    import { View } from '@element-plus/icons-vue'
    import { Bar } from 'vue-chartjs'
    import {ref} from 'vue'

    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

    const chartData = ref({
        label: "Відвідування",
        labels: ['Вчора', 'Сьогодні', 'За годину'],
        datasets: [{
            label: 'Відвідування',
            data: [40, 20, 12],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    })

    const chartOptions = ref({
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    })
</script>
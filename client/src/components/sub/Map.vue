<template>
    <div>
        <img src="@/assets/map.png" alt="" class="inmg">
    </div>
</template>

<script>
    export default {
        name: "Map",
        props: {
            data: {
                requiered: true
            }
        },
        mounted() {
            console.log(JSON.stringify(this.data))
        }
    }
</script>

<style scoped>
    .inmg {
        width: 100%;
    }
</style>
<template>
    <div>

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
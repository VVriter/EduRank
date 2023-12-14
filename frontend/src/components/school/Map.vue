<template>
    <GMapMap
        :center="center"
        :zoom="7"
        style="width: 500px; height: 300px; border-radius: 10px;"
    >
        <GMapCluster>
            <GMapMarker
                :key="index"
                v-for="(m, index) in markers"
                :position="m.position"
                :clickable="true"
                :draggable="true"
                @click="center = m.position"
            />
        </GMapCluster>
    </GMapMap>
</template>

<script setup>
    const center = ref({ lat: 51.093048, lng: 6.842120 })
    const markers = ref([
        {
            position: {
                lat: 51.093048, lng: 6.842120
            },
        }
    ])
</script>
<template>
    <GMapMap v-if="loaded"
        :center="center"
        :zoom="18"
        :options="mapOptions"
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

    import {ref, onMounted} from 'vue'

    const props = defineProps({
        prompt: { required: true }
    })

    const mapOptions = ref({
        style: "dark",
        theme: "dark"
    });

    const loaded = ref(false)

    const center = ref()
    const markers = ref([
        {
            position: {
                lat: 51.093048, lng: 6.842120
            },
        }
    ])

    onMounted(async () => {
        const res = await fetch(`https://maps.googleapis.com/maps/api/geocode/json?address=${props.prompt}&key=AIzaSyDDy5IUrvL4bVAdeQ_MBvcqsy1rgs5X3V4`)
        const json = await res.json()
        center.value = json.results[0].geometry.location
        markers.value = [
            {
                position: json.results[0].geometry.location
            }
        ]
        loaded.value = true
    })
</script>
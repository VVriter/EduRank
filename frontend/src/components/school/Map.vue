<template>
    <GMapMap v-if="loaded"
        :center="center"
        :zoom="zoomVal"
        :options="mapOptions"
    >
            <GMapMarker
                :key="index"
                v-for="(m, index) in markers"
                :position="m.position"
                :clickable="true"
                :draggable="true"
                @click="center = m.position"
                :title="name"
                :animation="0"
            >
            <GMapInfoWindow :opened="true" :closeclick="false" :auto-close="false" :position="m.position">
                <div style="max-width: 400px;">
                    <p style="text-align: center; color: black; font-size: 20px;">{{ name }}</p>
                    <el-button type="success" style="width: 100%;">
                        Перейти до гугл карт
                    </el-button>
                </div>
            </GMapInfoWindow>
            </GMapMarker>
    </GMapMap>
</template>

<script setup>
    import { useUiConfigStore } from '../../stores/uiThemeStore';
    import {ref, onMounted, computed} from 'vue'

    const uiConfigStore = useUiConfigStore()

    const props = defineProps({
        prompt: { required: true },
        name: { required: true },
        rank: { required: true }
    })

    const mapOptions = computed(() => {
        if (uiConfigStore.isDarkModeOn) {
            return {
                gestureHandling: 'none',
                disableDefaultUI: true,
                styles: [
                    { elementType: "geometry", stylers: [{ color: "#242f3e" }] },
                    { elementType: "labels.text.stroke", stylers: [{ color: "#242f3e" }] },
                    { elementType: "labels.text.fill", stylers: [{ color: "#746855" }] },
                    { featureType: "administrative.locality", elementType: "labels.text.fill", stylers: [{ color: "#d59563" }], },
                    { featureType: "poi", elementType: "labels.text.fill", stylers: [{ color: "#d59563" }], },
                    { featureType: "poi.park", elementType: "geometry", stylers: [{ color: "#263c3f" }], },
                    { featureType: "poi.park", elementType: "labels.text.fill", stylers: [{ color: "#6b9a76" }], },
                    { featureType: "road", elementType: "geometry", stylers: [{ color: "#38414e" }], },
                    { featureType: "road", elementType: "geometry.stroke", stylers: [{ color: "#212a37" }], },
                    { featureType: "road", elementType: "labels.text.fill", stylers: [{ color: "#9ca5b3" }], },
                    { featureType: "road.highway", elementType: "geometry", stylers: [{ color: "#746855" }], },
                    { featureType: "road.highway", elementType: "geometry.stroke", stylers: [{ color: "#1f2835" }],},
                    { featureType: "road.highway", elementType: "labels.text.fill", stylers: [{ color: "#f3d19c" }], },
                    { featureType: "transit", elementType: "geometry", stylers: [{ color: "#2f3948" }], },
                    { featureType: "transit.station", elementType: "labels.text.fill", stylers: [{ color: "#d59563" }], },
                    { featureType: "water", elementType: "geometry", stylers: [{ color: "#17263c" }], },
                    { featureType: "water", elementType: "labels.text.fill", stylers: [{ color: "#515c6d" }], },
                    { featureType: "water", elementType: "labels.text.stroke", stylers: [{ color: "#17263c" }],},
                    {
                        featureType: "poi",
                        elementType: "labels",
                        stylers: [{ visibility: "off" }]
                    },
                    {
                        featureType: "transit",
                        elementType: "labels",
                        stylers: [{ visibility: "off" }]
                    }
                ]
            }
        } else {
            return {
                gestureHandling: 'none',
                disableDefaultUI: true,
                styles: [
                    {
                        featureType: "poi",
                        elementType: "labels",
                        stylers: [{ visibility: "off" }]
                    },
                    {
                        featureType: "transit",
                        elementType: "labels",
                        stylers: [{ visibility: "off" }]
                    }
                ]
            }
        }
    })

    const loaded = ref(false)

    const center = ref()
    const markers = ref([
        {
            position: {
                lat: 51.093048, lng: 6.842120
            },
        }
    ])

    const zoomVal = ref(18)

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
        setTimeout(function() {
            zoomVal.value = 15
        }, 3000)
    })
</script>
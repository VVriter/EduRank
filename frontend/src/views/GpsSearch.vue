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

		<main style="min-height: 55vh; width: 90%;" v-else>
			<GMapMap
				:center="{
					lat: positionGetted.coords.latitude,
					lng: positionGetted.coords.longitude
				}"
				:zoom="11"
				mapType="terrain"
				:options="mapOptions"
				style="width: 100%; height: 100vh; border-radius: 10px;"
			>
				<!--My location-->
				<GMapCircle
					:radius="Math.sqrt(2) * 100"
					:center="{
						lat: positionGetted.coords.latitude,
						lng: positionGetted.coords.longitude
					}"
					:options="{
						strokeColor: '#FF0000',
						strokeOpacity: 0.8,
						strokeWeight: 2,
						fillColor: '#FF0000',
						fillOpacity: 0.35,
					}"
				/>

				<!--Radious of search-->
				<GMapCircle
					:radius="Math.sqrt(10000) * 100"
					:center="{
						lat: positionGetted.coords.latitude,
						lng: positionGetted.coords.longitude
					}"
					:options="{
						strokeColor: '#7F00FF',
						strokeOpacity: 0.8,
						strokeWeight: 2,
						fillColor: '#7F00FF',
						fillOpacity: 0.35,
					}"
				/>

				<GMapMarker
					v-for="(marker, index) in localSchools.all"
					:position="marker.more.geometry.location"
					:clickable="true"
					@click="console.log('asdasd')"
				/>
			</GMapMap>
		</main>
	</main>
</template>

<script setup>
	import { Position } from '@element-plus/icons-vue'
	import { onMounted, ref } from 'vue';

	const positionGetted = ref()
	const localSchools = ref()
	const finded = ref(false)

	const mapOptions = ref({
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
		],
	})

	onMounted(async () => {
        navigator.geolocation.getCurrentPosition(async (position) => {
			positionGetted.value = position
			const res = await fetch(`/api/searchNear?longitude=${position.coords.longitude}&latitude=${position.coords.latitude}`)
			const json = await res.json()
			localSchools.value = json
			finded.value = true
		}, (err) => {

		});
	})

	
	const format = (percentage) => ("")
</script>
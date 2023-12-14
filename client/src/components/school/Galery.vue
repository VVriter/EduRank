<template>
    <div class="gallery-container">
        <p class="gallery-title">Галерея зображень по запиту "{{ name }}"</p>
        <div class="gallery">
            <div v-for="image in images.items" :key="image.link">
                <img 
                :src="image.link" :alt="image.alt" 
                class="gallery-image" 
                @error="handleImageError(image)"
                @click="showInfo(image)"
                v-if="!erroredImages.includes(image)" />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Gallery",
    props: {
        images: {
            required: true,
        },
        name: {
            required: true,
        },
    },
    data() {
        return {
            erroredImages: [],
        };
    },
    methods: {
        handleImageError(image) {
            console.log(`Image loading error: ${image.link}`);
            this.erroredImages.push(image);
        },
        showInfo(image) {
            this.$swal({
                title: image.htmlTitle,
                text: `Ресурс звідки взята картинка: ${image.displayLink}`,
                imageUrl: image.link,
                imageWidth: image.image.width,
                imageHeight: 400,
                imageAlt: 'Custom image',
            });
        }
    },
};
</script>

<style scoped>
.gallery-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
}

.gallery-title {
    font-size: 3vh;
    text-align: center;
    margin: 1rem 0;
    color: #333;
}

.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
}

.gallery div {
    width: 25vh;
    cursor: pointer;
}

.gallery-image {
    width: 25vh;
    height: 100%;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: all 0.3s;
}

.gallery-image:hover {
    transform: scale(1.05);
    filter: brightness(0.8);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

@media only screen and (max-width: 700px) {
    .gallery {
        height: 500px;
        overflow: scroll;
    }
}
</style>

<template>
  <div class="gallery">

      <div v-for="image in validImages" class="gallery-item" :key="image.id">
        <div class="image-container">
          <img
            :src="image.link"
            :alt="image.title"
            class="gallery-image rounded"
            @load="image.loaded = true"
          />
          <div v-if="!image.loaded" class="loading-indicator">Loading...</div>
        </div>
      </div>

  </div>
</template>

<script>
export default {
  name: 'Gallery',
  props: {
    data: {
      required: true,
    },
  },
  data() {
    return {
      hoveredImage: null,
    };
  },
  computed: {
    validImages() {
      // Filter the images to include only those with valid extensions
      return this.data.items.filter((image) => {
        const validExtensions = ['.png', '.jpeg', '.jpg', '.webp'];
        const imageLink = image.link.toLowerCase();
        return validExtensions.some((ext) => imageLink.endsWith(ext));
      });
    },
  },
  methods: {
    hoverImage(image) {
      this.hoveredImage = image;
    },
    unhoverImage() {
      this.hoveredImage = null;
    },
  },
};
</script>

<style scoped>
/* Gallery container */
.gallery {
  display: flex;
  flex-wrap: wrap;
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  padding: 0.3rem;
  background: linear-gradient(to bottom, #d1ccce, #346379);
  border-radius: 1vh;
  margin: 1vh;
}

/* Individual gallery item */
.gallery-item {
  width: calc(33.33% - 1rem);
  padding: 0.3rem;
  box-sizing: border-box;
}

/* Container for the image */
.image-container {
  margin-left: auto;
  margin-right: auto;
  position: relative;
  overflow: hidden;
  padding-top: 100%;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* Gallery image */
.gallery-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.2s;
}

/* Rounded corners for the images */
.rounded {
  border-radius: 1vh;
}

/* Loading indicator */
.loading-indicator {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.8);
  position: absolute;
  top: 0;
  left: 0;
  z-index: 2;
}

/* Hover effect */
.image-container:hover .gallery-image {
  transform: scale(1.1);
}
</style>

<template>
    <div class="gallery">
      <div v-for="image in validImages" class="gallery-item">
        <img :src="image.link" :alt="image.title" class="gallery-image" />
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
  };
  </script>
  
  <style scoped>
  /* Your existing styling goes here */
  
  .gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 1rem;
    background: linear-gradient(to bottom, #d1ccce, #346379);
    border-radius: 1vh;
    margin: 1vh;
  }
  
  .gallery-item {
    flex: 0 0 calc(33.33% - 1rem);
    margin: 0.5rem;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .gallery-image {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 8px;
  }
  </style>
  
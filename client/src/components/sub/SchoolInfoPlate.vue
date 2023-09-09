<template>
    <div class="school_info">
      <div class="layers">
        <div class="layer">
          <div class="hexagon">
            <p class="hex_title">выыыыы</p>
          </div>
          <div class="hexagon"></div>
          <div class="hexagon"></div>
        </div>
  
        <div class="layer">
          <div class="hexagon"></div>
          <img src="@/assets/hat.png" alt="Your Image" class="center-image" />
          <div class="hexagon"></div>
        </div>
  
        <div class="layer">
          <div class="hexagon"></div>
          <div class="hexagon"></div>
          <div class="hexagon"></div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "SchoolInfoPlate",
    props: {
      data: {
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  .school_info {
    display: flex;
    flex-direction: column;
    width: 100%;
  }
  
  .layers {
    display: flex;
    flex-direction: column;
    margin-right: auto;
    margin-left: auto;
  }
  
  .layer {
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-direction: row;
  }
  
  .center-image {
    width: 30vh;
    margin-left: auto;
    margin-right: auto;
  }
  
  .hexagon {
    margin-top: auto;
    margin-bottom: auto;
    margin-left: 7vh;
    margin-right: 7vh;
    position: relative;
    width: 12vh;
    height: 20vh;
    background-color: transparent;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #000; /* Add a border to the hexagon */
    transition: transform 0.3s ease-in-out; /* Add a hover effect */
  }
  
  
  .hexagon:hover {
    transform: scale(1.05); /* Enlarge the hexagon on hover */
  }
  
  .hex_title {
    color: white;
    text-align: center;
    font-size: 1.5rem;
  }
  </style>
  
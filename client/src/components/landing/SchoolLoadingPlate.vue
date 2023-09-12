<template>
    <a href="/">
      <div class="school">
        <img src="@/assets/school.png" alt="" class="img_title">

        <div class="school_content">
          <div class="loading-spinner">
            <div class="line-base"><div class="line"></div></div>
            <div class="line-base"><div class="line"></div></div>
            <div class="line-base"><div class="line"></div></div>
          </div>
        </div>

      </div>
    </a>
  </template>
  
  <script>
  export default {
    name: 'SchoolLoadingPlate'
  };
  </script>
  
  <style scoped>
 .school {
    width: 80vh;
    height: 20vh;
    background: linear-gradient(to right, #0466c263, #6b5b95);
    margin: 1vh auto; /* Adjust margin for top and bottom spacing */
    border-radius: 3vh;
    display: flex;
    flex-direction: row;
    align-items: center; /* Center vertically */
  }
  
  .img_title {
    width: 20vh;
    height: 20vh;
    margin-right: 2vh; /* Add margin between the image and text */
  }
  
  .school_content {
    display: flex;
    flex-direction: column;
    height: fit-content;
  }
  
  .school_title {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 2vh;
    font-weight: 500;
    color: white;
    margin: 0; /* Reset margin to remove extra spacing */
  }
  
  .info_box {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-size: 1.5vh;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.753);
    margin: 0; /* Reset margin to remove extra spacing */
  }

  a {
    text-decoration: none;
  }
  .school {
    position: relative;
  }
  
  .loading-spinner {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin-left: 22vh;
    background-color: rgba(255, 255, 255, 0.8);
  }
  
  .line-base {
    height: 20px;
    width: 40vh;
    background: #E0E0EB;
    border-radius: 25px;
    margin: 5px 0;
  }
  
  .line {
    height: 20px;
    width: 6vh;
    background: blue;
    border-radius: 25px;
    animation: slide 2.5s linear infinite;
  }
  
  @keyframes slide {
    0% {
      transform: translateX(0px);
      background-color: rgba(0, 0, 255, 0.712);
      width: 100px;
    }
  
    25% {
      transform: translateX(200px);
      background-color: #b55bf5b2;
      width: 150px;
    }
  
    50% {
      transform: translateX(400px);
      background-color: #f33879a2;
      width: 100px;
    }
  
    75% {
      transform: translateX(200px);
      background-color: #b55bf59f;
      width: 150px;
    }
  
    100% {
      transform: translateX(0px);
      background-color: rgba(0, 0, 255, 0.658);
      width: 100px;
    }
  }


  @media only screen and (max-width: 767px) {
    .school {
      flex-direction: column;
      width: 100%; /* Ширина 100% на мобильных устройствах */
      height: 20vh; /* Высота автоматически подстраивается */
      flex-direction: column; /* Элементы столбцом */
    }

    .img_title {
      width: 30%; /* Уменьшаем ширину изображения */
      height: auto; /* Высота автоматически подстраивается */
      margin-top: auto;
      margin-bottom: auto;
    }

    .loading-spinner {
      margin-left: 0vh;
      background-color: rgba(255, 255, 255, 0.8);
    }



    @keyframes slide {
      0% {
        transform: translateX(0px);
        background-color: rgba(0, 0, 255, 0.712);
        width: 100px;
      }
  
      25% {
        transform: translateX(100px);
        background-color: #b55bf5b2;
        width: 150px;
      }
  
      50% {
        transform: translateX(200px);
        background-color: #f33879a2;
        width: 100px;
      }
  
      75% {
        transform: translateX(100px);
        background-color: #b55bf59f;
        width: 150px;
      }
  
      100% {
        transform: translateX(0px);
        background-color: rgba(0, 0, 255, 0.658);
        width: 100px;
      }
    }
  }
  </style>
  
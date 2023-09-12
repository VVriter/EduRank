<template>
    
    <div class="school">
        <img src="@/assets/school.png" alt="" class="img_title">
        <div class="school_content">
            <p class="school_title">{{ data.short_name }}</p>
            <div class="info_boxes">
                <p class="info_box">📍 Адреса: {{ data.address }}</p>
                <p class="info_box">📞 Телефон: {{ data.phone }}</p>
                <p class="info_box">👩‍🏫 Директор: {{ data.boss }}</p>
                <p class="info_box" v-if="data.approved_count">👨‍🎓 Учнів: {{ data.approved_count }}</p>
                <p class="info_box" v-if="data.email">💬 Е-пошта: {{ data.email }}</p>
                <p class="info_box" v-if="data.state_name">📰 Статус: {{ data.state_name }}</p>
            </div>
        </div>
    </div>
    
</template>

<script>
    export default {
        name: 'SchoolInfoPlate',
        props: {
            data: {
                requiered: true
            }
        }
    }
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


  @media only screen and (max-width: 1000px) {
    .school {
      width: 80%;
      height: auto;
      flex-direction: column;
      align-items: center; /* Center vertically */
    }

    .school_title {
      text-align: center;
    }

    .info_boxes {
      margin-top: 1vh;
      margin-bottom: 1vh;
      margin-left: 1vh;
      margin-right: 1vh;
      width: fit-content;
      width: 100%;
    }

    .info_box {
        text-align: center;
        margin-right: 2vh;
    }
  }
</style>
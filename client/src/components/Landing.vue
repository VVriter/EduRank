<template>
    <div class="content">
      <img src="@/assets/logo.png" alt="" class="logo">
      <p class="search_logo">Знайди свою школу та залиш відгук!</p>
      <div class="search-container">
        <input
          type="text"
          class="search_bar"
          v-model="inputText"
          @input="updateSearchResults"
          placeholder="Пошук школи"
        >
        <span class="search-icon">&#128269;</span>
      </div>

        <!-- Анімація для знайдених шкіл -->
        <transition-group name="school-fade" tag="div">
            <SchoolPlate v-for="school in schools" :data="school"/>
        </transition-group>
  
      <div class="nothing_found" v-if="notFound">
        <img src="@/assets/robot.gif" alt="">
        <p>Наші роботи нічого не знайшли :()</p>
      </div>
  
      <div v-if="inputText == ''" class="recommended">
        <!-- Add recommended content here -->
      </div>

      <footer>
        <p>Цей додаток був розроблений Романом Новохатьком. Телеграм: @dazed68</p>
      </footer>
    </div>
  </template>
  
  <script>
    import SchoolPlate from '@/components/sub/SchoolPlate.vue'

    export default {
        name: 'Landing',
        components: {
            SchoolPlate
        },
        data() {
          return {
              inputText: null,
              schools: [],
              notFound: false
          }
        },
        methods: {
          updateSearchResults() {
              this.notFound = false;
              this.schools = [];
              fetch(`http://127.0.0.1:5000/api/search?query=${this.inputText}`, { method: 'GET' })
              .then(response => response.json())
              .then(data => {
                  this.schools = data;
                  if (this.schools.length < 1) {
                  this.notFound = true;
                  }
              })
              .catch(error => {
                  console.error('Error fetching data:', error);
              });
          }
        }
    }
  </script>
  
  <style scoped>
  .content {
    display: flex;
    flex-direction: column;
    align-items: center; /* Center all content horizontally */
  }
  
  .logo {
    width: 40vh;
    border-radius: 50%;
    margin-top: 5vh;
  }
  
  .search_logo {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-weight: 900;
    font-size: 3vh;
    text-align: center;
  }
  
  .search-container {
    display: flex;
    align-items: center;
    margin-top: 2vh; /* Add some spacing */
    background: linear-gradient(to bottom, #0466c2, #6b5b95);
    border-radius: 1vh;
    margin-bottom: 3vh;
  }
  
  .search_bar {
    width: 80vh;
    height: 3vh;
    border-radius: 1vh;
    padding: 1vh 2vh; /* Add some padding for better appearance */
    font-size: 2vh; /* Adjust font size */
    border: 2px solid #ccc; /* Add a border */
  }
  
  .search-icon {
    font-size: 2.5vh; /* Adjust icon size */
    margin-left: 1vh;
    margin-right: 1vh;
    cursor: pointer; /* Change cursor to pointer for better UX */
  }
  
  .nothing_found {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    margin-top: 3vh;
  }
  
  .nothing_found img {
    border-radius: 50%;
    width: fit-content;
    margin: 0 auto; /* Center horizontally */
  }
  
  .nothing_found p {
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
    font-weight: 900;
    font-size: 3vh;
    margin: 1rem auto; /* Center horizontally and add some top margin */
  }
  
  /* Add styles for recommended content if needed */
  .recommended {
    /* Your recommended content styles here */
  }

    /* Додайте стилі для анімації переходу */
    .school-fade-enter-active, .school-fade-leave-active {
        transition: opacity 0.1s;
    }
    .school-fade-enter, .school-fade-leave-to {
        opacity: 0;
    }


    footer {
        position: relative;
        bottom: 0;
        width: 100%; /* Зробіть футер на весь ширину вікна */
        padding: 1rem; /* Додайте внутрішні відступи за потреби */
        text-align: center;
    }

    footer p {
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        font-weight: 900;
        font-size: 2vh;
        margin: 0; /* Видаліть зовнішні відступи, щоб футер був відцентрованим */
        color: black; /* Приклад кольору тексту */
    }

  </style>
  
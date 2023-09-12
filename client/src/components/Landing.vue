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
        <span class="search-icon" @click="updateSearchResults">&#128269;</span>
      </div>

      <transition-group name="school-fade" tag="div">
          <SchoolPlate v-for="school in schools" :data="school"/>
      </transition-group>

      <transition-group name="school-fade" tag="div">
        <NotFound v-if="notFound"/>
      </transition-group>

      <transition-group name="school-fade" tag="div">
        <LoadingSchoolPlate v-if="isTimeouted" v-for="i in itterators"/>
      </transition-group>
    </div>
</template>
  
<script>
    import SchoolPlate from '@/components/sub/SchoolPlate.vue'
    import LoadingSchoolPlate from '@/components/sub/LoadingSchoolPlate.vue'
    import NotFound from './sub/NotFound.vue'

    export default {
        name: 'Landing',
        components: {
            SchoolPlate,
            LoadingSchoolPlate,
            NotFound
        },
        data() {
          return {
              inputText: null,
              schools: [],
              notFound: false,
              isTimeouted: null,
              itterators: [1,2,3,4,5,6]
          }
        },
        mounted() {
          this.updateSearchResults()
        },
        methods: {
          updateSearchResults() {
            if (this.inputText == '' || this.inputText == null) {
              this.inputText = null
              this.schools = []
              this.notFound = false
              return
            }

            this.notFound = false;
            this.schools = [];
            this.isTimeouted = true

            // Устанавливаем таймаут в 1 секунду
            const searchTimeout = setTimeout(() => {
              // Выполняем поисковый запрос только после завершения таймаута
              fetch(`http://127.0.0.1:5000/api/search?query=${this.inputText}`, { method: 'GET' })
                .then(response => response.json())
                .then(data => {
                  this.schools = data;
                  this.isTimeouted = false 
                  if (this.schools.length < 1) {
                    this.notFound = true;
                  }
                })
                .catch(error => {
                  console.error('Error fetching data:', error);
                });
            }, 500); 

            if (this.searchTimeout) {
              clearTimeout(this.searchTimeout);
            }

            this.searchTimeout = searchTimeout;
          }
        }

    }
</script>
  
<style scoped>

  .content {
    display: flex;
    flex-direction: column;
    align-items: center; /* Center all content horizontally */
    position: relative;
    padding-bottom: 4rem;
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

    .school-fade-enter-active, .school-fade-leave-active {
        transition: opacity 0.3s;
    }
    .school-fade-enter, .school-fade-leave-to {
        opacity: 0;
    }

    @media only screen and (max-width: 1000px) {
        .logo {
          width: 20vh;
        }

        .search_bar {
          width: 70%;
          height: 3vh;
          border-radius: 1vh;
          padding: 1vh 2vh; /* Add some padding for better appearance */
          font-size: 2vh; /* Adjust font size */
          border: 2px solid #ccc; /* Add a border */
        }
    }
</style>
  
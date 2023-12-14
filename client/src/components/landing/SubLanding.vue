<template>
    <div class="above">
        <div class="info-box" v-if="statistics">
            <div class="circles">
                <div class="ic1" id="ic1">
                    <p class="ic_title">Відгуки</p>
                    <p class="ic_sub_title">{{ statistics.reviews }}</p>
                </div>
                <div class="ic1" id="ic2">
                    <p class="ic_title">Користувачі</p>
                    <p class="ic_sub_title">{{ statistics.users }}</p>
                </div>
                <div class="ic1" id="ic3">
                    <p class="ic_title">Відвідувань</p>
                    <p class="ic_sub_title">{{ statistics.visiting }}</p>
                </div>
            </div>
        </div>
        <div class="circle-2">
            <img src="@/assets/astronout.png" alt="">
        </div>
    </div>
</template>

<script>

    export default {
        name: "SubLanding",
        data() {
            return {
                statistics: null
            }
        },
        async mounted() {
            const res = await fetch('/api/statistic')
            this.statistics = await res.json()
        }
    }

</script>

<style scoped>

    #ic1 {
        background: linear-gradient(to bottom, #b4cccb, #6b5b95);
    }

    #ic2 {
        background: linear-gradient(to bottom, #b4c0cc, #6b5b95);
    }

    #ic3 {
        background: linear-gradient(to bottom, #ccb4c6, #6b5b95);
    }

    .ic1 {
        z-index: 2;
        margin-left: 1.5vh;
        margin-right: 1.5vh;
        display: flex;
        flex-direction: column;
        width: 25vh;
        height: 25vh;
        background: linear-gradient(to bottom, #0466c2, #6b5b95);
        border-radius: 50%;
        align-items: center;
        -webkit-filter: drop-shadow(10px 3px 10px rgba(117, 1, 184, 0.7));
        filter: drop-shadow(0px 0px 3px rgba(117, 1, 184, 0.7));
    }

    .ic_title {
        color: white;
        font-size: 3vh;
        text-align: center;
        margin: 0;
       margin-top: 8vh;
    }

    .ic_sub_title {
        color: #e2d8f8;
        font-size: 2vh;
        margin: 0;
        text-align: center;
    }

    .circle-2 {
        width: 80vh;
        height: 80vh;
        background: linear-gradient(to bottom, #0466c2, #6b5b95);
        border-radius: 50%;
        position: absolute;
        right: 1vh;
        top: 50%; /* Adjusted from 'translate' */
        transform: translate(50%); /* Corrected 'translate' to 'transform' */
        overflow: visible;
        z-index: 1; /* To place it behind the text */
        -webkit-filter: drop-shadow(10px 3px 10px rgba(117, 1, 184, 0.7));
        filter: drop-shadow(0px 0px 3px rgba(117, 1, 184, 0.7));
        margin-top: 10vh;
    }

    .circle-2 img {
        width: 50vh;
        margin-top: 15vh;
        margin-right: 10vh;
        -webkit-filter: drop-shadow(10px 3px 10px rgba(117, 1, 184, 0.7));
        filter: drop-shadow(10px 3px 10px rgba(117, 1, 184, 0.7));
        transform: scaleX(-1); /* Flip horizontally */
        animation: bounce 10s infinite alternate;
    }

    @keyframes bounce {
        0% {
            translate: 0vh;
        }

        50% {
            translate: -5vh;
        }
    }

    @keyframes bounceup {
        0% {
            transform: translate(0, -5vh);
        }
    }



  .above {
    display: flex;
    flex-direction: column; /* Changed to 'column' to stack elements vertically */
    justify-content: center; /* Center align elements vertically */
    align-items: center; /* Center align elements horizontally */
  }



  .info-box {
    display: flex;
    flex-direction: row;
    margin-right: 40vh;
    margin-top: 40vh;
    background-color: #b5a7da;
    width: 100%;
    height: 40vh;
    -webkit-filter: drop-shadow(10px 3px 10px rgba(117, 1, 184, 0.7));
        filter: drop-shadow(10px 3px 10px rgba(117, 1, 184, 0.7));
  }

  .circles {
    display: flex;
    flex-direction: row;
    margin: auto;
  }

</style>
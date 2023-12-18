<template>
    <nav>
        <el-card style="border-radius: 10px;" :class="'desktop' + ' ' + minimizeded">
            <el-row>
                <svg style="width: 60px; border-radius: 50%; cursor: pointer;" @click="goto('Home')" width="45" height="40" viewBox="0 0 45 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9.7551 25.4298V16.5762C9.7551 16.1665 9.53633 15.7879 9.1813 15.5833C8.42931 15.15 8.41326 14.0704 9.15203 13.6149L21.1035 6.24571C22.0435 5.66616 23.2258 5.64981 24.1814 6.20316L40.6868 15.7608C41.4516 16.2036 42.4042 16.1606 43.126 15.6507C44.471 14.7004 44.3825 12.6774 42.9597 11.8482L24.1545 0.8886C23.2134 0.34013 22.0489 0.344865 21.1123 0.900969L2.34292 12.0451C0.385441 13.2073 0.384954 16.0408 2.34203 17.2037L3.55032 17.9217C4.44896 18.4557 5.00486 19.4189 5.01762 20.4641L5.11652 28.5699C5.12926 29.6142 5.68415 30.5767 6.58147 31.111L19.9883 39.0938C20.9272 39.6529 22.0958 39.6572 23.0388 39.1051L36.6789 31.1199C37.5983 30.5816 38.1633 29.5962 38.1633 28.5309V19.1435C38.1633 18.7468 38.3904 18.3851 38.7477 18.2129C39.502 17.8492 39.533 16.7864 38.8012 16.3794L36.78 15.2553C36.078 14.8649 35.2204 14.8816 34.5343 15.2992L22.9877 22.3266C22.0989 22.8675 20.9677 22.8008 20.1486 22.1591C19.5105 21.6592 19.1547 20.8807 19.1942 20.071L19.2009 19.9343C19.2449 19.0322 19.7271 18.2086 20.4922 17.7287L22.7849 16.2906C24.2697 15.3593 24.188 13.1695 22.6379 12.3515C21.9374 11.9817 21.095 12.003 20.414 12.4077L15.9806 15.042C15.0708 15.5826 14.5131 16.5627 14.5131 17.621V22.6954C14.5131 23.7377 15.0541 24.7053 15.9421 25.2512L19.979 27.7326C20.9217 28.3121 22.1068 28.3256 23.0624 27.7678L29.9888 23.7247C31.5651 22.8046 33.5452 23.9415 33.5452 25.7667C33.5452 26.5926 33.1143 27.3586 32.4084 27.7874L23.0864 33.451C22.1196 34.0383 20.9047 34.032 19.9442 33.4345L11.1706 27.9772C10.2903 27.4297 9.7551 26.4665 9.7551 25.4298Z" fill="var(--el-text-color-regular)"/>
                    <path d="M9.7551 25.4298V16.5762C9.7551 16.1665 9.53633 15.7879 9.1813 15.5833C8.42931 15.15 8.41326 14.0704 9.15203 13.6149L21.1035 6.24571C22.0435 5.66616 23.2258 5.64981 24.1814 6.20316L40.6868 15.7608C41.4516 16.2036 42.4042 16.1606 43.126 15.6507C44.471 14.7004 44.3825 12.6774 42.9597 11.8482L24.1545 0.8886C23.2134 0.34013 22.0489 0.344865 21.1123 0.900969L2.34292 12.0451C0.385441 13.2073 0.384954 16.0408 2.34203 17.2037L3.55032 17.9217C4.44896 18.4557 5.00486 19.4189 5.01762 20.4641L5.11652 28.5699C5.12926 29.6142 5.68415 30.5767 6.58147 31.111L19.9883 39.0938C20.9272 39.6529 22.0958 39.6572 23.0388 39.1051L36.6789 31.1199C37.5983 30.5816 38.1633 29.5962 38.1633 28.5309V19.1435C38.1633 18.7468 38.3904 18.3851 38.7477 18.2129C39.502 17.8492 39.533 16.7864 38.8012 16.3794L36.78 15.2553C36.078 14.8649 35.2204 14.8816 34.5343 15.2992L22.9877 22.3266C22.0989 22.8675 20.9677 22.8008 20.1486 22.1591C19.5105 21.6592 19.1547 20.8807 19.1942 20.071L19.2009 19.9343C19.2449 19.0322 19.7271 18.2086 20.4922 17.7287L22.7849 16.2906C24.2697 15.3593 24.188 13.1695 22.6379 12.3515C21.9374 11.9817 21.095 12.003 20.414 12.4077L15.9806 15.042C15.0708 15.5826 14.5131 16.5627 14.5131 17.621V22.6954C14.5131 23.7377 15.0541 24.7053 15.9421 25.2512L19.979 27.7326C20.9217 28.3121 22.1068 28.3256 23.0624 27.7678L29.9888 23.7247C31.5651 22.8046 33.5452 23.9415 33.5452 25.7667C33.5452 26.5926 33.1143 27.3586 32.4084 27.7874L23.0864 33.451C22.1196 34.0383 20.9047 34.032 19.9442 33.4345L11.1706 27.9772C10.2903 27.4297 9.7551 26.4665 9.7551 25.4298Z" fill="black" fill-opacity="0.2"/>
                </svg>


                <el-text @click="goto('Home')" style="margin-left: 10px; font-size: 30px; cursor: pointer;">Edu Rank</el-text>

                <el-row style="margin-left: auto; margin-top: auto; margin-bottom: auto;">
                    <ThemeSwitcher style="margin-right: 10px;" />
                    <el-button size="large" plain @click="goto('EJournal')">Є-Журнал</el-button>
                    <el-button size="large" plain @click="goto('Donate')">Донат</el-button>
                </el-row>
            </el-row>
        </el-card>

        <el-card style="border-radius: 10px; width: 90%;" class="mobile">
            <el-row style="display: flex; justify-content: center; align-items: center; width: 100%;">
                <el-button size="large" :icon="Search" circle plain />
                <el-button size="large" @click="goto('Home')" :icon="House" circle plain />
                <el-button size="large" :icon="Notebook" circle plain @click="goto('EJournal')" />
                <el-button size="large" @click="goto('Donate')" :icon="Money" circle plain />
            </el-row>
        </el-card>
    </nav>
</template>

<script setup>
    import { Search, Money, Notebook, House  } from '@element-plus/icons-vue';
    import ThemeSwitcher from './ThemeSwitcher.vue';
    import { ref, onMounted, computed } from 'vue'
    import { useRouter, useRoute } from 'vue-router'
    const router = useRouter()

    const minimized = ref(false)

    onMounted(() => {
        addEventListener("scroll", (event) => {
            var top = window.pageYOffset || document.documentElement.scrollTop
            if (top > 200) {
                minimized.value = true
            } else {
                minimized.value = false
            }
        })
    })

    const minimizeded = computed(() => {
        return minimized.value ? "min" : "full"
    })

    function goto(name) {
        router.push({name: name})
    }

</script>

<style scoped>
nav {
    z-index: 1;
    width: 90%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 10px;
    transition: all 1s;
}

.full {
    width: 100%;
    transition: transform 0.5s ease-in-out;
    transform: translateY(0);
}

.min {
  width: 100%;
    transition: transform 0.5s ease-in-out;
    transform: translateY(-110%);
}

@media (max-width: 768px) {

    nav {
        position: fixed;
        bottom: 0;
    }

    .desktop {
        display: none;
    }

    .mobile {
        display: block;
    }
}

@media (min-width: 769px) {

    nav {
        position: fixed;
        top: 0;
    }

    .desktop {
        display: block;
    }
    .mobile {
        display: none;
    }
}</style>

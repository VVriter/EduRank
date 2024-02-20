<template>
  <main>
    <NavBar/>
    <router-view class="router"/>
    <Footer class="footer"/>
  </main>
  <container/>
</template>

<script setup>
  import { container } from "jenesius-vue-modal";
  import NavBar from '@/components/navbar/NavBar.vue';
  import Footer from '@/components/footer/Footer.vue'
  import { watch, onMounted, onUnmounted } from 'vue'

  import { useUiConfigStore } from './stores/uiThemeStore'
  const uiStore = useUiConfigStore()
  uiStore.applyTheme()

  import { useUserStore } from './stores/userStore';
  const userStore = useUserStore()
  userStore.updateUserInfo()


  watch(
    () => uiStore.isDarkModeOn,
    async (newValue, oldValue) => {
      uiStore.applyTheme()
      localStorage.setItem('isDark', uiStore.isDarkModeOn)
    }
  )
</script>

<style scoped>
  main {
      display: flex;
      flex-direction: column;
      width: 100%;
      align-items: center;
      justify-content: center;
  }

  .footer {
    width: 90%;
    padding: 20px 0;
    text-align: center;
    bottom: 0;
    left: 0;
  }
  .router {
    margin-top: 0px;
  }

  @media (min-width: 769px) {
    .router {
        margin-top: 110px;
    }
  }
</style>

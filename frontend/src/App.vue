<template>
  <main>
    <NavBar/>
    <router-view class="router"/>
  </main>
</template>

<script setup>
  import NavBar from './components/navbar/NavBar.vue';
  import { watch } from 'vue'

  import { useUiConfigStore } from './stores/uiThemeStore'
  const uiStore = useUiConfigStore()
  uiStore.applyTheme()


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

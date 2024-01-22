<template>
    <el-button 
    @click="toogle"
    size="large"
    circle
    :icon="uiConfigStore.isDarkModeOn ? Sunny : Moon"/>
</template>

<script setup>
  import { useUiConfigStore } from '../../stores/uiThemeStore';
  import { Sunny, Moon } from '@element-plus/icons-vue'

  const uiConfigStore = useUiConfigStore()

  function toogle() {
    uiConfigStore.isDarkModeOn = !uiConfigStore.isDarkModeOn
  }
</script>

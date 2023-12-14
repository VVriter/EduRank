<template>
    <el-switch 
    v-model="uiConfigStore.isDarkModeOn" 
    inline-prompt size="large" 
    active-color="#1d1e1f" 
    border-color="gray"
    :active-icon="Sunny" 
    :inactive-icon="Moon" />
</template>

<script setup>
  import { useUiConfigStore } from '../../stores/uiThemeStore';
  import { Sunny, Moon } from '@element-plus/icons-vue'

  const uiConfigStore = useUiConfigStore()
</script>

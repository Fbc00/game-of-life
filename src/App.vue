<template>
  <div id="app">
    <main-tabuleiro />
  </div>
</template>

<script>
import  mainTabuleiro from './components/mainTabuleiro.vue'

export default {
  name: 'App',
  components: {
    mainTabuleiro
  }
}
</script>

<style>
body, html {
  margin: 0;
  padding: 0;
  height: 100%; 
  
}
</style>

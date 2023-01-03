<template>
  <div class="main-tabuleiro">
      <capsula-mini 
        v-for="x in valeu" :key="x" 
        :id="x"
      />  
  </div>
</template>

<script>
import CapsulaMini from './CapsulaMini';
import eventBus from '../EventBus'
export default {
  name: 'main-tabuleiro',
  components: {
    CapsulaMini
  },
  data() { 
    return {
      valeu: 800,
      medida: 0,
      id: null,
      ih: 0,
      copyMatriz: [],
      matriz:[[0,0,20], [58,0,60], [0 ,99,100]],
    }
  },
  watch: {
    ih() {
      this.log()
    }
  },
  mounted () {
    this.log()
    this.medida = Math.floor(window.innerWidth / 47)
  },
  methods : {
   log () {
      this.matriz.forEach((element, id) => {
        element.forEach((elZinho, indice) => {
          if(elZinho != 0) {
            this.copyMatriz.push(elZinho)
            setTimeout(() => {
              eventBus.changeClass(elZinho)
              this.matriz[id][indice] += this.medida
            }, 2000);
            } 
        })
      })
    setTimeout(() => { 
       for (const iterator of this.copyMatriz) {
          eventBus.$emit('removeclasse', iterator)
       }
      this.ih++
      this.copyMatriz = []
    }, 3000)
  
    },
  }
}
</script>

<style scoped>
.main-tabuleiro {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: 100%;
  background-color: black;

}

</style>

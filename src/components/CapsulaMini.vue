<template>
    <div class="capsulaMini" :class="{azul: this.class}" >

    </div>
</template>

<script>
import eventBus from '../EventBus'
export default {
    data () {
        return {
            class: false,
        }
    },
    props: ['id'],
    mounted () {
       eventBus.escutaChangeClass(this.id, this)
       eventBus.$on('removeclasse', (e) => {
        if (e === this.id) {
            this.class = false
        }
  
       })
    }
}
</script>

<style scoped>
.capsulaMini {
    width: 45px;
    height: 45px;
    border: 1px solid rgb(168, 145, 142);
}
.azul {
  background-color: aqua;
}
</style>
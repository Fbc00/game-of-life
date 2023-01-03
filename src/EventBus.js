import Vue from 'vue'

const vm = new Vue({
    methods: {
        changeClass(data) {
            this.$emit("changeClasse", data)
        },
        escutaChangeClass(id, master) {
            this.$on("changeClasse", (e) => {
                if (id === e) {
                    master.class = true
                }
            })
        }
    }
})

export default vm
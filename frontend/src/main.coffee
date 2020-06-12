import Vue from 'vue'
import App from './App.vue'
import router from '../router'
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.config.productionTip = false

app = new Vue
  el: "#app"
  router: router
  render: (h) -> h(App)
.$mount('#app')
import Vue from 'vue'
import App from './App.vue'
import router from '../router'
import store from './store/index'
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.config.productionTip = false

app = new Vue
  el: "#app"
  router: router
  store: store
  render: (h) -> h(App)
.$mount('#app')
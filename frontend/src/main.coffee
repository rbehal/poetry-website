import Vue from 'vue'
import App from './App.vue'
import router from '../router'
import VueAnalytics from 'vue-analytics';
import store from './store/index'
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(VueAnalytics, {id: 'UA-172425045-1', router})
Vue.config.productionTip = false

app = new Vue
  el: "#app"
  router: router
  store: store
  render: (h) -> h(App)
.$mount('#app')
import Vue from 'vue'
import App from './App'
import router from './router'
import './assets/bootstrap-3.3.7-dist/css/bootstrap.min.css'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

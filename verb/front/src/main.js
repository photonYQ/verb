import Vue from 'vue'
import store from './store'
import router from './router'
import App from './App'
import './assets/bootstrap-3.3.7-dist/css/bootstrap.min.css'


new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})

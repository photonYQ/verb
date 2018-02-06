import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: home
    },
    {
      path: '/home',
      name: 'Home',
      component: home
    }
  ]
})

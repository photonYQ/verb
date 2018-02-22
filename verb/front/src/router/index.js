import Vue from 'vue'
import Router from 'vue-router'
const Blog = () => import('@/components/Blog')

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'blog',
      component: Blog,
    }
  ]
})

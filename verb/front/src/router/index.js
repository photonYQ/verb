import Vue from 'vue'
import Router from 'vue-router'
const Blog = () => import('@/components/Blog')
const Post = () => import('@/components/Post')

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'blog',
      component: Blog,
    },
    {
      path: '/post/:pid',
      name: 'post',
      component: Post,
    }
  ]
})

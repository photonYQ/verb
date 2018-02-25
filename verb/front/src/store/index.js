import Vue from 'vue'
import Vuex from 'vuex'
import tagList from './modules/taglist'
import postList from './modules/postlist'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    tagList,
    postList,
  },
})

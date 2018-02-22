import Vue from 'vue'
import Vuex from 'vuex'
import tagList from './modules/taglist'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    tagList,
  },
})

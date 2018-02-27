import Vue from 'vue'
import Vuex from 'vuex'
import tagList from './modules/taglist'
import postList from './modules/postlist'
import tagDetail from './modules/tagdetail'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    tagList,
    postList,
    tagDetail,
  },
})

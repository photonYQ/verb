import api from '@/api'
import {
  GET_POST_LIST_SUCCESS,
  GET_POST_LIST_FAILURE
} from "../types";

const state = {
  items: []
}

const actions = {
  getPostList({commit}) {
    api.getPostList().then(response => {
      if (!response.ok) {
        return commit(GET_POST_LIST_FAILURE)
      }
      commit(GET_POST_LIST_SUCCESS, { postList: response.data.results })
    })
  }
}

const mutations = {
  [GET_POST_LIST_FAILURE](state){
    state.items=[]
  },
  [GET_POST_LIST_SUCCESS](state, action){
    state.items = action.postList
  }
}

export default {
  state,
  actions,
  mutations
}

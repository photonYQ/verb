import api from '@/api'
import {
  GET_POST_LIST_SUCCESS,
  GET_POST_LIST_FAILURE
} from "../types";

const state = {
  items: [],
  currentPage: 1,
  nextPage: null,
  prevPage: null
}

const actions = {
  getPostList({commit}, {tagId, page}) {
    api.getPostList(tagId, page).then(response => {
      if (!response.ok) {
        return commit(GET_POST_LIST_FAILURE)
      }
      commit(GET_POST_LIST_SUCCESS, { postList: response.data, currentPage: page })
    })
  }
}

const mutations = {
  [GET_POST_LIST_FAILURE](state){
    state.currentPage = 1
    state.items = []
    state.nextPage = null
    state.prevPage = null
  },
  [GET_POST_LIST_SUCCESS](state, action){
    state.currentPage = action.currentPage
    state.items = action.postList.results
    state.nextPage = action.postList.next
    state.prevPage = action.postList.previous
  }
}

export default {
  state,
  actions,
  mutations
}

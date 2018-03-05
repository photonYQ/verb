import api from '@/api'
import {
  GET_POST_SUCCESS,
  GET_POST_FAILURE
} from "../types";

const state = {
  item: {}
}

const actions = {
  getPost({commit}, {id}) {
    api.getPost(id).then(response => {
      if(response.ok){
        commit(GET_POST_SUCCESS, {
          post: {...response.data}
        })
      } else {
        commit(GET_POST_FAILURE)
      }
    })
  }
}

const mutations = {
  [GET_POST_FAILURE](state) {
    state.item = {}
  },
  [GET_POST_SUCCESS](state, action) {
    state.item = {...state.item, ...action.post}
  }
}

export default {
  state,
  actions,
  mutations,
}

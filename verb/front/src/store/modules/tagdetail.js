import api from '@/api'
import {
  GET_TAG_DETAIL_SUCCESS,
  GET_TAG_DETAIL_FAILURE
} from "../types"

const state = {
  tag:{}
}

const actions = {
  getTagDetail({commit}, {tagId}) {
    api.getTagList(tagId).then(response => {
      if(!response.ok) {
        return commit(GET_TAG_DETAIL_FAILURE)
      }
      commit(GET_TAG_DETAIL_SUCCESS, { tagDetail: response.data })
    })
  }
}

const mutations = {
  [GET_TAG_DETAIL_FAILURE](state){
    state.tag = {}
  },
  [GET_TAG_DETAIL_SUCCESS](state, action){
    state.tag = action.tagDetail
  }
}

export default {
  state,
  actions,
  mutations
}

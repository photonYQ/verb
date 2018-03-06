import api from '@/api'
import {
  POST_COMMENT_SUCCESS
} from "../types"

const actions = {
  postComment({commit}, {comment}) {
    api.postComment(comment)
  }
}

export default {
  actions,
}


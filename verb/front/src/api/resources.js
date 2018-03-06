import Vue from 'vue'
import VueResource from 'vue-resource'
import {API_ROOT} from "../config";


Vue.use(VueResource)


Vue.http.options.crossOrigin = true

export const PostResource = Vue.resource(API_ROOT + 'posts{/id}{controller}/')
export const TagResource = Vue.resource(API_ROOT + 'tags{/id}')
export const CommentResource = Vue.resource(API_ROOT + 'comments{/id}')


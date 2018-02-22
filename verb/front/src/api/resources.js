import Vue from 'vue'
import VueResource from 'vue-resource'
import {API_ROOT} from "../config";


Vue.use(VueResource)


Vue.http.options.crossOrigin = true

export const PostResource = Vue.resource(API_ROOT + 'posts/')
export const TagResource = Vue.resource(API_ROOT + 'tags/')


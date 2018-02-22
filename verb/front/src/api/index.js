import {PostResource, TagResource} from './resources'


export const getPostList = () => { return PostResource.get() }

export const getTagList = () => { return TagResource.get() }

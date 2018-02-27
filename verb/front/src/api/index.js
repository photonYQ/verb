import {PostResource, TagResource} from './resources'


export default {
  getPostList: () => { return PostResource.get() },

  getTagList: () => { return TagResource.get() },

  getTag: (tagId) => { return TagResource.get({id: tagId})}
}

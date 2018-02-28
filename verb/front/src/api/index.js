import {PostResource, TagResource} from './resources'


export default {
  getPostList: (tagId) => { if (tagId) {return PostResource.get({'tag_id':tagId})} else {return PostResource.get()} },

  getTagList: () => { return TagResource.get() },
}

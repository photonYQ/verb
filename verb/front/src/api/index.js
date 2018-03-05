import {PostResource, TagResource} from './resources'


export default {
  getPostList: (tagId, page) => {
    if (tagId) {
      return PostResource.get({'tag_id':tagId, 'page':page})
    }
    else {
      return PostResource.get({'page':page})
    }
  },

  getTagList: () => { return TagResource.get() },

  getPost: (pid) => { return PostResource.get({'id':pid})}
}

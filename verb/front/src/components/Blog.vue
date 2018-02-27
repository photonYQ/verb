<template>
  <div class="container">
    <div class="row">
      <main class="col-md-8">
        <Postlist :post-list="postList"></Postlist>
      </main>
      <aside class="col-md-4">
        <Tagcloud :tag-list="tagList"></Tagcloud>
      </aside>
    </div>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'
  import Postlist from './Postlist'
  import Tagcloud from './Tagcloud'
  export default {
    components: { Postlist, Tagcloud },
    computed: {
      ...mapState({
        tagList: ({tagList}) => tagList.items,
        postList: ({postList}) => postList.items,
        tagDetail: ({tagDetail}) => tagDetail.tag,
      })
    },
    created() {
      this.getTagList()
      this.getPostList()
    },
    methods: {
      ...mapActions([
        'getTagList',
        'getPostList',
      ]),
      handleChange(tagId) {
        this.getTagDetail({"tagId":tagId})
      }
    }
  }
</script>

<style scoped>

</style>

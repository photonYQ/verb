<template>
  <div class="container">
    <div class="row">
      <main class="col-md-8">
        <Postlist :post-list="postList" :prev-page="prevPage" :next-page="nextPage"></Postlist>
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
        prevPage: ({postList}) => postList.prevPage,
        nextPage: ({postList}) => postList.nextPage,
      })
    },
    created() {
      this.getTagList()
      this.getPostList({"tagId":null, "page":1})
    },
    methods: {
      ...mapActions([
        'getTagList',
        'getPostList',
      ]),
      handleChange(tagId) {
        this.getPostList({"tagId":tagId, "page":1})
      }
    }
  }
</script>

<style scoped>

</style>

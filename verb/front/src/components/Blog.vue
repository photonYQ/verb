<template>
  <div class="content">
    <div class="col-md-8">
      <Postlist></Postlist>
    </div>
    <div class="col-md-4 col-md-offset-8">
      <Tagcloud :tag-list="tagList"></Tagcloud>
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
      })
    },
    created() {
      this.getTagList()
    },
    methods: {
      ...mapActions([
        'getTagList',
      ])
    }
  }
</script>

<style scoped>

</style>

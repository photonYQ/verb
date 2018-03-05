<template>
  <div class="container">
    <div class="row">
      <div class="col-md-10 col-md-offset-1">
        <div class="post">
          <div class="post-title">
            <h1>{{ post.title }}</h1>
            <div class="create-info">
              <span class="label label-default">
                {{ post.create_time }}
              </span>
              <span v-for="tag in post.tags" class="label label-info">
                {{ tag }}
              </span>
            </div>
            <div class="view-info">
              <span class="label label-primary">
                浏览 {{ post.num_views }}
              </span>
              <span class="label label-success">
                评论 {{ post.num_comments }}
              </span>
            </div>
          </div>
          <hr>
          <div class="post-content">
            {{ post.content }}
            <p>博文最后更新于:  {{ post.update_time }}</p>
          </div>
          <hr>
          <div class="post-comments">
            <h4>评论区</h4>
            <ul>
              <li v-if="post.comments!=[]">暂无评论</li>
              <li v-for="comment in post.comments">
                {{ comment.nick_name }}<{{ comment.email }}>回复{{ comment.reply }}<br>
                {{ comment.content }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapState, mapActions } from 'vuex'

  export default {
    computed: {
      ...mapState({
        post: ({post}) => post.item,
        pid: ({route}) => route.params.pid
      })
    },
    created () {
      const pid = this.$route.params.pid
      this.getPost({"id":pid})
    },
    methods: {
      ...mapActions([
        'getPost',
      ]),
    }
  }
</script>

<style scoped>
  .post {
    background: #fff;
    padding: 20px 100px;
  }
  .post-title {
    height: 60px;
  }
  .post .create-info {
    float: left;
  }
  .post .view-info {
    float: right;
  }
</style>

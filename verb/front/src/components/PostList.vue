<template>
  <div>
    <div class="post-info" v-for="post in postList">
      <h3>{{ post.title }}</h3>
      <div class="base-info">
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
      <div class="post-summary">
        <p>{{ post.summary }}</p>
      </div>
    </div>
    <nav aria-label="Page navigation">
      <ul class="pagination">
        <li>
          <a href="#" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li><a href="#">1</a></li>
        <li>
          <a href="#" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
  export default {
    props: ['postList', ]
  }
</script>

<style scoped>
  .post-info {
   background: #fff;
   padding: 20px 20px;
   margin-bottom: 20px;
  }
  span {
    margin-right: 5px;
  }
  .base-info {
    height: 35px;
  }
  .create-info {
    float: left;
  }
  .view-info {
    float: right;
  }
  nav {
    text-align: center;
  }

</style>

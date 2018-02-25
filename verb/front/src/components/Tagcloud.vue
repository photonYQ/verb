<template>
  <div class="widget">
    <h4>标签云</h4>
    <p>标签个数 <span class="badge">{{tagList.length}}</span></p>
    <p v-for="tag in tagList">
      {{ tag.name }} <span class="badge">共{{tag.num_posts}}篇</span>
    </p>
  </div>
</template>

<script>
  export default {
    props: ['tagList',]
  }
</script>

<style scoped>
  .widget {
    background: #fff;
    padding: 20px 20px;
  }
</style>

<template>
  <div>
    <h1>{{ list.count }}</h1>
  </div>
</template>

<script>
  import {getPostList, } from '../api/index';
    export default {
      name: "post-list",
      data() {
        return {
          list: {}
        }
      },
      methods: {
        getList() {
          getPostList().then((response)=> {
            this.list = response.data
          })
        }
      },
      created() {
        this.getList();
      }
    }
</script>

<style scoped>

</style>

<template>
  <div id="home">
    <xheader></xheader>

    <xfooter></xfooter>
  </div>
</template>

<script>
  import xheader from './Header';
  import xfooter from './Footer';
  import {getPostList, } from '../api/index';

  export default {
    name: "home",
    components: {
      xheader, xfooter
    },
    data() {
      return {
        list: []
      }
    },
    methods: {
      getList() {
        getPostList().then((response)=> {
          console.log(response)
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

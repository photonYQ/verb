<template>
  <div id="home">
    <navbar></navbar>
    <router-view></router-view>
    <footer></footer>
  </div>
</template>

<script>
  import navbar from './Navbar';
  import footer from './Footer';

  export default {
    name: "home",
    components: {
      navbar, footer
    }
  }

</script>

<style scoped>

</style>

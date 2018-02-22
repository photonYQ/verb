<template>
  <div>
    <Navbar></Navbar>
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>

<script>
  import store from 'store'
  import Navbar from './components/Navbar'
  import Footer from './components/Footer'
  export default {
    store,
    name: 'App',
    components: {Navbar, Blog, Footer}
  }
</script>

<style>

</style>

<template>
  <div>
    <Navbar></Navbar>
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>

<script>
  import Navbar from './components/Navbar'
  import Footer from './components/Footer'
  export default {
    name: 'App',
    components: {Navbar, Footer}
  }
</script>

<style>

</style>

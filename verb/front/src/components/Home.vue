<template>
  <div id="home">
    <xheader></xheader>
    <xfooter></xfooter>
  </div>
</template>

<script>
  import xheader from './Header';
  import xfooter from './Footer'

  export default {
    name: "home",
    components: {
      xheader, xfooter
    }
  }
</script>

<style scoped>

</style>

<template>
  <header class="main-header">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <a class="branding" href="#"><h1>Verb 开源博客框架</h1></a>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
  import banner from "@/assets/banner.jpg"
  export default {
    name: "xheader",
    data(){
      return {
        bannerUrl: banner
      }
    }
  }
</script>

<style scoped>
.main-header {
  text-align: center;
  padding: 42px 0;
  background: #ffffff;
}
  .main-header .branding {
    font-size: 3.5em;
    color: #303030;
  }
</style>

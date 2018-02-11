<template>
  <header class="main-header">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <a class="branding" href="#"><h1>Verb 开源博客框架</h1></a>
        </div>
      </div>
    </div>
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <ul class="nav navbar-nav">
          <li class="active"><router-link to="/posts">主页 <span class="sr-only">(current)</span></router-link></li>
          <li><a href="#">关于</a></li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
  import banner from "@/assets/banner.jpg"
  export default {
    name: "navbar",
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

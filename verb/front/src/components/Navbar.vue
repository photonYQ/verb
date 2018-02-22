<template>
  <header class="main-header">
    <div class="banner">
      <a href="#"><h1>Verb Blog</h1></a>
    </div>
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <ul class="nav navbar-nav">
          <li class="active"><router-link to="/">主页 <span class="sr-only">(current)</span></router-link></li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
  export default {}
</script>

<style scoped>
.main-header {
  text-align: center;
  padding: 42px 0;
  background: #ffffff;
}
.main-header .banner {
  text-align: left;
  color: #303030;
}
</style>

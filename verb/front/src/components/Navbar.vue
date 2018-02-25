<template>
  <div>
    <header class="main-header" style="background-image: url(http://image.golaravel.com/5/c9/44e1c4e50d55159c65da6a41bc07e.jpg)">
      <div class="container">
        <div class="row">
          <div class="col-xs-12">
            <h1>Verb Blog <small style="color: #fff"> A framework based on vue and django.</small></h1>
          </div>
        </div>
      </div>
    </header>
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#main-menu" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
        <div class="collapse navbar-collapse" id="main-menu" aria-expanded="false">
          <ul class="nav navbar-nav">
            <li><router-link to="/">主页</router-link></li>
            <li><router-link to="/">关于</router-link></li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
  export default {}
</script>

<style scoped>
  .main-header {
    padding: 42px 0;
    color: #fff;
    background-position-x: center;
    background-position-y: 20%;
    background-size: cover;
  }
  nav {
    background: #fff;
  }
  #main-menu {
    font-size: 1.2em;
    padding-left: 100px;
  }
</style>

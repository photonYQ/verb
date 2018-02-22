<template>
  <ul>
    <li v-for="tag in tagList">
      <h1>{{ tag.name }}</h1>
    </li>
  </ul>
</template>

<script>
  export default {
    props: ['tagList',]
  }
</script>

<style scoped>

</style>

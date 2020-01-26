<template>
  <div class="header-container pure-u-1 pure-u-md-1-4">
    <div class="blog-header pure-u-1 pure-u-md-1-4">
    <div class="pure-menu custom-restricted-width">
      <ul class="pure-menu-list">
        <li class="pure-menu-item"><a href="#" class="pure-menu-heading pure-menu-link">Paweł Mstowski Blog</a></li>
        <li class="pure-menu-item"><a href="#" class="pure-menu-link">News</a></li>
        <li class="pure-menu-item"><a href="#" class="pure-menu-link">Sports</a></li>
        <li class="pure-menu-item"><a href="#" class="pure-menu-link">Finance</a></li>
      </ul>
    </div>
    </div>
  <div>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style>

@media(min-width: 48em){
  .blog-header {
    position: fixed
  }
}

.header-container {
  padding-top: 2em;
  padding-bottom: 2em;
  height: 100%;
}

.blog-header {
  border-right: solid 1px #ddd;
  height: 100%;
}

.custom-restricted-width {
    /* To limit the menu width to the content of the menu: */
    display: inline-block;
    /* Or set the width explicitly: */
    /* width: 10em; */
}
</style>

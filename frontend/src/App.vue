<template>
  <div id="app" class="pure-g">
    <Header></Header> 
    <div class="content pure-u-1 pure-u-lg-3-4">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Header from './components/core/Header';
import Home from './components/pages/Home'

export default {
  name: 'App',
  components: {
    Header,
    Home
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Lato&display=swap');
@import "./style/colors.scss";

.content {
  padding: 1em;
}

@media (min-width: 64em){
  .content {
      padding: 2em 3em 0;
      margin-left: 25%;
  }
}


body{
  background-color: $background-main-color;
  color: $font-normal-color;
  h1{
    color: $font-accent-color;
  }
}

body,
.pure-g [class *= "pure-u"],
.pure-g-r [class *= "pure-u"] {
    /* Set you're content font stack here: */
    font-family: lato;
}
</style>

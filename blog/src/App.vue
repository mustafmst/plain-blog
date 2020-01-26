<template>
  <div id="app" class="pure-g">
    <Header></Header> 
    <div class="content pure-u-1 pure-u-md-3-4">
      <Home></Home>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
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

<style>
@import url('https://fonts.googleapis.com/css?family=Lato&display=swap');

.content {
  padding: 1em;
}

@media (min-width: 48em){
  .content {
      padding: 2em 3em 0;
      margin-left: 25%;
  }
}


body{
  font-family: 'Lato', sans-serif;
}
</style>

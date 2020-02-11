<template>
  <div id="app" class="pure-g">
    <Header></Header>
    <div class="content pure-u-1 pure-u-lg-3-4">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Header from "./components/core/Header";
import Home from "./components/pages/Home";

export default {
  name: "App",
  components: {
    Header,
    Home
  }
};
</script>

<style lang="scss">
@import "./style/colors.scss";

body {
  /* Set you're content font stack here: */
  font-family: "lato";
  background-color: $background-main-color;
  color: $font-normal-color;
}
</style>

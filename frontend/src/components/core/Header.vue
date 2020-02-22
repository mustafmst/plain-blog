<template>
  <nav class="navbar navbar-expand-lg navbar-dark sticky-top">
    <router-link to="/" class="navbar-brand">
      <img src="../../../static/nav-logo.png" height="60px" >
      Trochę o kodzie
    </router-link>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <MenuItem
          v-for="item in menuItems"
          v-bind:to="item.to"
          v-bind:title="item.title"
          v-bind:key="item.id"
        ></MenuItem>
      </ul>
    </div>
  </nav>
</template>

<script>
import MenuItem from "./menu/MenuItem";

export default {
  name: "Header",
  components: {
    MenuItem
  },
  data() {
    return {
      menuItems: [
        {
          id: 0,
          title: "Blog",
          to: "/blog"
        },
        {
          id: 1,
          title: "Kontakt",
          to: "/info"
        }
      ]
    };
  }
};
</script>

<style lang='scss'>
@import "../../style/colors.scss";
.navbar{
  background-color: $accent-color;
  .navbar-brand{
    color: $font-accent-color;
    transition: color 0.5s;
    &:hover{
      color: $font-hover-color;
    }
    &:focus{
      color: $font-accent-color;
    }
  }
}
</style>

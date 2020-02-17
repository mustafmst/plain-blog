<template>
  <nav class="navbar navbar-expand-lg navbar-dark sticky-top">
    <router-link to="/" class="navbar-brand">/home/PawełMstowski</router-link>
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
          title: "Info",
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
}
</style>

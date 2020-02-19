<template>
  <li class="nav-item">
    <router-link v-bind:to="to" class="nav-link blog-nav-link">{{title}}</router-link>
  </li>
</template>

<script>
export default {
  name: "MenuItem",
  props: ["title", "to"]
};
</script>

<style lang="scss">
@import "./../../../style/colors.scss";
#app {
  .blog-nav-link {
    transition: color 0.5s;
    &:hover {
      color: $font-accent-color;
    }
    &:focus {
      color: $font-accent-color;
    }
  }
}
</style>
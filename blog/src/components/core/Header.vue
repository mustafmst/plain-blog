<template>
  <div class="header-container pure-u-1 pure-u-lg-1-4">
    <div class="pure-menu menu">
      <ul class="pure-menu-list">
        <li class="pure-menu-item"><router-link to="/" class="pure-menu-heading pure-menu-link">/dev/PawełMstowski</router-link></li>
        <MenuItem v-for="item in menuItems" v-bind:to="item.to" v-bind:title="item.title" v-bind:key="item.id"></MenuItem>
      </ul>
    </div>
  <div>
</template>

<script>
import MenuItem from './menu/MenuItem'

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
        },
      ]
    }
  }
}
</script>

<style lang='scss'>
@import "../../style/colors.scss";

@media(min-width: 64em){
  .header-container {
    position: fixed;
    border-right: solid 1px $accent-color;
  }
  .menu {
    margin-top: 15em;
  }
}

.header-container {
  height: 100%;
  text-align: right;
}


.menu {
  .pure-menu-link {
    color: $font-normal-color;
    &:hover{
      background-color: $accent-color;
    }
  }
  .router-link-exact-active {
    background-color: $background-main-color;
    color: $font-accent-color;
    &:after{
      content: " $"
    }
  }
}

.blog-header {
  border-right: solid 1px #ddd;
  height: 100%;
}
</style>

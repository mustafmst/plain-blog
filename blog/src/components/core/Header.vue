<template>
  <div class="header-container pure-u-1 pure-u-lg-1-4">
    <div class="pure-menu menu">
      <ul class="pure-menu-list">
        <li class="pure-menu-item"><a href="#" class="pure-menu-heading pure-menu-link">/dev/PawełMstowski</a></li>
        <MenuItem v-for="item in menuItems" v-bind:title="item.title" v-bind:key="item.id"></MenuItem>
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
          title: "Blog"
        },
        {
          id: 1,
          title: "Info"
        },
      ]
    }
  }
}
</script>

<style lang='scss'>

@media(min-width: 64em){
  .header-container {
    position: fixed;
    border-right: solid 1px #ddd;
  }
  .menu {
    margin-top: 15em;
    .pure-menu-item {
      &:hover{
        background-color: none;
      }
    }
  }
}

.header-container {
  height: 100%;
  text-align: right;
}

.blog-header {
  border-right: solid 1px #ddd;
  height: 100%;
}
</style>

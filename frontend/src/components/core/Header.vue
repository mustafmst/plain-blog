<template>
  <div class="header-container pure-u-1 pure-u-lg-1-4">
    <div class="pure-menu menu">
      <ul class="pure-menu-list">
        <li class="pure-menu-item"><router-link to="/" class="pure-menu-heading pure-menu-link">/home/PawełMstowski</router-link></li>
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
</style>

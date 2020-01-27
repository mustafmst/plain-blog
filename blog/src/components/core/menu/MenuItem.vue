<template>
  <li class="pure-menu-item"><router-link v-bind:to="to" class="pure-menu-link">~/{{title}}</router-link></li>
</template>

<script>
export default {
    name: "MenuItem",
    props: ['title','to']
}
</script>

<style>

</style>
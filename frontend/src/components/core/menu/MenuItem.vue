<template>
  <li class="nav-item"><router-link v-bind:to="to" class="nav-link">~/{{title}}</router-link></li>
</template>

<script>
export default {
    name: "MenuItem",
    props: ['title','to']
}
</script>

<style>

</style>
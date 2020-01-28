<template>
  <div>
    <h1>Blog Page</h1>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Blog",
   methods: {
     ...mapActions({
             fetchAllPosts: 'posts/fetchAllPosts'
     })
   },
  computed: mapGetters({
          posts: 'posts/allPosts'
  }),
  created() {
    this.fetchAllPosts()
  }
};
</script>

<style lang="scss">
</style>
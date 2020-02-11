<template>
  <div class="">
    <PostsList v-bind:posts="posts"></PostsList>
  </div>
</template>

<script>
import PostsList from "../core/postsList/PostsList";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Blog",
  components: {
    PostsList
  },
  methods: {
    ...mapActions({
      fetchAllPosts: "posts/fetchAllPosts"
    })
  },
  computed: {
    ...mapGetters({
      posts: "posts/allPosts"
    })
  },
  created() {
    this.fetchAllPosts();
  }
};
</script>

<style lang="scss">
</style>
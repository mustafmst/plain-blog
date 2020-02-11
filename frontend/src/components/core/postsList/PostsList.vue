<template>
  <div>
    <div class="posts-list row row-cols-1 row-cols-md-2">
      <PostsListItem v-for="post in posts" v-bind:key="post.id" v-bind:post="post"></PostsListItem>
    </div>
  </div>
</template>

<script>
import PostsListItem from "./PostsListItem";

export default {
  name: "PostsList",
  components: {
    PostsListItem
  },
  props: ["posts"]
};
</script>

<style lang="scss">
</style>
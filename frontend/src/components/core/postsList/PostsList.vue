<template>
  <div>
    <div class="posts-list row">
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
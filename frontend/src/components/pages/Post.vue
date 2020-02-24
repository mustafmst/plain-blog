<template>
  <div>
    <div v-if="post != null">
      <h1>{{post.title}}</h1>
      <div v-html="compiledContent"></div>
      <Comments v-bind:forPost="postId"></Comments>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import marked from "marked";
import Comments from "./../core/comments/Comments";

export default {
  name: "Post",
  components: {
    Comments
  },
  data: function() {
    return {
      postId: this.$route.params.id
    };
  },
  methods: {
    ...mapActions({
      getPost: "posts/fetchPost",
      clearPost: "posts/clearCurrentPost"
    })
  },
  computed: {
    ...mapGetters({
      post: "posts/currentPost"
    }),
    compiledContent: function() {
      return marked(this.post.content);
    }
  },
  created() {
    this.getPost(this.$route.params.id);
  },
  beforeRouteUpdate(to, from, next) {
    this.clearPost();
    if (to.params.id !== undefined || to.params.id !== null) {
      this.postId = to.params.id;
      this.getPost(to.params.id);
    }
    next();
  },
  destroyed() {
    this.clearPost();
  }
};
</script>

<style lang="scss">
</style>

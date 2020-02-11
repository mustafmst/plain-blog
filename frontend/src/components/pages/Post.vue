<template>
  <div>
    <div v-if="post != null">
      <h1>{{post.title}}</h1>
      <div class="" v-html="compiledContent"></div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import marked from "marked";

export default {
  name: "Post",
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
    if(to.params.id !== undefined || to.params.id !== null)
      this.getPost(to.params.id);
    next();
  },
  destroyed() {
    this.clearPost();
  }
};
</script>

<style lang="scss">
</style>
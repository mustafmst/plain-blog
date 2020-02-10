<template>
  <div>
    <div v-if="post != null">
      <h1>{{post.title}}</h1>
      <div class="post-content" v-html="compiledContent"></div>
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
@import '../../style/colors.scss';

.post-content {
  h1 tt,
  h1 code {
    font-size: inherit;
  }

  h2 tt,
  h2 code {
    font-size: inherit;
  }

  h3 tt,
  h3 code {
    font-size: inherit;
  }

  h4 tt,
  h4 code {
    font-size: inherit;
  }

  h5 tt,
  h5 code {
    font-size: inherit;
  }

  h6 tt,
  h6 code {
    font-size: inherit;
  }

  code,
  tt {
    margin: 0 2px;
    padding: 0 5px;
    white-space: nowrap;
    border: 1px solid $accent-color;
    background-color: $black;
    border-radius: 3px;
  }

  pre code {
    margin: 0;
    padding: 0;
    white-space: pre;
    border: none;
    background: transparent;
  }

  .highlight pre {
    background-color: #f8f8f8;
    border: 1px solid #cccccc;
    font-size: 13px;
    line-height: 19px;
    overflow: auto;
    padding: 6px 10px;
    border-radius: 3px;
  }

  pre {
    background-color: $black;
    border: 1px solid $accent-color;
    font-size: 13px;
    line-height: 19px;
    overflow: auto;
    padding: 6px 10px;
    border-radius: 3px;
  }
  pre code,
  pre tt {
    background-color: transparent;
    border: none;
  }
}
</style>
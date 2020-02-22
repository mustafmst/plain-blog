<template>
  <div>
    <div class="row home-content" v-if="homepage != undefined">
        <div class="col-12" v-html="homepage.content"></div>
    </div>
    <h3>Przypięte posty</h3>
    <PostsList v-bind:posts="pinned"></PostsList>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import PostsList from "../core/postsList/PostsList";

export default {
  name: "Home",
  components: {
    PostsList
  },
  methods: {
    ...mapActions({
      getContent: "posts/fetchHomepagePosts"
    })
  },
  computed: {
    ...mapGetters({
      homepage: "posts/getHomepage",
      pinned: "posts/getPinned"
    })
  },
  created() {
    this.getContent();
  }
};
</script>

<style lang="scss">
@import "./../../style/colors.scss";

.home-content {
  border-bottom: 1px solid $blue-gray-600;
  padding-bottom: 5em;
  margin-bottom: 5em;
}
</style>
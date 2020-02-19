<template>
  <div class="posts-list-item col-12">
    <router-link v-bind:to="postLink">
      <div class="card h-100">
        <div class="card-body">
          <h5 class="card-title">{{post.title}}</h5>
          <p class="card-text">{{post.content_short}}</p>
          <p class="card-text publication-date">
            <small class="text-muted">{{post.publication_date}}</small>
          </p>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "PostsListItem",
  props: ["post"],
  computed: {
    postLink: function() {
      return `/post/${this.post.id}`;
    }
  }
};
</script>

<style lang="scss">
@import "../../../style/colors.scss";


.posts-list-item {
    height: 100%;
  a {
    color: inherit;
    text-decoration: none;
  }
  margin-bottom: 1em;
  $shadow-move: 0.5em;
  .card {
    position: relative;
    background-color: $accent-color;
    display: flex;
    transition: opacity 0.4s;
    &:hover {
      opacity: 0.7;
    }
  }
  .card-body {
    height: 18em;
  }

  .post-card-date {
    text-align: right;
  }

  .publication-date {
    position: absolute;
    bottom: 1em;
    right: 1em;
  }
}
</style>

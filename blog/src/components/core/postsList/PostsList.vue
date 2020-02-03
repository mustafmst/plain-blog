<template>
  <div>
      <div class="posts-list">
          <ul>
              <li v-for="post in posts" v-bind:key="post.id">
                  <PostsListItem v-bind:post="post"></PostsListItem>
              </li>
          </ul>
      </div>
  </div>
</template>

<script>
import PostsListItem from './PostsListItem'


export default {
    name: 'PostsList',
    components: {
        PostsListItem
    },
    props: ['posts']
}
</script>

<style lang="scss">
@import '../../../style/colors.scss';

.posts-list {
    li {
        list-style-type: none;
        border-bottom: $blue-gray-600 solid 1px;
        padding-top: 3em;
    }
}
</style>
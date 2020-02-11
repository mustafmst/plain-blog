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
</style>
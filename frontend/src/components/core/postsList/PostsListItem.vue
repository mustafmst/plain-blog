<template>
    <div class="posts-list-item">
        <div class="pure-g">
            <h3 class=pure-u-3-4><router-link v-bind:to="postLink">{{post.title}}</router-link></h3>
            <span class="pure-u-1-4">{{post.publication_date}}</span>
        </div>
        <div class="pure-g">
            <p class="pure-u">
                {{post.content_short}}
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PostsListItem',
    props: ['post'],
    computed: {
        postLink: function() {
            return `/post/${this.post.id}`
        }
    }
}
</script>

<style lang="scss">
</style>
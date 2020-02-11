<template>
    <div class="posts-list-item">
        <div class="">
            <h3 class=""><router-link v-bind:to="postLink">{{post.title}}</router-link></h3>
            <span class="">{{post.publication_date}}</span>
        </div>
        <div class="">
            <p class="">
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
<template>
  <div class="comments">
    <h1>Comments</h1>
    <CommentForm></CommentForm>
  </div>
</template>

<script>
import CommentForm from "./CommentForm";

export default {
  name: 'Comments',
  components:{
    CommentForm
  },
  props: [
    "forPost"
  ],
  created(){
  }
}
</script>

<style lang="scss">
.comments {
  margin-top: 5em;
  padding-bottom: 5em;
}
</style>

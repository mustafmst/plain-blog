<template>
  <div class="comment-form">
    <form>
      <div class="form-group">
        <label for="author">Your name:</label>
        <input type="text" id="author" class="form-control" v-model="author"/>
      </div>
      <div class="form-group">
        <label for="comment">Comment</label>
        <textarea name="Comment" id="comment" cols="30" rows="10" class="form-control" v-model="comment"></textarea>
      </div>
      <input type="button" value="Submit" class="btn btn-primary" @click="sendComment"/>
    </form>
  </div>
</template>

<script>
export default {
  name: "CommentForm",
  data: function() {
    return {
      author: "",
      comment: ""
    };
  },
  created() {
  },
  methods: {
    sendComment(){
      window.alert(`author: ${author}; comment: ${comment}`)
    }
  }
};
</script>

<style lang="scss">
</style>

<template>
  <div>
    <div class="row" v-if="infopage != undefined">
        <div class="col-12" v-html="infopage.content"></div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
    name: "Info",
  methods: {
    ...mapActions({
      getContent: "posts/fetchInfopagePosts"
    })
  },
  computed: {
    ...mapGetters({
      infopage: "posts/getInfopage"
    })
  },
  created() {
    this.getContent();
  }
}
</script>

<style>

</style>
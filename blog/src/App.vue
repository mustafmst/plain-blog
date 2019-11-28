<template>
  <div id="app">
    <h1>Hello World!!!11</h1>
    <button @click="SelectWinner()">Select a Winner</button>
    <p>
      {{winner}}
    </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      names: null,
      winner: null
    };
  },
  mounted: function() {
    this.FetchData();
  },
  methods: {
    FetchData: function() {
      var app = this;
      axios.get("/api/blog/").then(res => {
        app.names = res.data.names;
      });
    },
    SelectWinner: function() {
      var winner = this.names[Math.floor(Math.random()*this.names.length)];
      this.winner = winner;
    }
  }
}
</script>

<style>
</style>

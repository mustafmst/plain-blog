<template>
  <div id="app" class="">
    <Header></Header>
    <div class="">
      <h1>Whatsjhfg jhgfjhgfjh up?</h1>
      <h1>Hello World!!!11</h1>
      <button @click="SelectWinner()">Select fffff a Winner</button>
      <p>
        {{winner}}
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Header from './components/core/Header';

export default {
  name: 'App',
  components: {
    Header
  },
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
@import url('https://fonts.googleapis.com/css?family=Lato&display=swap');


body{
  font-family: 'Lato', sans-serif;
}
</style>

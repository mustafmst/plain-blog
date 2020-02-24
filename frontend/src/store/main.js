import Vue from 'vue'
import Vuex from 'vuex'


import posts from './modules/posts'
import comments from './modules/comments'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    posts,
    comments
  }
})

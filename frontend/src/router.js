import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from './components/pages/Home.vue'
import Blog from './components/pages/Blog.vue'
import Info from './components/pages/Info.vue'
import Post from './components/pages/Post.vue'


Vue.use(VueRouter)

const routes = [
    { path: '/', component: Home },
    { path: '/blog', component: Blog },
    { path: '/info', component: Info },
    { path: '/post/:id', component: Post }
]

export default new VueRouter({
    routes
})
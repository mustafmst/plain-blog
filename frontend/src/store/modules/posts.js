import Axios from 'axios'

const state = {
    posts: [],
    currentPost: null
}

const getters = {
    allPosts: state => state.posts,
    currentPost: state => state.currentPost
}

const actions = {
    async fetchAllPosts({ commit }) {
        const res = await Axios.get('/api/blog/posts')
        commit('setPosts', res.data)
    },
    async fetchPost({commit}, postId) {
        const res = await Axios.get(`/api/blog/posts/${postId}`)
        commit('setCurrentPost', res.data)
    },
    clearCurrentPost({commit}) {
        commit('clearCurrentPost')
    }
}

const mutations = {
    setPosts: (state, posts) => (state.posts = [...posts]),
    setCurrentPost: (state, post) => (state.currentPost = {...post}),
    clearCurrentPost: (state) => (state.currentPost = null)
}

export default { namespaced: true, state, getters, actions, mutations }
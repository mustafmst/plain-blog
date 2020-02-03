import Axios from 'axios'

const state = {
    posts: []
}

const getters = {
    allPosts: state => state.posts
}

const actions = {
    async fetchAllPosts({ commit }) {
        const res = await Axios.get('/api/blog/posts')
        commit('setPosts', res.data)
    }
}

const mutations = {
    setPosts: (state, posts) => (state.posts = [...posts])
}

export default { namespaced: true, state, getters, actions, mutations }
import Axios from 'axios'

const state = {
    posts: [],
    currentPost: null,
    homepage: null,
    pinned: [],
    infopage: null
}

const getters = {
    allPosts: state => state.posts,
    currentPost: state => state.currentPost,
    getHomepage: state => state.homepage,
    getPinned: state => state.pinned,
    getInfopage: state => state.infopage,
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
    async clearCurrentPost({commit}) {
        commit('clearCurrentPost')
    },
    async fetchHomepagePosts({commit}) {
        const res = await Axios.get('/api/blog/posts/homepage')
        commit('setHomepagePosts', res.data)
    },
    async fetchInfopagePosts({commit}) {
        const res = await Axios.get('/api/blog/posts/infopage')
        commit('setInfopagePost', res.data)
    }
}

const mutations = {
    setPosts: (state, posts) => (state.posts = [...posts]),
    setCurrentPost: (state, post) => (state.currentPost = {...post}),
    clearCurrentPost: (state) => (state.currentPost = null),
    setHomepagePosts: (state, data) => (state.homepage = {...data.homepage}, state.pinned = [...data.pinned]),
    setInfopagePost: (state, data) => (state.infopage = {...data})
}

export default { namespaced: true, state, getters, actions, mutations }
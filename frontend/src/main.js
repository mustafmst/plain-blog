// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Purecss from 'purecss'
import 'purecss/build/grids-responsive-min.css'
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store/main'

Vue.config.productionTip = false


/* eslint-disable no-new */
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

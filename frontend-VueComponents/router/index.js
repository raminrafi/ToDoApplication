import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Main from '@/components/Main'
import Login from '@/components/Login'
import Signup from '@/components/Signup'

Vue.use(Router)

/*Router file containing all the components and their routes*/

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
    },
    {
      path: '/Signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/Main',
      name: 'Main',
      component: Main
    },

  ]
})

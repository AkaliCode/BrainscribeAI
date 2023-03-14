import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'

/**
 * Hier sind alle Links zu setzen für die verschiedenen Views für den Router.
 */
const routes: Array<RouteRecordRaw> = [
  {
    // The Home View 
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },
  {
    // The About View 
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    // The Pricing View 
    path: '/pricing',
    name: 'pricing',
    component: () => import('../views/PricingView.vue')
  },
  {
    // The Generate View
    path: '/generate',
    name: 'generate',
    component: () => import('../views/GenerateView.vue')
  }
]

// DONT TOUCH AB HIER: DAS IST DER ROUTER
const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

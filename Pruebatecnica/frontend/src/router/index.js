import { createRouter, createWebHistory } from 'vue-router'
// Importamos las vistas (las crearemos en el siguiente paso)
import ClienteView from '../views/ClienteView.vue'
import LogisticaView from '../views/LogisticaView.vue'
import AdminView from '../views/AdminView.vue'
import ClienteidView from '@/views/ClienteidView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'cliente',
      component: ClienteView
    },
    {
      path: '/logistica',
      name: 'logistica',
      component: LogisticaView
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminView
    },
    {
      path: '/clienteid',
      name: 'clienteid',
      component: ClienteidView
    }
  ]
})

export default router
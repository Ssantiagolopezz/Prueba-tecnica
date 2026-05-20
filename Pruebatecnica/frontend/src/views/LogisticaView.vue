<template>
  <div>
    <h2>📦 Panel de Control Logístico</h2>
    <div class="card">
      <div class="card-header">
        <h3>Órdenes Procesadas</h3>
        <p>Listado en tiempo real de los productos</p>
    </div>
    </div>
    <table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Proveedor</th>
      <th>Producto</th>
      <th>Cantidad</th>
      <th>Fecha Entrega</th> 
      <th>Prioridad</th>
      <th>Estado</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="orden in ordenes" :key="orden.id">
      <td>{{ orden.id }}</td>
      <td>{{ orden.proveedor }}</td>
      <td>{{ orden.producto }}</td>
      <td>{{ orden.cantidad }}</td>
      <td>{{ orden.fecha_entrega }}</td> 
      <td :style="estiloPrioridad(orden.prioridad)">
        {{ orden.prioridad }}
      </td>
      <td>
  <select 
  v-model="orden.estado" 
  @change="cambiarEstado(orden.id, orden.estado)"
  :class="{ 
    'status-entregado': orden.estado === 'Entregado',
    'status-cancelado': orden.estado === 'Cancelado' 
  }"
  class="status-select"
>
  <option value="Pendiente">Pendiente</option>
  <option value="En Proceso">En Proceso</option>
  <option value="Entregado">Entregado</option>
  <option value="Cancelado">Cancelado</option>
</select>
</td>
    </tr>
  </tbody>
</table>
  </div>
</template>



<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Swal from 'sweetalert2'

const ordenes = ref([])

const obtenerDatos = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/ordenes')
    ordenes.value = res.data
  } catch (err) {
    console.error("Error conectando al backend:", err)
  }
}

const estiloPrioridad = (nivel) => {
  if (nivel === 'Alta') return { color: 'red', fontWeight: 'bold' }
  if (nivel === 'Media') return { color: 'orange' }
  return { color: 'green' }
}

const cambiarEstado = async (id, estado) => {
  try {
    await axios.put(`http://127.0.0.1:8000/ordenes/${id}/estado?nuevo_estado=${estado}`)
    
    Swal.fire({
      title: '¡Estado Actualizado!',
      text: `La orden ${id} ahora está marcada como: ${estado}`,
      icon: 'success', 
      confirmButtonText: 'Genial',
      confirmButtonColor: '#4f46e5', 
      timer: 2500, 
      toast: true, 
      position: 'top-end' 
    })

  } catch (err) {
    console.error("Error al actualizar estado:", err)
    
  
    Swal.fire({
      title: '¡Ups!',
      text: 'No se pudo conectar con la base de datos.',
      icon: 'error', 
      confirmButtonText: 'Entendido',
      confirmButtonColor: '#ef4444' 
    })
  }
}

onMounted(obtenerDatos)
</script>

<style scoped>

.status-select {
  border: #4338ca 1px solid;
  background: #f1f5f9;
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 0.05em;
  padding: 8px 16px;
  border-radius: 999px; 
  transition: all 0.3s;
}

.status-entregado {
  background-color: #dcfce7 !important;
  color: #166534 !important;
}

.status-cancelado {
  background-color: #fee2e2 !important;
  color: #991b1b !important;
}

.status-select:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2);
  border-color: var(--primary);
}
</style>
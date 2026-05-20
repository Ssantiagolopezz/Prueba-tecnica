<template>
  <div class="view-container">
    <h2>📊 Panel de Control Administrativo</h2>

    <div class="stats-grid">
      
      <div class="card">
        <h3>Análisis de Prioridad</h3>
        <div class="chart-container">
           <Doughnut v-if="cargado" :data="chartData" :options="chartOptions" />
        </div>
      </div>

      
      <div class="card action-card">
        <h3>Acciones del Sistema</h3>
        <button @click="limpiarBaseDatos" class="btn-danger">
          Vaciar Registro de Órdenes
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { Doughnut } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js'
import Swal from 'sweetalert2'


ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

const cargado = ref(false)
const chartData = ref(null)
const chartOptions = { responsive: true, maintainAspectRatio: false }

const procesarDatosParaGrafico = (ordenes) => {
  const conteo = { Alta: 0, Media: 0, Baja: 0 }
  
  ordenes.forEach(o => {
    if (conteo[o.prioridad] !== undefined) conteo[o.prioridad]++
  })

  chartData.value = {
    labels: ['Alta', 'Media', 'Baja'],
    datasets: [{
      backgroundColor: ['#ff4d4d', '#ffaa00', '#42b983'],
      data: [conteo.Alta, conteo.Media, conteo.Baja]
    }]
  }
  cargado.value = true
}

const obtenerEstadisticas = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/ordenes')
    procesarDatosParaGrafico(res.data)
  } catch (err) {
    console.error("Error al cargar gráficos:", err)
  }
}

const limpiarBaseDatos = () => {

  Swal.fire({
    title: '¿Estás completamente seguro?',
    text: "¡Esta acción no se puede deshacer! Se borrarán todas las órdenes del sistema.",
    icon: 'warning',
    showCancelButton: true, 
    confirmButtonColor: '#ef4444', 
    cancelButtonColor: '#64748b', 
    confirmButtonText: 'Sí, vaciar base de datos',
    cancelButtonText: 'Cancelar'
  }).then(async (result) => {
    
    
    if (result.isConfirmed) {
      try {
      
        await axios.delete('http://127.0.0.1:8000/ordenes/vaciar')
      
        Swal.fire({
          title: '¡Base de Datos Limpia!',
          text: 'El registro de órdenes ha sido vaciado exitosamente.',
          icon: 'success',
          confirmButtonColor: '#4f46e5'
        });

        await obtenerEstadisticas();
      } catch (error) {
        Swal.fire({
          title: 'Error',
          text: 'Hubo un problema al intentar vaciar la base de datos.',
          icon: 'error',
          confirmButtonColor: '#ef4444'
        });
      }
    }
  });
};

onMounted(obtenerEstadisticas)
</script>

<style scoped>
.stats-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 20px;
}
.chart-card, .actions-card {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 10px;
  height: 400px;
}
.btn-danger {
  background: #ff4d4d;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}
.chart-container {
  position: relative;
  height: 250px; 
  width: 100%;
  display: flex;
  justify-content: center;
}

.action-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
<template>
    <div class="buscar-seccion">
      <h3>Buscar Producto por ID</h3>
      <div style="display: flex; gap: 10px; margin-bottom: 20px;">
        <input 
        type="number"
        v-model="idBuscado"
        placeholder="Ej: 63"
        class="input-estilo"
        />
        <button @click="buscarPorId" class="btn-primary">Buscar</button>
      </div>
      <div v-if="productoEncontrado" class="tarjeta-moderna">
  <h4 class="tarjeta-titulo">📦 Detalles del Producto #{{ productoEncontrado.id }}</h4>
  
  <div class="tarjeta-cuerpo">
    <div class="fila-dato">
      <span class="etiqueta">Estado:</span> 
      <span class="valor estado-badge">{{ productoEncontrado.estado }}</span>
    </div>
    
    <div class="fila-dato">
      <span class="etiqueta">Prioridad:</span> 
      <span class="valor">{{ productoEncontrado.prioridad }}</span>
    </div>
    
    <div class="fila-dato">
      <span class="etiqueta">Proveedor:</span> 
      <span class="valor">{{ productoEncontrado.proveedor }}</span>
    </div>

    <div class="fila-dato">
      <span class="etiqueta">Cantidad:</span> 
      <span class="valor">{{ productoEncontrado.cantidad }}</span>
    </div>

    <div class="fila-dato">
      <span class="etiqueta">Fecha de entrega:</span> 
      <span class="valor">{{ productoEncontrado.fecha_entrega }}</span>
    </div>

    <div class="fila-dato destacado">
      <span class="etiqueta">Última modificación:</span> 
      <span class="valor">{{ formatearFecha(productoEncontrado.hora_entrega) }}</span>
    </div>
  </div>
</div>
    </div>
    <p v-if="mensaje" :class="esError ? 'error' : 'success'">{{ mensaje }}</p>

</template>
<script setup>
import { ref } from 'vue'
import axios from 'axios'
import Swal from 'sweetalert2'

const mensaje = ref('')
const esError = ref(false)
const idBuscado = ref('');
const productoEncontrado = ref(null);


const formatearFecha = (fechaCruda) => {
  if (!fechaCruda) return 'Sin registrar';
  
  const fecha = new Date(fechaCruda);
  return fecha.toLocaleString('es-AR', {
    day: '2-digit', 
    month: '2-digit', 
    year: 'numeric',
    hour: '2-digit', 
    minute: '2-digit'
  });
};

const buscarPorId = async () => {
  if (!idBuscado.value){
    Swal.fire('Atencion', 'Por favor ingresa un ID valido.', 'warning');
    return;
  }

  try{
    const respuesta = await axios.get(`http://127.0.0.1:8000/ordenes/buscar/${idBuscado.value}`);

    if (respuesta.data.error) {
      Swal.fire('Sin resultado', 'No se encontro ningún producto con el ID ' + idBuscado.value, 'info');
      productoEncontrado.value = null;
    }else{
      productoEncontrado.value = respuesta.data;
    }
  }
  catch (error){
    Swal.fire('Error', 'Hubo un problema de conexion al buscar.', 'error');
  }
};
</script>
<style scoped>
.tarjeta-moderna {
  background-color: #ffffff;
  border: 1px solid #e5e7eb;
  border-left: 6px solid #10b981; /* Borde verde elegante */
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  max-width: 450px;
  font-family: system-ui, -apple-system, sans-serif;
}

.tarjeta-titulo {
  margin-top: 0;
  margin-bottom: 20px;
  color: #111827;
  font-size: 1.2rem;
  border-bottom: 2px solid #f3f4f6;
  padding-bottom: 10px;
}

.fila-dato {
  display: flex;
  justify-content: space-between; /* Esto alinea a los extremos */
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid #f9fafb;
}

.fila-dato:last-child {
  border-bottom: none;
}

.etiqueta {
  color: #6b7280;
  font-weight: 600;
  font-size: 0.9rem;
}

.valor {
  color: #374151;
  font-weight: 500;
}

.estado-badge {
  background-color: #d1fae5;
  color: #065f46;
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 0.85rem;
}

.destacado .etiqueta, .destacado .valor {
  color: #10b981;
}
.upload-container {
  max-width: 500px;
}
.card {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 8px;
  background: #f9f9f9;
  display: flex;
  flex-direction: column;
  gap: 15px;
}
.btn-upload {
  padding: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.btn-upload:disabled {
  background-color: #ccc;
}
.success { color: green; font-weight: bold; }
.error { color: red; font-weight: bold; }
</style>
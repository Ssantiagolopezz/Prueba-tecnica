<template>
  <div class="upload-container">
    <h2>📤 Carga de Órdenes de Suministro</h2>
    <p>Seleccione un archivo JSON o CSV para procesar las órdenes industriales.</p>
    
    <div class="card">
      <input type="file" @change="seleccionarArchivo" accept=".csv, .json" />
      <button @click="subirArchivo" :disabled="!archivo" class="btn-upload">
        Procesar Archivo
      </button>
    </div>


    <p v-if="mensaje" :class="esError ? 'error' : 'success'">{{ mensaje }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import Swal from 'sweetalert2'

const archivo = ref(null)
const mensaje = ref('')
const esError = ref(false)

const seleccionarArchivo = (event) => {
  archivo.value = event.target.files[0]
}

const subirArchivo = async () => {

    if (!archivo.value) {
        Swal.fire('Cuidado', 'Por favor selecciona un archivo primero.', 'warning');
        return;
    }

    const formData = new FormData();
    formData.append('file', archivo.value); 

    try {

        const response = await axios.post('http://127.0.0.1:8000/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });


        Swal.fire({
            title: '¡Archivo Procesado!',
            text: 'Las órdenes han sido guardadas y categorizadas correctamente.',
            icon: 'success',
            confirmButtonText: 'Genial',
            confirmButtonColor: '#10b981'
        });

    } catch (error) {

        console.error("Error en la subida:", error);
        Swal.fire({
            title: 'Error de carga',
            text: 'Asegúrate de que el backend esté encendido y el archivo sea correcto.',
            icon: 'error',
            confirmButtonText: 'Revisar',
            confirmButtonColor: '#ef4444'
        });
    }
};
</script>

<style scoped>
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
<template>
  <nav class="main-nav">

    <div class="nav-logo">
      <img src="./assets/logo-proa.jfif" alt="Logo Escuela" class="school-logo" />
      Sistema Logístico
    </div>
    
    <div class="nav-links">
      <RouterLink to="/" class="link">Cliente</RouterLink>
      <RouterLink to="/clienteid" class="link">Buscar Pedido</RouterLink>
      <RouterLink to="/logistica" class="link">Logística</RouterLink>
      <RouterLink to="/admin" class="link">Admin</RouterLink>
      
    </div>
  </nav>

  <div class="container">
    <RouterView />
  </div>
</template>

<style scoped>
.main-nav {
  display: flex;
  border-radius: var(--radius-lg);
  justify-content: space-between;
  align-items: center;
  padding: 0 10%;
  height: 75px;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  --shadow-sm: 0 4px 6px -1px #4338ca, 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --shadow-hover: 0 20px 25px -5px #4338ca, 0 8px 10px -6px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: var(--shadow-sm);
}


.nav-logo {
  display: flex;
  align-items: center;
  gap: 15px; 
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
}


.school-logo {
  height: 45px; 
  width: auto;
  object-fit: contain;
}

.link {
  color: #64748b;
  text-decoration: none;
  margin-left: 30px;
  font-weight: 500;
  transition: color 0.3s ease;
  position: relative;
}

.link:hover {
  color: #4f46e5;
}


.router-link-active {
  color: #4f46e5;
}
.router-link-active::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 100%;
  height: 3px;
  background-color: #4f46e5;
  border-radius: 2px;
}

.container {
  max-width: 1200px;
  margin: 3rem auto;
  padding: 0 20px;
}
</style>
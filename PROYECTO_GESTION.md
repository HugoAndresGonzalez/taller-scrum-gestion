# Sección 1: Planificación
# Sección 2: Historias de Usuario
Estas historias de usuario se desarrollan para una aplicación sencilla de Lista de Tareas implementada en Python.
# HU-01: Ver lista de tareas
**Como** usuario,  
**quiero** ver la lista de tareas registradas,  
**para** visualizar mis pendientes en cualquier momento.

**Criterios de aceptación**
- Dado que existen tareas, cuando solicito ver la lista, entonces se muestran todas.
- Dado que no existen tareas, el sistema muestra un mensaje informativo.

**Implementación**
- Función sugerida: `mostrar_tareas(tareas)`

# HU-02: Agregar tarea
**Como** usuario,  
**quiero** agregar una tarea escribiendo su descripción,  
**para** guardar nuevos pendientes.

**Criterios de aceptación**
- Se permite agregar tareas con texto válido.
- No se permiten tareas vacías.

**Implementación**
- Función sugerida: `agregar_tarea(tareas, descripcion)`
# HU-02: Agregar tarea
**Como** usuario,  
**quiero** agregar una tarea escribiendo su descripción,  
**para** guardar nuevos pendientes.

**Criterios de aceptación**
- Se permite agregar tareas con texto válido.
- No se permiten tareas vacías.

**Implementación**
- Función sugerida: `agregar_tarea(tareas, descripcion)`

# HU-03: Marcar tarea como completada
**Como** usuario,  
**quiero** marcar una tarea como completada,  
**para** identificar lo que ya terminé.

**Criterios de aceptación**
- Se puede cambiar el estado de una tarea existente.
- Si el ID no existe, el sistema muestra un error.

**Implementación**
- Función sugerida: `completar_tarea(tareas, id_tarea)`




# Sección 3: Evidencias y Retro

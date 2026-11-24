# VetCare - Arquitectura en capas

Aplicación de escritorio de ejemplo para una veterinaria, desarrollada con Python, Tkinter y SQLite.

## Requisitos
- Python 3.10 o superior
- No requiere instalar paquetes externos (Tkinter suele venir con Python).

## Ejecutar
Desde la carpeta del proyecto:

```bash
python main.py
```

La base de datos `vetcare.db` se crea automáticamente en la primera ejecución.

## Capas
1. **Presentación** (`presentacion/`): ventanas, controles y eventos de Tkinter.
2. **Negocio** (`negocio/`): validaciones y coordinación de operaciones.
3. **Acceso a datos** (`datos/`): conexión SQLite y repositorio SQL.
4. **Modelos** (`modelos/`): estructuras de datos del dominio.

## Módulos
- Mascotas
- Clientes
- Citas
- Servicios

Cada módulo permite crear, listar, editar y eliminar registros. Los campos obligatorios se validan en la capa de negocio.

## Nota de diseño
La interfaz usa Tkinter estándar para evitar dependencias externas. El diseño puede ampliarse con CustomTkinter sin mezclar la interfaz con SQL.

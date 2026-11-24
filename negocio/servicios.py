from datos.repositorio import Repositorio
from negocio.servicio_base import ServicioBase

mascotas = ServicioBase(
    Repositorio("mascotas", ["nombre", "especie", "raza", "edad", "propietario", "telefono"]),
    ["nombre", "especie", "propietario"]
)
clientes = ServicioBase(
    Repositorio("clientes", ["nombre", "documento", "telefono", "correo", "direccion"]),
    ["nombre", "documento", "telefono"]
)
citas = ServicioBase(
    Repositorio("citas", ["fecha", "hora", "mascota", "propietario", "servicio", "estado"]),
    ["fecha", "hora", "mascota", "propietario", "servicio"]
)
servicios = ServicioBase(
    Repositorio("servicios", ["nombre", "descripcion", "duracion", "precio"]),
    ["nombre"]
)

MODULOS = {
    "Mascotas": (mascotas, ["Nombre", "Especie", "Raza", "Edad", "Propietario", "Teléfono"],
                 ["nombre", "especie", "raza", "edad", "propietario", "telefono"]),
    "Clientes": (clientes, ["Nombre", "Documento", "Teléfono", "Correo", "Dirección"],
                 ["nombre", "documento", "telefono", "correo", "direccion"]),
    "Citas": (citas, ["Fecha", "Hora", "Mascota", "Propietario", "Servicio", "Estado"],
              ["fecha", "hora", "mascota", "propietario", "servicio", "estado"]),
    "Servicios": (servicios, ["Nombre", "Descripción", "Duración", "Precio"],
                  ["nombre", "descripcion", "duracion", "precio"]),
}

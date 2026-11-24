from dataclasses import dataclass

@dataclass
class Servicio:
    nombre: str
    descripcion: str
    duracion: str
    precio: str
    id: int | None = None

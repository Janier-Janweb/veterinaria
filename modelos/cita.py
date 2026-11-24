from dataclasses import dataclass

@dataclass
class Cita:
    fecha: str
    hora: str
    mascota: str
    propietario: str
    servicio: str
    estado: str = "Pendiente"
    id: int | None = None

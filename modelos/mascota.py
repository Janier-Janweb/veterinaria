from dataclasses import dataclass

@dataclass
class Mascota:
    nombre: str
    especie: str
    raza: str
    edad: str
    propietario: str
    telefono: str
    id: int | None = None

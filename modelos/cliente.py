from dataclasses import dataclass

@dataclass
class Cliente:
    nombre: str
    documento: str
    telefono: str
    correo: str
    direccion: str
    id: int | None = None

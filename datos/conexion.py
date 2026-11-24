import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "vetcare.db"

def obtener_conexion():
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

def inicializar_base_datos():
    with obtener_conexion() as con:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            documento TEXT NOT NULL UNIQUE,
            telefono TEXT NOT NULL,
            correo TEXT,
            direccion TEXT
        );
        CREATE TABLE IF NOT EXISTS mascotas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especie TEXT NOT NULL,
            raza TEXT,
            edad TEXT,
            propietario TEXT NOT NULL,
            telefono TEXT
        );
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            mascota TEXT NOT NULL,
            propietario TEXT NOT NULL,
            servicio TEXT NOT NULL,
            estado TEXT NOT NULL DEFAULT 'Pendiente'
        );
        CREATE TABLE IF NOT EXISTS servicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            duracion TEXT,
            precio TEXT
        );
        """)

from datos.conexion import obtener_conexion

class Repositorio:
    """Acceso genérico a datos. Solo esta capa conoce SQL y SQLite."""
    def __init__(self, tabla, campos):
        self.tabla = tabla
        self.campos = campos

    def listar(self):
        with obtener_conexion() as con:
            sql = f"SELECT id, {', '.join(self.campos)} FROM {self.tabla} ORDER BY id DESC"
            return [dict(fila) for fila in con.execute(sql).fetchall()]

    def insertar(self, valores):
        columnas = ", ".join(self.campos)
        marcadores = ", ".join("?" for _ in self.campos)
        with obtener_conexion() as con:
            cur = con.execute(
                f"INSERT INTO {self.tabla} ({columnas}) VALUES ({marcadores})",
                tuple(valores[c] for c in self.campos)
            )
            return cur.lastrowid

    def actualizar(self, registro_id, valores):
        asignaciones = ", ".join(f"{c} = ?" for c in self.campos)
        parametros = [valores[c] for c in self.campos] + [registro_id]
        with obtener_conexion() as con:
            con.execute(f"UPDATE {self.tabla} SET {asignaciones} WHERE id = ?", parametros)

    def eliminar(self, registro_id):
        with obtener_conexion() as con:
            con.execute(f"DELETE FROM {self.tabla} WHERE id = ?", (registro_id,))

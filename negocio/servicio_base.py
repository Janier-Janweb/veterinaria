class ServicioBase:
    def __init__(self, repositorio, campos_obligatorios):
        self.repositorio = repositorio
        self.campos_obligatorios = campos_obligatorios

    def listar(self):
        return self.repositorio.listar()

    def guardar(self, valores, registro_id=None):
        valores = {k: str(v).strip() for k, v in valores.items()}
        faltantes = [campo for campo in self.campos_obligatorios if not valores.get(campo)]
        if faltantes:
            raise ValueError("Completa los campos obligatorios: " + ", ".join(faltantes))
        if registro_id:
            self.repositorio.actualizar(registro_id, valores)
        else:
            self.repositorio.insertar(valores)

    def eliminar(self, registro_id):
        if not registro_id:
            raise ValueError("Selecciona un registro.")
        self.repositorio.eliminar(registro_id)

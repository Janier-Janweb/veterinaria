import tkinter as tk
from tkinter import ttk, messagebox
from datos.conexion import inicializar_base_datos
from negocio.servicios import MODULOS
from presentacion.componentes.estilos import *

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        inicializar_base_datos()
        self.title("VetCare | Gestión veterinaria")
        self.geometry("1250x760")
        self.minsize(1000, 650)
        self.configure(bg=BG)
        self.seleccion_id = None
        self.modulo_actual = None
        self._construir_estructura()
        self.mostrar_inicio()

    def _construir_estructura(self):
        self.menu = tk.Frame(self, bg=SIDEBAR, width=220)
        self.menu.pack(side="left", fill="y")
        self.menu.pack_propagate(False)
        tk.Label(self.menu, text="✚  VetCare", bg=SIDEBAR, fg=WHITE,
                 font=("Segoe UI", 21, "bold")).pack(anchor="w", padx=22, pady=(28, 4))
        tk.Label(self.menu, text="GESTIÓN VETERINARIA", bg=SIDEBAR, fg="#9FB4CC",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=25, pady=(0, 35))
        for nombre in ["Dashboard", "Mascotas", "Clientes", "Citas", "Servicios"]:
            tk.Button(self.menu, text="   " + nombre, anchor="w",
                      command=lambda n=nombre: self.mostrar_modulo(n) if n != "Dashboard" else self.mostrar_inicio(),
                      bg=SIDEBAR, fg="#D5E0EC", activebackground=PRIMARY,
                      activeforeground=WHITE, relief="flat", bd=0,
                      font=("Segoe UI", 10), padx=15, pady=13,
                      cursor="hand2").pack(fill="x", padx=10, pady=2)
        tk.Label(self.menu, text="Uniteg", bg=SIDEBAR,
                 fg="#91A9C2", font=("Segoe UI", 8), wraplength=175).pack(side="bottom", pady=22)

        self.zona = tk.Frame(self, bg=BG)
        self.zona.pack(side="left", fill="both", expand=True)
        barra = tk.Frame(self.zona, bg=WHITE, height=65)
        barra.pack(fill="x")
        barra.pack_propagate(False)
        tk.Label(barra, text="Panel de administración", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 12, "bold")).pack(side="left", padx=28)
        tk.Label(barra, text="●  Administrador", bg=WHITE, fg=GREEN,
                 font=("Segoe UI", 9, "bold")).pack(side="right", padx=28)
        self.contenido = tk.Frame(self.zona, bg=BG)
        self.contenido.pack(fill="both", expand=True, padx=28, pady=25)

    def limpiar(self):
        for w in self.contenido.winfo_children():
            w.destroy()

    def titulo(self, titulo, subtitulo):
        tk.Label(self.contenido, text=titulo, bg=BG, fg=TEXT,
                 font=("Segoe UI", 22, "bold")).pack(anchor="w")
        tk.Label(self.contenido, text=subtitulo, bg=BG, fg=MUTED,
                 font=("Segoe UI", 9)).pack(anchor="w", pady=(4, 20))

    def mostrar_inicio(self):
        self.limpiar()
        self.modulo_actual = None
        self.titulo("¡Bienvenido a VetCare!", "Resumen de la información registrada en tu clínica.")
        tarjetas = tk.Frame(self.contenido, bg=BG)
        tarjetas.pack(fill="x")
        for nombre, cantidad, color in [
            ("Mascotas", len(MODULOS["Mascotas"][0].listar()), PRIMARY),
            ("Clientes", len(MODULOS["Clientes"][0].listar()), GREEN),
            ("Citas", len(MODULOS["Citas"][0].listar()), "#E99A36"),
            ("Servicios", len(MODULOS["Servicios"][0].listar()), "#8066C8")
        ]:
            caja = tk.Frame(tarjetas, bg=WHITE, highlightthickness=1, highlightbackground=BORDER)
            caja.pack(side="left", fill="x", expand=True, padx=(0, 12), ipady=14)
            tk.Label(caja, text=nombre, bg=WHITE, fg=MUTED,
                     font=("Segoe UI", 9)).pack(anchor="w", padx=17, pady=(10, 4))
            tk.Label(caja, text=str(cantidad), bg=WHITE, fg=color,
                     font=("Segoe UI", 25, "bold")).pack(anchor="w", padx=17, pady=(0, 8))
        panel = tk.Frame(self.contenido, bg=WHITE, highlightthickness=1, highlightbackground=BORDER)
        panel.pack(fill="both", expand=True, pady=24)
        tk.Label(panel, text="Arquitectura del sistema", bg=WHITE, fg=TEXT,
                 font=("Segoe UI", 14, "bold")).pack(anchor="w", padx=22, pady=(22, 8))
        texto = ("Presentación: ventanas Tkinter y formularios.\n\n"
                 "Negocio: validaciones y reglas de la veterinaria.\n\n"
                 "Datos: repositorios que ejecutan las operaciones SQL.\n\n"
                 "Base de datos: SQLite almacena los registros localmente.")
        tk.Label(panel, text=texto, bg=WHITE, fg=MUTED, justify="left",
                 font=("Segoe UI", 10)).pack(anchor="w", padx=22, pady=10)

    def mostrar_modulo(self, nombre):
        self.limpiar()
        self.modulo_actual = nombre
        self.seleccion_id = None
        servicio, etiquetas, claves = MODULOS[nombre]
        self.titulo("Gestión de " + nombre.lower(), "Crea, consulta, edita y elimina registros.")
        acciones = tk.Frame(self.contenido, bg=BG)
        acciones.pack(fill="x", pady=(0, 12))
        tk.Button(acciones, text="+ Nuevo registro", command=self.nuevo,
                  bg=PRIMARY, fg=WHITE, relief="flat", font=("Segoe UI", 9, "bold"),
                  padx=15, pady=9).pack(side="left")
        tk.Button(acciones, text="Editar seleccionado", command=self.editar,
                  bg="#E7F0FC", fg=PRIMARY, relief="flat", font=("Segoe UI", 9, "bold"),
                  padx=15, pady=9).pack(side="left", padx=8)
        tk.Button(acciones, text="Eliminar", command=self.eliminar,
                  bg="#FCEBEC", fg="#C44952", relief="flat", font=("Segoe UI", 9, "bold"),
                  padx=15, pady=9).pack(side="left")
        panel = tk.Frame(self.contenido, bg=WHITE, highlightthickness=1, highlightbackground=BORDER)
        panel.pack(fill="both", expand=True)
        self.tabla = ttk.Treeview(panel, columns=["id"] + claves, show="headings")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=34, font=("Segoe UI", 9),
                        background=WHITE, fieldbackground=WHITE, foreground=TEXT)
        style.configure("Treeview.Heading", background="#EFF4F9", foreground=MUTED,
                        font=("Segoe UI", 8, "bold"), padding=9, relief="flat")
        self.tabla.heading("id", text="ID")
        self.tabla.column("id", width=55, anchor="center")
        for etiqueta, clave in zip(etiquetas, claves):
            self.tabla.heading(clave, text=etiqueta.upper())
            self.tabla.column(clave, width=145, minwidth=90)
        self.tabla.pack(fill="both", expand=True, padx=15, pady=15)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)
        self.recargar()

    def recargar(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        servicio, etiquetas, claves = MODULOS[self.modulo_actual]
        for fila in servicio.listar():
            self.tabla.insert("", "end", values=[fila["id"]] + [fila.get(c, "") for c in claves])

    def seleccionar(self, _event=None):
        seleccionado = self.tabla.selection()
        self.seleccion_id = self.tabla.item(seleccionado[0], "values")[0] if seleccionado else None

    def nuevo(self):
        self.abrir_formulario()

    def editar(self):
        if not self.seleccion_id:
            messagebox.showwarning("Atención", "Selecciona un registro para editar.")
            return
        fila = next((r for r in MODULOS[self.modulo_actual][0].listar()
                     if str(r["id"]) == str(self.seleccion_id)), None)
        self.abrir_formulario(fila)

    def abrir_formulario(self, fila=None):
        nombre = self.modulo_actual
        servicio, etiquetas, claves = MODULOS[nombre]
        ventana = tk.Toplevel(self)
        ventana.title(("Editar " if fila else "Nuevo ") + nombre)
        ventana.configure(bg=WHITE)
        ventana.geometry("440x600")
        ventana.resizable(False, True)
        ventana.transient(self)
        ventana.grab_set()
        tk.Label(ventana, text=("Editar " if fila else "Registrar ") + nombre.lower(),
                 bg=WHITE, fg=TEXT, font=("Segoe UI", 17, "bold")).pack(anchor="w", padx=25, pady=(22, 5))
        tk.Label(ventana, text="Ingresa la información solicitada.",
                 bg=WHITE, fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w", padx=25, pady=(0, 12))
        entradas = {}
        for etiqueta, clave in zip(etiquetas, claves):
            tk.Label(ventana, text=etiqueta, bg=WHITE, fg=TEXT,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=25, pady=(7, 3))
            entrada = tk.Entry(ventana, font=("Segoe UI", 10), relief="solid", bd=1)
            entrada.pack(fill="x", padx=25, ipady=7)
            if fila:
                entrada.insert(0, fila.get(clave, "") or "")
            entradas[clave] = entrada

        def guardar():
            valores = {k: e.get() for k, e in entradas.items()}
            try:
                servicio.guardar(valores, fila["id"] if fila else None)
                messagebox.showinfo("VetCare", "Registro guardado correctamente.")
                ventana.destroy()
                self.recargar()
            except Exception as error:
                messagebox.showerror("No se pudo guardar", str(error))

        tk.Button(ventana, text="Guardar", command=guardar, bg=PRIMARY, fg=WHITE,
                  relief="flat", font=("Segoe UI", 10, "bold"), pady=10).pack(fill="x", padx=25, pady=20)

    def eliminar(self):
        if not self.seleccion_id:
            messagebox.showwarning("Atención", "Selecciona un registro para eliminar.")
            return
        if messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar este registro?"):
            try:
                MODULOS[self.modulo_actual][0].eliminar(self.seleccion_id)
                self.seleccion_id = None
                self.recargar()
            except Exception as error:
                messagebox.showerror("Error", str(error))

import tkinter as tk
from tkinter import simpledialog, messagebox
from model.registro import Registro
from model.factura import Factura
class InterfazGrafica:
    def __init__(self, registro, factura):
        self.registro = registro
        self.factura = factura
        self.ventana = tk.Tk()
        self.ventana.title("Aplicación de Registro y Facturación")

        self.resultado_label = tk.Label(self.ventana, text="")
        self.resultado_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.menu_principal()

    def menu_principal(self):
        etiqueta = tk.Label(self.ventana, text="Seleccione una opción:")
        etiqueta.grid(row=1, column=0, columnspan=2, pady=10)

        opciones = [
            "Crear preregistro",
            "Mostrar registro",
            "Modificar preregistro",
            "Eliminar registro",
            "Mostrar todos los registros",
            "Generar factura",
            "Crear estudiante",
            "Modificar info estudiante",
            "Eliminar estudiante",
            "Crear carnet",
            "Salir"
        ]

        for i, opcion in enumerate(opciones, start=2):
            boton = tk.Button(self.ventana, text=f"{i-1}. {opcion}", command=lambda op=opcion: self.ejecutar_opcion(op))
            boton.grid(row=i, column=0, columnspan=2, pady=5)

    def ejecutar_opcion(self, opcion):
        try:
            if opcion == "Crear preregistro":
                self.crear_preregistro()
            elif opcion == "Mostrar registro":
                self.mostrar_registro()
            elif opcion == "Modificar preregistro":
                self.modificar_preregistro()
            elif opcion == "Eliminar registro":
                self.eliminar_registro()
            elif opcion == "Mostrar todos los registros":
                self.mostrar_todos_los_registros()
            elif opcion == "Generar factura":
                self.generar_factura()
            elif opcion == "Crear estudiante":
                self.crear_estudiante()
            elif opcion == "Modificar info estudiante":
                self.modificar_info_estudiante()
            elif opcion == "Eliminar estudiante":
                self.eliminar_estudiante()
            elif opcion == "Crear carnet":
                self.crear_carnet()
            elif opcion == "Salir":
                self.ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def volver_al_menu_principal(self):
        self.ventana.destroy()
        self.ventana = tk.Tk()
        self.ventana.title("Aplicación de Registro y Facturación")
        self.menu_principal()

    def mostrar_resultado(self, resultado):
        resultado_ventana = tk.Toplevel(self.ventana)
        resultado_ventana.title("Resultado")
        resultado_label = tk.Label(resultado_ventana, text=resultado)
        resultado_label.pack(padx=10, pady=10)

    def crear_preregistro(self):
        nombre = simpledialog.askstring("Crear preregistro", "Nombre:")
        if nombre is None:
            self.volver_al_menu_principal()
            return

        edad = simpledialog.askinteger("Crear preregistro", "Edad:")
        if edad is None:
            self.volver_al_menu_principal()
            return

        identidad = simpledialog.askstring("Crear preregistro", "Tarjeta de identidad:")
        if identidad is None:
            self.volver_al_menu_principal()
            return

        grado = simpledialog.askstring("Crear preregistro", "Grado:")
        if grado is None:
            self.volver_al_menu_principal()
            return

        nombre_acudiente = simpledialog.askstring("Crear preregistro", "Nombre del acudiente:")
        if nombre_acudiente is None:
            self.volver_al_menu_principal()
            return

        cedula_acudiente = simpledialog.askstring("Crear preregistro", "Cédula del acudiente:")
        if cedula_acudiente is None:
            self.volver_al_menu_principal()
            return

        trabaja_acudiente = simpledialog.askstring("Crear preregistro", "¿Trabaja el acudiente? (Sí/No):")
        if trabaja_acudiente is not None:
            trabaja_acudiente = trabaja_acudiente.lower()
        else:
            self.volver_al_menu_principal()
            return

        telefono = simpledialog.askstring("Crear preregistro", "Teléfono:")
        if telefono is None:
            self.volver_al_menu_principal()
            return

        direccion = simpledialog.askstring("Crear preregistro", "Dirección:")
        if direccion is None:
            self.volver_al_menu_principal()
            return

        convenio_policia = simpledialog.askstring("Crear preregistro", "¿Convenio con la policía? (Sí/No):")
        if convenio_policia is not None:
            convenio_policia = convenio_policia.lower()
        else:
            self.volver_al_menu_principal()
            return
        
        if any(val is None or val == "" for val in [nombre, identidad, grado, nombre_acudiente, cedula_acudiente, telefono, direccion, convenio_policia]):
            messagebox.showwarning("Error", "Todos los campos son obligatorios. Por favor, complete la información.")
            return

        self.registro.crear_preregistro(
        nombre, edad, identidad, grado, nombre_acudiente, cedula_acudiente,
        trabaja_acudiente, telefono, direccion, convenio_policia,
    )
        self.mostrar_resultado("Pre-registro creado con éxito.")

    def mostrar_registro(self):
        indice_mostrar = simpledialog.askinteger("Mostrar registro", "Ingrese el índice del preregistro que desea mostrar:")
        
        if indice_mostrar is not None:
            resultado = self.registro.mostrar_registro(indice_mostrar)
            self.mostrar_resultado(resultado)
        else:
            self.mostrar_resultado("Operación cancelada por el usuario.")

    def modificar_preregistro(self):
        indice_modificar = simpledialog.askinteger("Modificar preregistro", "Ingrese el índice del preregistro que desea modificar:")
        if 0 <= indice_modificar < len(self.registro.registros):
            nuevos_valores = {}
            for campo in self.registro.registros[indice_modificar]:
                valor_nuevo = simpledialog.askstring(f"Modificar preregistro", f"Nuevo {campo} (deje en blanco para mantener el valor actual):")
                if valor_nuevo:
                    nuevos_valores[campo] = valor_nuevo

            self.registro.modificar_info_preregistro(indice_modificar, **nuevos_valores)
            messagebox.showinfo("Éxito", "Pre-registro modificado con éxito.")
        else:
            messagebox.showwarning("Error", "Índice de registro no válido.")

    def eliminar_registro(self):
        indice_eliminar = simpledialog.askinteger("Eliminar registro", "Ingrese el índice del preregistro que desea eliminar:")
        if self.registro.registros is not None and 0 <= indice_eliminar < len(self.registro.registros):
            confirmacion = messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar este registro?")
            if confirmacion:
                self.registro.eliminar_registro(indice_eliminar)
                messagebox.showinfo("Éxito", "Registro eliminado con éxito.")
            else:
                messagebox.showinfo("Cancelado", "Eliminación cancelada.")
        else:
            messagebox.showwarning("Error", "Índice de registro no válido.")

    def mostrar_todos_los_registros(self):
        if self.registro.registros:
            info_registros = "Lista de inscripciones:\n"
            for i, preregistro in enumerate(self.registro.registros):
                info_registros += f"{i}. {preregistro['nombre']}\n"

            messagebox.showinfo("Información", info_registros)
        else:
            messagebox.showinfo("Información", "No hay inscripciones disponibles.")

    def generar_factura(self):
        indice_generar_factura = simpledialog.askinteger("Generar factura", "Ingrese el índice del preregistro para generar la factura:")
        if 0 <= indice_generar_factura < len(self.registro.registros):
            self.factura.calcular_factura(indice_generar_factura)
            messagebox.showinfo("Éxito", "Factura generada con éxito.")
        else:
            messagebox.showwarning("Error", "Índice de registro no válido.")

    def crear_estudiante(self):
        try:
            if not self.registro.registros:
                messagebox.showwarning("Error", "No hay preregistros disponibles para crear un estudiante.")
                return

            indice_crear_estudiante = simpledialog.askinteger("Crear estudiante", "Ingrese el índice del preregistro para crear el estudiante:")
            if indice_crear_estudiante is not None:
                if 0 <= indice_crear_estudiante < len(self.registro.registros):
                    self.registro.crear_estudiante(indice_crear_estudiante)
                    messagebox.showinfo("Éxito", "Estudiante creado con éxito.")
                else:
                    messagebox.showwarning("Error", "Índice de preregistro no válido.")
            else:
                messagebox.showinfo("Cancelado", "Creación de estudiante cancelada.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear estudiante: {str(e)}")

    def modificar_info_estudiante(self):
        indice_modificar_estudiante = simpledialog.askinteger("Modificar info estudiante", "Ingrese el índice del estudiante que desea modificar:")
        if self.registro.registros is not None and 0 <= indice_modificar_estudiante < len(self.registro.registros):
            nuevos_valores = {}
            for campo in self.registro.registros[indice_modificar_estudiante]:
                valor_nuevo = simpledialog.askstring(f"Modificar info estudiante", f"Nuevo {campo} (deje en blanco para mantener el valor actual):")
                if valor_nuevo:
                    nuevos_valores[campo] = valor_nuevo

            self.registro.modificar_info_estudiante(indice_modificar_estudiante, **nuevos_valores)
            messagebox.showinfo("Éxito", "Información de estudiante modificada con éxito.")
        else:
            messagebox.showwarning("Error", "Índice de registro no válido.")

    def eliminar_estudiante(self):
        indice_eliminar_estudiante = simpledialog.askinteger("Eliminar estudiante", "Ingrese el índice del estudiante que desea eliminar:")
        if self.registro.registros is not None and 0 <= indice_eliminar_estudiante < len(self.registro.registros):
            confirmacion = messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar este estudiante?")
            if confirmacion:
                self.registro.eliminar_estudiante(indice_eliminar_estudiante)
                messagebox.showinfo("Éxito", "Estudiante eliminado con éxito.")
            else:
                messagebox.showinfo("Cancelado", "Eliminación cancelada.")
        else:
            messagebox.showwarning("Error", "Índice de estudiante no válido.")

    def crear_carnet(self):
        indice_crear_carnet = simpledialog.askinteger("Crear carnet", "Ingrese el índice del estudiante para crear el carnet:")
        if self.registro.registros is not None and 0 <= indice_crear_carnet < len(self.registro.registros):
            self.registro.crear_carnet(indice_crear_carnet)
            messagebox.showinfo("Éxito", "Carnet creado con éxito.")
        else:
            messagebox.showwarning("Error", "Índice de estudiante no válido.")

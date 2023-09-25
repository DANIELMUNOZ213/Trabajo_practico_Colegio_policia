class Registro:
    def __init__(self):
        self.registros = []

    def crear_preregistro(self, nombre, edad, identidad, grado, nombre_acudiente, cedula_acudiente, trabaja, telefono, direccion, convenio_policia, factura):
        try:
            edad = int(edad)
        except ValueError:
            print("Error: Edad debe ser un número entero.")
            return

        preregistro = {
            "nombre": nombre,
            "edad": edad,
            "identidad": identidad,
            "grado": grado,
            "nombre_acudiente": nombre_acudiente,
            "cedula_acudiente": cedula_acudiente,
            "trabaja": trabaja,
            "telefono": telefono,
            "direccion": direccion,
            "convenio_policia": convenio_policia
        }
        self.registros.append(preregistro)
        print("Registro creado con éxito.")

        factura.generar_factura(len(self.registros) - 1)

    def mostrar_registro(self, indice):
        if 0 <= indice < len(self.registros):
            registro = self.registros[indice]
            for key, value in registro.items():
                print(f"{key}: {value}")
        else:
            print("Índice de registro no válido.")

    def modificar_preregistro(self, indice, **kwargs):
        if 0 <= indice < len(self.registros):
            registro = self.registros[indice]
            for key, value in kwargs.items():
                if key == "edad":
                    try:
                        value = int(value)
                    except ValueError:
                        print("Error: Edad debe ser un número entero.")
                        continue
                if key == "trabaja":
                    if value.lower() not in ("sí", "no"):
                        print("Error: El valor de 'trabaja' debe ser 'Sí' o 'No'.")
                        continue
                registro[key] = value
            print("Registro modificado con éxito.")
        else:
            print("Índice de registro no válido.")

    def eliminar_registro(self, indice):
        if 0 <= indice < len(self.registros):
            del self.registros[indice]
            print("Registro eliminado con éxito.")
        else:
            print("Índice de registro no válido.")

    def mostrar_registros(self):
        for i, registro in enumerate(self.registros):
            print(f"Registro {i + 1}:")
            for key, value in registro.items():
                print(f"{key}: {value}")
            print()

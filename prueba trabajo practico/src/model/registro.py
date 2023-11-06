import json
import uuid
class Factura:
    def __init__(self, registro):
        self.registro = registro
        self.tarifas_por_grado = {
            "1": 1000,
            "2": 1500,
            "3": 2000,
            "4": 2500,
            "6": 3000,
            "7": 3500,
            "8": 4000,
            "9": 4500,
            "10": 5000,
            "11": 5500,
        }
        self.descuento_trabajo_policia = 0.2

    def generar_factura(self, indice):
        try:
            if 0 <= indice < len(self.registro.registros):
                estudiante = self.registro.registros[indice]
                factura = self.calcular_factura(indice)
                estudiante['factura'] = factura
                self.imprimir_factura(estudiante)
                self.registro.guardar_en_json()
            else:
                print("Índice de registro no válido.")
        except Exception as e:
            print(f"Error al generar factura: {str(e)}")

    def calcular_factura(self, indice):
        try:
            if 0 <= indice < len(self.registro.registros):
                preregistro = self.registro.registros[indice]
                costo_inscripcion = self.calcular_costo_inscripcion(indice)
                return {
                    "costo_inscripcion": costo_inscripcion,
                    "descuentos": {}
                }
            else:
                return None
        except Exception as e:
            print(f"Error al calcular factura: {str(e)}")
            return None

    def calcular_costo_inscripcion(self, indice):
        try:
            if 0 <= indice < len(self.registro.registros):
                preregistro = self.registro.registros[indice]
                grado = preregistro["grado"]
                costo_base = self.tarifas_por_grado.get(grado, 0)
                if preregistro["convenio_policia"]:
                    costo_con_descuento = costo_base * (1 - self.descuento_trabajo_policia)
                    return costo_con_descuento
                else:
                    return costo_base
            else:
                return None
        except Exception as e:
            print(f"Error al calcular costo de inscripción: {str(e)}")
            return None

    def imprimir_factura(self, estudiante):
        print("Factura:")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"ID Estudiante: {estudiante['id_estudiante']}")
        print(f"Costo de Inscripción: ${estudiante['factura']['costo_inscripcion']:.2f}")
        
class Registro:
    def __init__(self):
        self.registros = []
        self.factura = Factura(self)
        self.cargar_desde_json()

    def guardar_en_json(self):
        with open('registros.json', 'w') as archivo_json:
            json.dump(self.registros, archivo_json)

    def cargar_desde_json(self):
        try:
            with open('registros.json', 'r') as archivo_json:
                self.registros = json.load(archivo_json)
        except FileNotFoundError:
            print("No se encontró el archivo JSON. Se creará uno nuevo al guardar datos.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. Revise el formato del archivo.")

    def generar_id_estudiante(self):
        return str(uuid.uuid4())[:8]

    def validar_campos_obligatorios(self, **campos):
        for campo, valor in campos.items():
            if not valor:
                raise ValueError(f"Error: El campo '{campo}' es obligatorio.")

    def crear_preregistro(self, nombre, edad, identidad, grado, nombre_acudiente, cedula_acudiente,
                        trabaja_acudiente, telefono, direccion, convenio_policia):
        try:
            edad = int(edad)
        except ValueError:
            print("Error: Edad debe ser un número entero.")
            return

        self.validar_campos_obligatorios(
            nombre=nombre, identidad=identidad, grado=grado,
            nombre_acudiente=nombre_acudiente, cedula_acudiente=cedula_acudiente,
            telefono=telefono, direccion=direccion, convenio_policia=convenio_policia
        )

        preregistro = {
            "nombre": nombre,
            "edad": edad,
            "identidad": identidad,
            "grado": grado,
            "nombre_acudiente": nombre_acudiente,
            "cedula_acudiente": cedula_acudiente,
            "trabaja_acudiente": trabaja_acudiente,
            "telefono": telefono,
            "direccion": direccion,
            "convenio_policia": convenio_policia,
        }

        self.registros.append(preregistro)
        indice_asignado = len(self.registros)
        preregistro["id_estudiante"] = self.generar_id_estudiante()

        print(f"Pre-registro creado con éxito. Índice asignado: {indice_asignado}")
        self.guardar_en_json()

        # Llama al método generar_factura después de crear el preregistro
        self.factura.generar_factura(indice_asignado - 1)

    def mostrar_registro(self, indice):
        if self.registros is not None and 0 <= indice < len(self.registros):
            preregistro = self.registros[indice]
            info_preregistro = f"Inscripción en el índice {indice}:\n"
            
            for campo, valor in preregistro.items():
                info_preregistro += f"{campo}: {valor}\n"

            factura_info = preregistro.get('factura')
            if factura_info is not None:
                info_preregistro += "Factura:\n"
                for clave, valor in factura_info.items():
                    info_preregistro += f"{clave}: {valor}\n"

            carnet_info = preregistro.get('carnet')
            if carnet_info is not None:
                info_preregistro += f"Carnet: {carnet_info}\n"

            return info_preregistro
        else:
            return "Error: Índice de inscripción no válido."

    def modificar_info_preregistro(self, indice, **kwargs):
        if 0 <= indice < len(self.registros):
            preregistro = self.registros[indice]
            for key, value in kwargs.items():
                if key in preregistro:
                    preregistro[key] = value
            print("Información de pre-registro modificada con éxito.")
            self.guardar_en_json()
        else:
            print("Índice de registro no válido.")

    def eliminar_registro(self, indice):
        if 0 <= indice < len(self.registros):
            del self.registros[indice]
            print(f"Registro en el índice {indice} eliminado con éxito.")
            self.guardar_en_json()
        else:
            print("Índice de registro no válido.")

    def crear_estudiante(self, indice):
        if self.registros is not None and 0 <= indice < len(self.registros):
            preregistro = self.registros[indice]
            estudiante = {
                "nombre": preregistro["nombre"],
                "id_estudiante": f"ID-{indice}",
                "telefono": preregistro["telefono"],
                "direccion": preregistro["direccion"],
                "edad": preregistro["edad"],
                "carnet": None,
                "factura": None,
            }
            preregistro.update(estudiante)
            print("Estudiante creado con éxito.")
            self.guardar_en_json()
        else:
            print("Índice de registro no válido.")

    def modificar_info_estudiante(self, indice, **kwargs):
        if 0 <= indice < len(self.registros):
            estudiante = self.registros[indice]
            for key, value in kwargs.items():
                if key in estudiante:
                    estudiante[key] = value
            print("Información de estudiante modificada con éxito.")
            self.guardar_en_json()
        else:
            print("Índice de registro no válido.")
    
    def eliminar_estudiante(self, indice):
        if 0 <= indice < len(self.registros):
            estudiante = self.registros[indice]
            if estudiante.get('id_estudiante') is not None:
                estudiante_eliminado = self.registros.pop(indice)
                print(f"Estudiante eliminado con éxito: {estudiante_eliminado['nombre']}")
                self.guardar_en_json()
            else:
                print("El estudiante no tiene información para eliminar.")
        else:
            print("Índice de estudiante no válido.")

    def crear_carnet(self, indice):
        if 0 <= indice < len(self.registros):
            estudiante = self.registros[indice]
            if estudiante.get('id_estudiante') is not None:
                carnet = f"Carnet-{estudiante['id_estudiante']}"
                estudiante['carnet'] = carnet
                print(f"Carnet creado para {estudiante['nombre']}: {carnet}")
                self.guardar_en_json()
            else:
                print("El estudiante no tiene información para crear el carnet.")
        else:
            print("Índice de registro no válido.")

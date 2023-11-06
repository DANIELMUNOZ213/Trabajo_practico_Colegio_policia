
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
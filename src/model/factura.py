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

    def calcular_costo_inscripcion(self, indice):
        if 0 <= indice < len(self.registro.registros):
            preregistro = self.registro.registros[indice]
            grado = preregistro["grado"]
            costo_base = self.tarifas_por_grado.get(grado, 0)
            if preregistro["convenio_policia"] == "si":  
                costo_con_descuento = costo_base * (1 - self.descuento_trabajo_policia)
                return costo_con_descuento
            else:
                return costo_base
        else:
            return None 

    def generar_factura(self, indice):
        costo_inscripcion = self.calcular_costo_inscripcion(indice)
        if costo_inscripcion is not None:
            preregistro = self.registro.registros[indice]
            print("Factura:")
            print(f"Nombre: {preregistro['nombre']}")
            print(f"Grado: {preregistro['grado']}")
            print(f"Costo de Inscripción: ${costo_inscripcion:.2f}")
        else:
            print("Índice de registro no válido.")
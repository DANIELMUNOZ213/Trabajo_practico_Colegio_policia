import unittest
from model.registro import Registro
from model.factura import Factura
class TestRegistro(unittest.TestCase):
    def setUp(self):
        self.registro = Registro()

    def test_creacion_preregistro_generacion_factura_creacion_estudiante(self):
        self.registro.crear_preregistro(
            nombre="Juan Perez",
            edad=15,
            identidad="ID123",
            grado="10",
            nombre_acudiente="Maria Perez",
            cedula_acudiente="Cedula789",
            trabaja_acudiente=True,
            telefono="123456789",
            direccion="Calle Principal 123",
            convenio_policia=True
        )

        self.assertEqual(len(self.registro.registros), 1)

        indice_preregistro = 0

        self.registro.modificar_info_preregistro(indice_preregistro, edad=16, direccion="Calle Nueva 456")

        preregistro_modificado = self.registro.registros[indice_preregistro]
        self.assertEqual(preregistro_modificado["edad"], 16)
        self.assertEqual(preregistro_modificado["direccion"], "Calle Nueva 456")

        self.registro.factura.generar_factura(indice_preregistro)

        factura_generada = preregistro_modificado.get("factura")
        self.assertIsNotNone(factura_generada)
        self.assertIn("costo_inscripcion", factura_generada)

        info_preregistro_con_factura = self.registro.mostrar_registro(indice_preregistro)
        self.assertIn("Factura", info_preregistro_con_factura)

if __name__ == '__main__':
    unittest.main()


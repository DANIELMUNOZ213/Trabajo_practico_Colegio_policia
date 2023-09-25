from src.model.registro import Registro
from src.model.factura import Factura

registro = Registro()
factura = Factura(registro)  

while True:
    print("\n1. Crear preregistro")
    print("2. Mostrar registro")
    print("3. Modificar preregistro")
    print("4. Eliminar registro")
    print("5. Mostrar todos los registros")
    print("6. Generar factura")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        identidad = input("Trajeta de identidad: ")
        grado = input("Grado: ")
        nombre_acudiente = input("Nombre del acudiente: ")
        cedula_acudiente = input("Cédula del acudiente: ")
        trabaja = input("¿Trabaja? (Si/No): ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        convenio_policia = input("¿Convenio con la policía? (Si/No): ")

        registro.crear_preregistro(
            nombre, edad, identidad, grado, nombre_acudiente, cedula_acudiente,
            trabaja, telefono, direccion, convenio_policia, factura
        )

    elif opcion == "2":
        indice_mostrar = int(input("Ingrese el índice del preregistro que desea mostrar: "))
        registro.mostrar_registro(indice_mostrar)

    elif opcion == "3":
        indice_modificar = int(input("Ingrese el índice del preregistro que desea modificar: "))
        if 0 <= indice_modificar < len(registro.registros):
            nuevos_valores = {}
            for campo in registro.registros[indice_modificar]:
                valor_nuevo = input(f"Nuevo {campo} (deje en blanco para mantener el valor actual): ")
                if valor_nuevo:
                    nuevos_valores[campo] = valor_nuevo

            registro.modificar_preregistro(indice_modificar, **nuevos_valores)
        else:
            print("Índice de registro no válido.")

    elif opcion == "4":
        indice_eliminar = int(input("Ingrese el índice del preregistro que desea eliminar: "))
        registro.eliminar_registro(indice_eliminar)

    elif opcion == "5":
        print("Registros:")
        for i, preregistro in enumerate(registro.registros):
            print(f"Registro {i + 1}:")
            for key, value in preregistro.items():
                print(f"{key}: {value}")

    elif opcion == "6":
        indice_generar_factura = int(input("Ingrese el índice del preregistro para generar la factura: "))
        factura.generar_factura(indice_generar_factura)

    elif opcion == "7":
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
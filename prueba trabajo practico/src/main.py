from model.registro import Registro
from model.factura import Factura
from interfaz_grafica import InterfazGrafica

if __name__ == "__main__":
    registro = Registro()
    factura = Factura(registro)
    app = InterfazGrafica(registro, factura)
    app.ventana.mainloop()

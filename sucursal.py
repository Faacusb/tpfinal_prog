class Sucursal:
    def __init__(self, numero_id, direccion):
        self.__numero_id = numero_id
        self.__direccion = direccion
        self.__ventas = []

    def establecerNumeroId(self, numero_id):
        self.__numero_id = numero_id

    def establecerDireccion(self, direccion):
        self.direccion = direccion

    def agregarVenta(self, venta):
        self.__ventas.append(venta)

    def removerVenta(self, venta):
        self.__ventas.remove(venta)

    def obtenerNumeroId(self):
        return self.__numero_id

    def obtenerDireccion(self):
        return self.__direccion

    def obtenerVentas(self):
        return self.__ventas

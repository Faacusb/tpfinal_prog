class Venta:
    def __init__(self, numeroId, fecha, clienteId, vehiculoId, monto):
        self.__numeroId = numeroId
        self.__fecha = fecha
        self.__clienteId = clienteId
        self.__vehiculoId = vehiculoId
        self.__monto = monto

    def establecerNumeroId(self,numeroId):
        self.__numeroId = numeroId

    def establecerFecha(self, fecha):
        self.__fecha = fecha

    def establecerClienteId(self, clienteId):
        self.__clienteId = clienteId

    def establecerVehiculoId(self, vehiculoId):
        self.__vehiculoId = vehiculoId

    def establecerMonto(self, monto):
        self.__monto = monto    

    def obtenerNumeroId(self):
        return self.__numeroId
    
    def obtenerFecha(self):
        return self.__fecha

    def obtenerClienteId(self):
        return self.__clienteId

    def obtenerVehiculoId(self):
        return self.__vehiculoId

    def obtenerMonto(self):
        return self.__monto
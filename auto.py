import vehiculo


class Auto(vehiculo.Vehiculo):
    def __init__(self, numero_id, marca, modelo, anio, sucursal_id, estado_id, airbags, frenosAbs, caballosFuerza):
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
        self.__airbags = airbags
        self.__frenosAbs = frenosAbs
        self.__caballosFuerza = caballosFuerza
    
    def establecerAirbags(self, airbags):
        self.__airbags = airbags

    def establecerFrenosAbs(self, frenosAbs):
        self.__frenosAbs = frenosAbs

    def establecerCaballosFuerza(self, caballosFuerza):
        self.__caballosFuerza = caballosFuerza

    def obtenerAirbags(self):
        return self.__airbags
    
    def obtenerFrenosAbs(self):
        return self.__frenosAbs
    
    def obtenerCaballosFuerza(self):
        return self.__caballosFuerza
    
    

class Cliente:
    def __init__(self, numeroId, nombre, apellidos, mail):
        self.__numeroId = numeroId
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = mail

    def establecerNumeroId(self, numero_id):
        self.__numero_id = numero_id

    def establecerNombres(self, nombres):
        self.__nombre = nombres

    def establecerApellidos(self, apellidos):
        self.__apellidos = apellidos

    def establecerEmail(self, email):
        self.__email = email

    def obtenerNumeroId(self):
        return self.__numero_id
    
    def obtenerNombres(self):
        return self.__nombre
    
    def obtenerApellidos(self):
        return self.__apellidos
    
    def obtenerEmail(self):
        return self.__email

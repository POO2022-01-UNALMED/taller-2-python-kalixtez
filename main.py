class Motor:
    def __init__(self):
        self.numeroCilindros = 0
        self.tipo = ""
        self.registro = 0

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Asiento:
    POSIBLES_COLORES = ["rojo", "verde", "amarillo", "negro", "blanco"]
    def __init__(self):
        self.color = ""
        self.precio = 0
        self.registro = 0

    def cambiarColor(self, color):
        if color in POSIBLES_COLORES:
            self.color = color


class Auto:
    cantidadCreados = 0
    def __init__(self):
        self.modelo = ""
        self.precio = 0
        self.marca = ""
        self.asientos = []
        self.motor = Motor()
        self.registro = 0

    def cantidadAsientos(self):
        return len(asientos)

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piesas no son originales"
            
        for i in range(0, len(asientos) - 1):
            if self.registro != asientos[i].registro:
                return "Las piezas no son originales"

        return "Auto original"


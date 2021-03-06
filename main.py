class Motor:
    def __init__(self, nc, tipo, registro):
        self.numeroCilindros = nc
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Asiento:
    POSIBLES_COLORES = ["rojo", "verde", "amarillo", "negro", "blanco"]
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in Asiento.POSIBLES_COLORES:
            self.color = color


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.asientos = asientos
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        count = 0
        for i in self.asientos:
            if i != None:
                count += 1
                
        return count

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piesas no son originales"
            
        for i in range(0, len(self.asientos) - 1):
            if self.asientos[i] != None:
                if self.registro != self.asientos[i].registro:
                    return "Las piezas no son originales"

        return "Auto original"


import math
class Point:
  definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
  def __init__(self, x: float=0, y: float=0):
    self.x = x
    self.y = y
  def move(self, new_x: float, new_y: float):
    self.x = new_x
    self.y = new_y
  def reset(self):
    self.x = 0
    self.y = 0

class Line:
    def __init__(self, longitud:float, pendiente: float, punto_inicio:Point, punto_final:Point):
        self.longitud= longitud
        self.pendiente = pendiente
        self.punto_inicio = punto_inicio
        self.punto_final = punto_final
    #Metodos de la clase Line
    def calcular_longitud(self):
       distancia = math.sqrt((self.punto_final.x - self.punto_inicio.x)**2 + (self.punto_final.y - self.punto_inicio.y)**2) 
       return distancia
    def calcular_pendiente(self):
       opuesto = self.punto_final.y - self.punto_inicio.y
       adjacente = self.punto_final.x - self.punto_inicio.x
       angulo = (180/math.pi)*(math.atan(opuesto / adjacente))
       #Calculamos el angulo en grados
       if opuesto > 0 and adjacente > 0:
          return angulo
       if opuesto > 0 and adjacente < 0:
          return 180 - angulo
       if opuesto < 0 and adjacente < 0:
          return 180 + angulo
       if opuesto < 0 and adjacente > 0:
          return 360 - angulo
    #Verificamos si la linea cruza el eje horizontal o vertical
    #Para el eje horizontal verificamos si la coordenada y de los puntos inicial y final son iguales a 0 o si una es menor que 0 y la otra mayor que 0
    def calcular_cruce_horizontal(self):
       if self.punto_inicio.y == 0 or self.punto_final.y == 0:
          return True
       elif self.punto_inicio.y < 0 and self.punto_final.y > 0:
          return True
       elif self.punto_inicio.y > 0 and self.punto_final.y < 0:
          return True
       else :
          return False
    #Para el eje vertical verificamos si la coordenada x de los puntos inicial y final son iguales a 0 o si una es menor que 0 y la otra mayor que 0
    def calcular_cruce_vertical(self):
       if self.punto_inicio.x == 0 or self.punto_final.x == 0:
          return True
       elif self.punto_inicio.x < 0 and self.punto_final.x > 0:
          return True
       elif self.punto_inicio.x > 0 and self.punto_final.x < 0:
          return True
       else :
          return False
class Rectangule:
    def __init__(self, linea1:Line, linea2:Line, linea3:Line, linea4:Line):
        self.linea1 = linea1
        self.linea2 = linea2
    def crear_rectangulo(self):
        esquina1 = self.linea1.punto_inicio
        esquina2 = self.linea1.punto_final
        esquina3 = Point(self.linea2.punto_inicio.x, self.linea1.punto_final.y)
        esquina4 = Point(self.linea2.punto_final.x, self.linea1.punto_inicio.y)

        self.esquinas = [esquina1, esquina2, esquina3, esquina4]

        # Creamos las otras dos líneas
        self.linea3 = Line(
            longitud=self.linea1.calcular_longitud(),
            pendiente=self.linea1.calcular_pendiente(),
            punto_inicio = esquina2,
            punto_final = esquina3
        )
        self.linea4 = Line(
            longitud = self.linea2.calcular_longitud(),
            pendiente = self.linea2.calcular_pendiente(),
            punto_inicio = esquina4,
            punto_final = esquina1
        )

        # Calculamos el punto medio del rectángulo
        self.punto_medio = Point(
            (esquina1.x + esquina3.x) / 2,
            (esquina1.y + esquina3.y) / 2
        )

        return self.esquinas, self.punto_medio


class Parqueadero:
    VACIO = 0

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.parqueadero = [[self.VACIO for _ in range(columnas)] for _ in range(filas)]

    def mostrar_parqueadero(self):
        print("------------------------------")
        for fila in self.parqueadero:
            for plaza in fila:
                print(plaza, end="\t")
            print("\n")
        print("------------------------------")

    def ingresar_vehiculo_parqueadero(self,indice_fila:int,indice_columna:int):
        if self.parqueadero[indice_fila][indice_columna] == 0:
            self.parqueadero[indice_fila][indice_columna] = 1
            print("El vehículo se ingresó exitosamente")


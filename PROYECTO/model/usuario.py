from model.parqueadero import Parqueadero

class Usuario:
    

    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.parqueadero_asociado = None

    def asociar_parqueadero(self, parqueadero):
        self.parqueadero_asociado = parqueadero
        
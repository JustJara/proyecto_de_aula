from model.usuario import Usuario
from model.parqueadero import Parqueadero
from model.usuario_existente_error import UsuarioExistenteError
from model.usuario_error import UsuarioError

class Estacionamiento:
    def __init__(self):
        self.lista_usuario = []
        self.usuario_actual = None

    def inicializar_parqueadero(self,filas:int,columnas:int):
        self.parqueadero = Parqueadero(filas,columnas)


    def registrar_usuario(self, nombre_usuario, contraseña):
        usuario = Usuario(nombre_usuario, contraseña)
        for u in self.lista_usuario:
            if usuario.nombre_usuario == u.nombre_usuario:
                raise UsuarioExistenteError(usuario)

        # Solicitar información del parqueadero al usuario
        filas = int(input("Ingrese la cantidad de filas del parqueadero: "))
        columnas = int(input("Ingrese la cantidad de columnas del parqueadero: "))

        # Inicializar y asociar el parqueadero al usuario
        parqueadero = Parqueadero(filas, columnas)
        usuario.asociar_parqueadero(parqueadero)
        self.lista_usuario.append(usuario)  # Agregar usuario a la lista
        return usuario

    def iniciar_sesion_usuario(self, nombre_usuario, contraseña):
        for usuario in self.lista_usuario:
            if nombre_usuario == usuario.nombre_usuario and contraseña == usuario.contraseña:
                print("Ha iniciado sesión exitosamente")
                self.usuario_actual = usuario  # Establecer el usuario actualmente logueado
                return True
        raise UsuarioError("Nombre de usuario o contraseña incorrectos")

    def cerrar_sesion(self):
        print("Sesión cerrada exitosamente")
        self.usuario_actual = None
                        
    def mostrar_parqueadero(self):
        self.parqueadero.mostrar_parqueadero()

    def ingreasr_vehiculo_parqueadero(self,indice_fila:int,indice_columna:int):
        self.usuario_actual.parqueadero_asociado.ingresar_vehiculo_parqueadero(indice_fila,indice_columna)
    
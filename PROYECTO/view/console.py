from model.estacionamiento import Estacionamiento
from model.usuario_existente_error import UsuarioExistenteError
from model.usuario_error import UsuarioError

class UIConsola:

    def __init__(self) -> None:
        self.estacionamiento: Estacionamiento = Estacionamiento()
    
    def registrar_usuario(self):
        try:
            print("------------------------")
            print("Bienvenido al sistema de parqueaderos P&J")
            print("Para registrarte debes seguir las instrucciones")
            print("Ingresa el nombre de usuario: ")
            nombre_usuario: str = str(input())
            print("Ingrese la contraseña: ")
            contraseña: str = str(input())

            # Registrar usuario y parqueadero
            usuario = self.estacionamiento.registrar_usuario(nombre_usuario, contraseña)

            print(f"Usuario {usuario.nombre_usuario} registrado exitosamente")
            print(f"Parqueadero de {usuario.nombre_usuario} creado y asociado exitosamente")
            
        except UsuarioExistenteError as uee:
            print(f"Error: UsuarioExistenteError - {uee}")


    def crear_parqueadero(self):
        print("------------------------")
        print("Para crear el parqueadero asociado sigue las instrucciones")
        print("Ingresa la cantidad de filas del parqueadero: ")
        filas = int(input())
        print("Ingresa la cantidad de columnas")
        columnas = int(input())
        parqueadero = self.estacionamiento.inicializar_parqueadero(filas,columnas)
        return parqueadero
    
    def iniciar_sesion(self):
        print("------------------------")
        print("Para iniciar sesión debes de seguir las instrucciones.")
        print("Ingresa el nombre de usuario")
        nombre_usuario = str(input())
        print("Ingrese la contraseña")
        contraseña = str(input())
        try:
            while True:
                if self.estacionamiento.iniciar_sesion_usuario(nombre_usuario, contraseña):
                    return True
        except UsuarioError as ue:
            print(f"Error: {ue}")
            return False


    def ejecutar_app(self):
        while True:
            self.mostrar_menu_inicial()
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.registrar_usuario()
            if opcion == 2:
                if self.iniciar_sesion():
                    self.ejecutar_app_dentro()
            if opcion == 3:
                print("¡Vuelve pronto!")
                break
        
    def ejecutar_app_dentro(self):
        while True:
            self.mostrar_menu_dentro_app()
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.mostrar_parqueadero()
            if opcion == 2:
                self.ingresar_vehiculo()
            if opcion == 3:
                pass
            if opcion == 4:
                print("Sesión cerrada exitosamente")
                break

    @staticmethod
    def mostrar_menu_inicial():
        print("------------------------")
        print("Escoje la opción según lo que deseas hacer")
        print("1. Registrarse")
        print("2. Logearse")
        print("3. Salir")
        print("------------------------")

    @staticmethod
    def mostrar_menu_dentro_app():
        print("------------------------")
        print("Escoge la opción según lo que quieras hacer")
        print("1. Mostrar parqueadero")
        print("2. Ingresar vehiculo")
        print("3. Retirar vehiculo")
        print("4. Cerrar sesión")
        print("------------------------")

    def mostrar_parqueadero(self):
        usuario_actual = self.estacionamiento.usuario_actual  # Asegúrate de tener un mecanismo para gestionar el usuario actualmente logueado
        if usuario_actual:
            usuario_actual.parqueadero_asociado.mostrar_parqueadero()
        else:
            print("Ningún usuario logueado.")

    def ingresar_vehiculo(self):
        usuario_actual = self.estacionamiento.usuario_actual  # Asegúrate de tener un mecanismo para gestionar el usuario actualmente logueado
        if usuario_actual:
            print("-------------------------")
            indice_fila = int(input("Ingrese el índice de la fila: "))
            indice_columna = int(input("Ingrese el índice de la columna: "))
            self.estacionamiento.ingreasr_vehiculo_parqueadero(indice_fila,indice_columna)

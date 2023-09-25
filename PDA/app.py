
from model.parqueadero import *


def registro_usuario() -> User:
        print("------------------------------")
        print("Bienvenido al sistema de parqueaderos P&J")
        print("Para registrate debes seguir las instrucciones.")
        print("Ingresa el nombre de usuario: ")
        nombre_usuario : str = input()
        print("Ingrese la contraseña")
        password : str = input()
        parqueadero : Parqueadero = crear_parqueadero()
        usuario : User= User(nombre_usuario,password,parqueadero)
        print("------------------------------")
        User.agregar_usuario_lista_usuarios(usuario)

        print(f"lista usuarios es = {User.lista_usuarios}")
        return usuario
        
def iniciar_sesion() -> User:
        print("------------------------------")
        print("Para iniciar sesión sigue las instrucciones")
        print("Ingresa el nombre de usuario: ")
        nombre_usuario : str = input()
        print("Ingrese la contrasena")
        contrasena : str = input()
        usuario : User = User.buscar_usuario(nombre_usuario,contrasena)
        print("------------------------------")
        if User.iniciar_sesion(usuario):
              return usuario
        else: 
              return None


def menu_inicio():
        print("------------------------------")
        print("Bienvenido a la aplicación")
        print("Según lo que desees hacer escribe el número.")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("4. Salir")
        print("------------------------------")

def menu_dentro_app():
        print("------------------------------")
        print("Bienvenido al sistema de parqueos.")
        print("Según lo que desees: ")
        print("------------------------------")
        print("1. Ingresar Vehículo")
        print("2. Reitrar vehícuholo")
        print("3. Reservar parqueadero")
        print("4. Calcular tarifa")
        print("5. Salir")

def iniciar_aplicacion():
        usuario = None
        while True:
            menu_inicio()
            eleccion = int(input())
            if eleccion == 1:
                usuario = registro_usuario()
            if eleccion == 2:
                usuario = iniciar_sesion()
                if usuario:
                      while True:
                        print("------------------------------")
                        usuario.parqueadero.mostrar_parqueadero()
                        menu_dentro_app()
                        opcion = int(input())
                        if opcion == 5:
                                print("¡Vuelve pronto!")
                                break
                        print("------------------------------")
            if eleccion == 4:
                print("¡Vuelve pronto!")
                break
            
            
def crear_parqueadero() -> Parqueadero:
        print("------------------------------")
        print("Ahora que iniciaste sesión crea el parqueadero virtualmente")
        print("Ingresa el tamaño en filas (Horizontalmente)")
        filas : int = int(input())
        print("Ingresa el tamaño en columnas (verticalmente)")
        columnas : int = int(input())
        parqueadero = Parqueadero.crear_parqueadero(filas,columnas)
        parqueadero : Parqueadero = Parqueadero(filas,columnas,parqueadero)
        return parqueadero

Consola = iniciar_aplicacion()
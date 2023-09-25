class User:
    lista_usuarios =[]
    def __init__(self,n_usuario : str,contrasena : str,parqueadero):
        self.nombre_usuario : str = n_usuario
        self.contrasena : str = contrasena
        self.parqueadero : Parqueadero = parqueadero
        
    
    def agregar_usuario_lista_usuarios(usuario : str):
        if usuario not in User.lista_usuarios:
            User.lista_usuarios.append(usuario)
            print("El usuario fue registrado exitosamente")
        else:
            print("El usuario ya está registrado")



    def iniciar_sesion(self) -> bool:
        usuario : User = User.buscar_usuario(self.nombre_usuario,self.contrasena)
        if usuario.nombre_usuario == None and usuario.contrasena== None:
            print("El usuario o contraseña son incorrectas")
            return False
        else:
            print("Inicio de sesión exitoso")
            return True
        
    def buscar_usuario(nombre_usuario : str,contrasena : str):
        posicion : int = 0
        for u in User.lista_usuarios:
            if nombre_usuario == u.nombre_usuario and contrasena == u.contrasena:
                usuario : User = User.lista_usuarios[posicion]
                return usuario
            else:
                return User(None,None,None)
            
        posicion+=1


class Vehiculo:

    def verificar_posicion(self):
        pass

    def ingresar_vehiculo(self):
        pass

    def retirar_vehiculo(self):
        pass


class Parqueadero:
    def __init__(self, filas: int, columnas: int,parqueadero):  
        self.filas : int = filas
        self.columnas: int = columnas
        self.parqueadero: Parqueadero = parqueadero

    def crear_parqueadero(filas: int,columnas: int):
        parqueadero : list[Vehiculo] = []  
        for f in range(filas):
            fila = []  
            for c in range(columnas):
                fila.append(0)  
            parqueadero.append(fila)  
        print("Parqueadero creado exitosamente")
        return parqueadero


    def mostrar_parqueadero(self):
        print("------------------------------")
        filas = self.filas
        columnas = self.columnas
        for f in range(filas):
            for c in range(columnas):
                print(self.parqueadero[f][c], end="\t")
            print("\n")
        print("------------------------------")

    def reservar_parqueadero(self):
        pass

    def calcular_tarifa(self):
        pass

    def generar_factura(self):
        pass
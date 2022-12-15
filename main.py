class Usuario():
    nombre = ""
    apellido = ""
    cedula = 0
    edad = 0

    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad

class Cuenta (Usuario):
    monto = 0

    def __init__(self, nombre, apellido, cedula, edad, monto):
        super().__init__(nombre, apellido, cedula, edad)
        self.monto = monto

    def mostrar(self):
        print(f"La cuenta de {self.nombre} {self.apellido}, de {self.edad} años, con cedula {self.cedula}, tiene un monto de {self.monto} pesos")

    def beneficiar(self):
        if(self.edad >= 18 and self.edad <=28):
            return True
        return False
        

    def ingresar(self, dinero):
        if(dinero < 0):
            print('No se admiten valores negativos')
            return False
        
        self.monto += dinero
        print(f'Se ingresaron {dinero} pesos, el valor actual de la cuenta es {self.monto}')
        return True

    def retirar(self, dinero):
        if(dinero < 0):
            print('No se admiten valores negativos')
            return False
        
        self.monto -= dinero
        print(f'Se retiraron {dinero} pesos, el valor actual de la cuenta es {self.monto}')
        return True

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getCedula(self):
        return self.cedula

    def getEdad(self):
        return self.edad

    def getMonto(self):
        return self.monto
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido

    def setCedula(self, cedula):
        self.cedula = cedula

    def setEdad(self, edad):
        self.edad = edad

    def setMonto(self, monto):
        self.monto = monto

class beneficio(Cuenta):
    def __init__(self, nombre, apellido, cedula, edad, monto):
        super().__init__(nombre, apellido, cedula, edad, monto)
        self.monto += self.monto*0.05

usuario_1 = Usuario('Juan', 'Perez', 123, 20)
cuenta_1 = Cuenta(usuario_1.nombre, usuario_1.apellido, usuario_1.cedula, usuario_1.edad, 10000)

cuenta_1.mostrar()
cuenta_1.ingresar(10000)
cuenta_1.retirar(5000)

if(cuenta_1.beneficiar()):
    ben1 = beneficio(cuenta_1.nombre, cuenta_1.apellido, cuenta_1.cedula, cuenta_1.edad, cuenta_1.monto)
    ben1.mostrar()
else: 
    print('Esta cuenta no es apta para beneficios')
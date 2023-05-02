# class Profesor:
#     def __init__(self, param_nombre, param_email):
#         self.nombre = param_nombre
#         self.email = param_email
#         self.asistencia = 0

#     def cambiar_nombre(self, nuevo_nombre):
#         self.nombre = nuevo_nombre
    
#     def asistencia_clase(self):
#         self.asistencia += 1

# #def __init__    
# profesor_pepe = Profesor('pepe', 'jose@gmail.com')
# print(profesor_pepe.nombre)
# print(profesor_pepe.email)
# print(profesor_pepe.asistencia)

# # cambiar nombre
# profesor_pepe.cambiar_nombre("JOSA")
# print(profesor_pepe.nombre)
# profesor_pepe.cambiar_nombre("FACUNDO")
# print(profesor_pepe.nombre)

# # asistencia 
# profesor_pepe.asistencia_clase()
# profesor_pepe.asistencia_clase()
# print(profesor_pepe.asistencia)

class Persona:
    def __init__(self,param_nombre,param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def asistencia_clase(self):
        self.asistencia += 1

class Profesor(Persona):
    def __init__(self,param_nombre, param_email,legajo_empleado):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre,param_email)

class Alumno(Persona):
    def __init__(self,param_nombre, param_email,numero_alumno):
        self.numero_alumno = numero_alumno
        self.materias_cursando = []
        super().__init__(param_nombre, param_email)

    def cursando(self,materia):
            self.materias_cursando.append(materia)

diego = Alumno('diego','diegoxh85@gmail.ccom','18')
print(id(diego))

print('nombre: ')
print(diego.nombre)

print('email: ')
print(diego.email)

print('numero: ')
print(diego.numero_alumno)

materias = diego.materias_cursando
print(materias)

diego.cursando('fisica')
diego.cursando('matematica')
diego.cursando('calculo')
print(materias)


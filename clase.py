class Persona:
    def __init__(self, persona:dict):
        self.nombre = persona.get('nombre')
        self.apellido = persona.get('apellido')

    cliente1 = {
        'nombre' : 'Pepe',
        'apellido' : 'Honguito',
    }

    cliente2 = {
        'nombre' : 'Pepa',
        'apellido' : 'Fernandez',
    }

    if __name__ == '__main__':
        p1 = Persona(cliente1)
        p2 = Persona(cliente2)
        p3 = p1
        p3.nombre = 'Pablo'
        print(p1)
        print(p2)
        print(p3)

    def __init__(self, nombre = "",apellido=""):
        self.nombre = nombre
        self.apellido = apellido
    
    def __repr__(self):
        return f"->Persona:[nombre]={self.nombre} [apellido] = {self.apellido}"

    # p4 = Persona('Juan', 'Molina')





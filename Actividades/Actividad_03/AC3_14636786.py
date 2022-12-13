class salas():
    def __init__(self,ancho, largo, MaxPersonas, asientos):
        self.personas=[]
        self.largo=largo
        self.ancho=ancho
        self.asientos=asientos

class SalaDeClases(salas):
    def __init__(self,ancho, largo, MaxPersonas, asientos):
        super().__init__(asientos,*argv)
        self.asientos=asientos
class SalaDeReuniones(salas):
    
    def __init__(self,ancho, largo, MaxPersonas, asientos):
        super().__init__(asientos,*argv)
        self.asientos=asientos
        
class Subterraneo(salas):
    def __init__(self, ancho, largo, MaxPersonas):
        super().__init__(*argv)
        
class persona():
    def __init__(self, nombre,asiento):
        self.nombre=''
    def entrar_a_sala(self, sala):
        sala.personas.append(self)
        if type(self) is alumno:
            sala.asientos      
            
                         
class profesor(persona):
    def __init__(self):
        super().__init__(*argv)
        
class alumno(persona):
    def __init__(self):
        super().__init__(*argv)
        
    
        
    
        

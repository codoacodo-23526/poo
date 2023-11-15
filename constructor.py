class Jugador:
    def __init__(self,nombre,apellido, goles):
        self.nombre = nombre
        self.apellido = apellido
        self.goles = goles
        
    def __str__(self):
        return f"El jugador {self.nombre} {self.apellido} tiene {self.goles} goles"
    
    def __del__(self):
        print("Se ha borrado el objeto")
        
    def destruir_objeto(self):
        del self
        
    def saludar(self):
        print(f"Hola {self.nombre} y {self.apellido}")
        
    def despedirse(self):
        print(f"Adios {self.nombre} y {self.apellido}")
        
    


#programa principal

jugador1 = Jugador("Lionel","Messi", 1000) # Creacion de un objeto de tipo persona
jugador2 = Jugador("Cristiano","Ronaldo", 800) # Creacion de un objeto de tipo persona


print(f"El jugador {jugador1.nombre} {jugador1.apellido} tiene {jugador1.goles} goles")

print(f"El jugador {jugador2.nombre} {jugador2.apellido} tiene {jugador2.goles} goles")


print(jugador1.saludar()) # Llamada a un metodo de la clase persona

print(jugador2.saludar()) # Llamada a un metodo de la clase persona

print(jugador1)
print(jugador2)

del jugador1 # Borrado del objeto jugador1
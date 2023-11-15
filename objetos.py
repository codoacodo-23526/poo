# La clase(molde/prototipo) es el molde para crear objetos
# El objeto que tiene atributos y metodos
# El objeto es una instancia de una clase 

# Definicion de una clase
class Persona:
    nombre = ""
    piernas = 2
    
    def constructor(self, nombre): # self es una referencia a la instancia de la clase
        self.nombre = nombre
    
    
    def saludar(self): # self es una referencia a la instancia de la clase
        print("Hola" + self.nombre)
        
    def despedirse(self):
        print("Adios" + self.nombre)
        
        

#PROGAMA PRINCIPAL

persona1 = Persona() # Creacion de un objeto de tipo persona

persona2 = Persona() # Creacion de un objeto de tipo persona    


mis_piernas = persona1.piernas # Acceso a un atributo de la clase persona   
mis_piernas_2 = persona2.piernas # Acceso a un atributo de la clase persona

print(persona1.saludar()) # Llamada a un metodo de la clase persona
print(persona2.saludar()) # Llamada a un metodo de la clase persona
print(persona1.despedirse()) # Llamada a un metodo de la clase persona
print(persona2.despedirse()) # Llamada a un metodo de la clase persona

persona3 = Persona() # Creacion de un objeto de tipo persona
persona3.inicializar("Lionel") # Llamada a un metodo de la clase persona
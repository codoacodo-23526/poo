# # 1 - CARGAR ALUMNO
# # 2 - LISTAR ALUMNOS
# # 3 - MOSTRAR ALUMNOS CON NOTAS MAYORES A 7
# # 4 - SALIR DEL PROGRAMA

# class Alumno:
#     def __init__(self):
#         self.nombres = []
#         self.notas = []
        
#     def menu(self):
#         opcion = 0
#         while opcion != 4:
#             print("1 - Cargar Alumnos")
#             print("2 - Listar Alumbos")
#             print("3 - Mostrar aprobados")
#             print("4 - Finalizo el programa")
#             print("")
#             opcion = int(input("ingrese su opcion: "))
#             if opcion == 1:
#                 self.cargar()
#             elif opcion == 2: 
#                 self.listar()
#             elif opcion == 3:
#                 self.mostrar_aprobados()
#             else:
#                 self.finalizar()
            
#     def cargar(self):
#         for a in range(5):
#             nombre = input("Nombre de alumno: ")
#             self.nombres.append(nombre)
#             nota = int(input("Ingresa la nota: "))
#             self.notas.append(nota) 
            
#     def listar(self):
#         print("Listado de alumnos")
#         for x in range(5):
#             print(f"Alumno: {self.nombres[x]} Nota: {self.notas[x]}")

#     def mostrar_aprobados(self):
#         print("Listado de alumnos")
#         for x in range(5):
#             if self.notas[x] >= 7:
#                 print(f"Alumno: {self.nombres[x]} Nota: {self.notas[x]} APROBADO")
                
#     def finalizar(self):
#         print("CERRO EL PROGRAMA")
        
# #PROGRAMA PRINCIPAL

# lista_de_alumnos = Alumno()
# lista_de_alumnos.menu()




# class Alumno:
#     nombre = ""
#     nota = 0
    
#     def cargar(self):
#         nombre = input("Nombre de alumno: ")
#         nota = int(input("Ingresa la nota: "))
        
        
# alumno = Alumno()

# for x in range(5):
#     alumno.cargar()
    
    
# alumno.listar()
# alumno.mostrar()

    

    



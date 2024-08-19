class Animal:
   def __init__(self, nombre, raza, edad, peso, color, sexo, propietario, telefono):
       self.nombre = nombre
       self.raza = raza
       self.edad = edad
       self.peso = peso
       self.color = color
       self.sexo = sexo
       self.propietario = propietario
       self.telefono = telefono
       self.estado = "NO ATENDIDO"  # Estado inicial
       self.tamaño = self.determinar_tamaño()  # Determinar tamaño según el peso
   def determinar_tamaño(self):
       return "Grande" if self.peso >= 10 else "Pequeño"
   def atender_animal(self):
       self.estado = "ATENDIDO"  # Cambiar el estado a "ATENDIDO"
   def obtener_datos(self):
       datos = [
           f"Nombre: {self.nombre}",
           f"Raza: {self.raza}",
           f"Edad: {self.edad} años",
           f"Peso: {self.peso} kg",
           f"Color: {self.color}",
           f"Sexo: {self.sexo}",
           f"Propietario: {self.propietario}",
           f"Teléfono: {self.telefono}",
           f"Estado: {self.estado}",
           f"Tamaño: {self.tamaño}"
       ]
       return datos

class ClinicaVeterinaria:
   def __init__(self):
       self.animales = []  # Lista para almacenar los objetos Animal
   def registrar_animal(self):
       nombre = input("Ingrese el nombre del animal: ")
       raza = input("Ingrese la raza del animal: ")
       edad = int(input("Ingrese la edad del animal (en años): "))
       peso = float(input("Ingrese el peso del animal (en kg): "))
       color = input("Ingrese el color del animal: ")
       sexo = input("Ingrese el sexo del animal (Macho/Hembra): ")
       propietario = input("Ingrese el nombre del propietario: ")
       telefono = input("Ingrese el número de teléfono del propietario: ")
       animal = Animal(nombre, raza, edad, peso, color, sexo, propietario, telefono)
       animal.atender_animal()  # Marcar el animal como atendido
       self.animales.append(animal)  # Agregar el animal a la lista
       print(f"\nEl animal {nombre} ha sido registrado con éxito.\n")
   def buscar_animal_por_nombre(self, nombre):
       for animal in self.animales:
           if animal.nombre == nombre:
               return animal.obtener_datos()
       return None

# Ejemplo de uso
clinica = ClinicaVeterinaria()
while True:
   print("1. Registrar un animal")
   print("2. Mostrar información de un animal por nombre")
   print("3. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       clinica.registrar_animal()
   elif opcion == "2":
       nombre_buscar = input("Ingrese el nombre del animal a buscar: ")
       datos = clinica.buscar_animal_por_nombre(nombre_buscar)
       if datos:
           print("\nInformación del animal:\n")
           for linea in datos:
               print(linea)
           print("")
       else:
           print(f"No se encontró ningún animal con el nombre {nombre_buscar}.\n")
   elif opcion == "3":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")